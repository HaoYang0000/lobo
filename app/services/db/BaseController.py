from typing import List
from sqlalchemy.sql.elements import UnaryExpression

from app.main import db
from flask import abort
from flask_api import status
from sqlalchemy import inspect, exists, Column
from sqlalchemy.orm import joinedload, lazyload, Query, RelationshipProperty
from sqlalchemy import inspect, exists, func
import logging
from app.services.location import get_distance

from app.models.UserModel import UserModel
from libs.enums import RelationshipLoadOption

logger = logging.getLogger('flask.app')


class BaseService:
    model = None

    def get_all(self, **kwargs):
        """
        Return api list result
        
        Returns:
            model | null
        """
        return self.model.query.all()

    def get_multiple(
        self,
        page: int=1,
        limit: int=None,
        sort: UnaryExpression=None,
        load_options: dict=None,
        filters: list=None,
        kwarg_filters: dict=None,
        select_columns: List[Column]=None
    ) -> list:
        """
        Selects a set of paginated, filtered, and sorted records from the table
        set in self.model and returns a list of their models. Filter expressions
        can be sql expressions passed as positional arguments (ex. self.model.column==True)
        or as keyword arguments (ex. column_name=value).

        Keyword Arguments:
            page {int} -- Page of results (default: {1})
            limit {int} -- Number of results per page (default: {None})
            sort {UnaryExpression} -- Sqlalchemy sorting expression.
                (ex. self.model.column.asc()) (default: {None})
            load_options {dict} -- Controls loading technique for any relationships
                with other models. Parameter takes the form
                {RelationshipLoadOption: [Model.relationship, ...], ...} (default: {None})
            filters {list} -- List of sql expressions to filter query (ex. [self.model.column==True])
            kwarg_filters {dict} -- Dictionary of expressions to filter query (ex. {column_name: value})
            select_columns {List[Column]} -- Columns of self.model to select. All columns
                are selected by default. (default: {None})

        Returns:
            List[self.model] -- List of models or list of named tuples if a subset of columns are selected.
                If no results, an empty list is returned
        """
        # select specific columns
        if select_columns:
            query = db.session.query(*select_columns)
        else:
            query = db.session.query(self.model)

        # add query filters
        query = self._apply_filters_to_query(query, filters, kwarg_filters)

        # sorting
        if sort is not None:
            query = query.order_by(sort)

        # pagination
        offset = None
        if page is not None and limit is not None:
            offset = (page - 1) * limit
        query = query.limit(limit).offset(offset)

        # set relationship loading options
        if load_options:
            for option in load_options:
                for relationship in load_options.get(option):
                    query = BaseService._set_relationship_load_option(query, relationship, option)

        return query.all()

    def get_multiple_nearby(self, uid: int) -> list:
        # Get source user by uid
        source_user = self.model.query.filter(self.model.id == uid).one_or_none()

        # Get all guides
        guides = self.get_multiple(filters=[UserModel.is_guide == True])

        for guide in guides:
            distance = get_distance(source_user.latitude, source_user.longitude,
                                    guide.latitude, guide.longitude)
            guide.distance = distance

        # Calculate distances for all guides (guide_uid, distance)
        # Sort by distance; return sorted users
        return sorted(guides, key=lambda k: k.distance)

    def _apply_filters_to_query(self, query: Query, filters: list, kwarg_filters: dict) -> Query:
        """
        Applies filter criteria to a query. Filter expressions can be sql expressions
        or keyword arguments.

        Arguments:
            query {Query} -- Existing sql query
            filters {list} -- List of sql expressions to filter query (ex. [self.model.column==True])
            kwarg_filters {dict} -- Dictionary of expressions to filter query (ex. {column_name: value})

        Raises:
            AttributeError -- If kwarg_filters contains keys that aren't column names of self.model

        Returns:
            Query -- Modified sql query
        """
        if kwarg_filters:
            for k, v in kwarg_filters.items():
                try:
                    query = query.filter(getattr(self.model, k) == v)
                except AttributeError as e:
                    raise AttributeError(f'Cannot filter query with invalid model attribute \'{k}\'') from e
        if filters:
            for condition in filters:
                query = query.filter(condition)

        return query

    @staticmethod
    def _set_relationship_load_option(
            query: Query,
            relationship: RelationshipProperty,
            load_option: RelationshipLoadOption,
    ) -> Query:
        """
        Sets a model's relationship loading technique for a select query. Eager loading
        will perform the necessary join at the time the select query is executed. Lazy
        loading will issue a distinct select statement for the relationship at the time
        when the property is first accessed.

        Arguments:
            query {Query} -- Base select query
            relationship {RelationshipProperty} -- Model's relationship property
            load_option {RelationshipLoadOption} -- Relationship loading technique

        Returns:
            Query -- Select query with relationship loading options
        """

        if load_option == RelationshipLoadOption.LAZY:
            query = query.options(lazyload(relationship))
        elif load_option == RelationshipLoadOption.EAGER:
            query = query.options(joinedload(relationship))

        return query

    def get_by_id(self, id, **kwargs):
        """
        Return api detail result

        Args:
            param1 (int): primary key

        Returns:
            model | null
        """
        return self.model.query.filter(self.model.id == id).one_or_none()

    def create(self, **kwargs):
        """
        Add new model record

        Returns:
            model
        """
        new_model = self.model(**kwargs)
        db.session.add(new_model)
        db.session.commit()
        logger.debug('Creating new item {model_name} with {data}'.format(
                data=new_model, 
                model_name=self.model.__table__.name
            )
        )
        return new_model

    def delete_by_id(self, id, **kwargs):
        """
        Delete a record by id

        Args:
            param1 (int): primary key

        Returns:
            bool
        """
        record = self.get_by_id(id)

        if record == None:
            logger.debug('Deleting {model_name} failed with id: {id}, record not found'.format(
                    model_name=self.model.__table__.name, 
                    id=id
                )
            )
            return False
        else:
            db.session.delete(record)
            db.session.commit()
            logger.debug('Deleting {model_name} from {data}'.format(
                    data=record, 
                    model_name=self.model.__table__.name
                )
            )
            return True

    def update_by_id(self, id, data):
        """
        Update a record by id

        Args:
            param1 (int): primary key
        
        Returns:
            model | null
        """
        record = self.model.query.filter(self.model.id == id)

        if record.one_or_none() == None:
            logger.debug('Updating {model_name} failed with id: {id}, record not found'.format(
                    model_name=self.model.__table__.name, 
                    id=id
                )
            )
            return None
        else:
            record.update(data)
            db.session.commit()
            logger.debug('Updating {model_name} with {data}, id:{id}'.format(
                    data=data,
                    model_name=self.model.__table__.name,
                    id=id
                )
            )
            return record.first()
