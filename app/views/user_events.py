import logging

from marshmallow import fields

from app.models.UserEventRelationModel import UserEventRelationModelSchema
from flask import Blueprint, abort, make_response
from flask_api import status
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from app.services.db.UserEventController import UserEventService
from app.util.db_tool import unrequire
from libs.parameters import RequestParams
from libs.security import get_token_info

logger = logging.getLogger(__name__)
app = Blueprint(
    'user_events',
    __name__,
    url_prefix='/api/user_events'
)


@doc(tags=['UserEvents List view'])
class UserEventResourceList(MethodResource):
    event_service = UserEventService()

    @marshal_with(UserEventRelationModelSchema(many=True), code=status.HTTP_200_OK)
    @use_kwargs({
        **RequestParams.pagination_params(),
        **unrequire(UserEventRelationModelSchema().fields)
    })
    @doc(description='return all user_events')
    def get(self, **kwargs):
        _ = get_token_info()
        page = kwargs.pop('page')
        limit = kwargs.pop('limit')

        return self.event_service.get_multiple(
            page=page,
            limit=limit,
            kwarg_filters=kwargs
        ), status.HTTP_200_OK

    @use_kwargs({
        **UserEventRelationModelSchema().fields,
        'user_id_one': fields.Integer(required=True),
        'user_id_two': fields.Integer(required=True)
    })
    @marshal_with(UserEventRelationModelSchema, code=status.HTTP_201_CREATED)
    @doc(description='Create a new event')
    def post(self, **kwargs):
        _ = get_token_info()
        user_id_one = kwargs.pop('user_id_one')
        user_id_two = kwargs.pop('user_id_two')
        created = self.event_service.create(**kwargs)
        user_event_service = UserEventService()
        user_event_service.create(**{
            'user_id_one': user_id_one,
            'user_id_two': user_id_two,
            'event_id': created.id
        })
        return created, status.HTTP_201_CREATED


@doc(tags=['UserEvents detail view'])
class UserEventResourceDetail(MethodResource):
    event_service = UserEventService()

    @marshal_with(UserEventRelationModelSchema, code=status.HTTP_200_OK)
    @doc(description='return event with id')
    def get(self, event_id, **kwargs):
        _ = get_token_info()
        result = self.event_service.get_by_id(event_id)
        if result == None:
            abort(status.HTTP_404_NOT_FOUND)
        return result, status.HTTP_200_OK

    @marshal_with(None, code=status.HTTP_204_NO_CONTENT)
    @doc(description='delete a event')
    def delete(self, event_id, **kwargs):
        _ = get_token_info()
        result = self.event_service.delete_by_id(event_id)
        if result == False:
            abort(status.HTTP_404_NOT_FOUND)
        return make_response('', status.HTTP_204_NO_CONTENT)

    @use_kwargs(UserEventRelationModelSchema().fields)
    @marshal_with(UserEventRelationModelSchema, code=status.HTTP_200_OK)
    @doc(description='update a existing event')
    def put(self, event_id, **kwargs):
        _ = get_token_info()
        result = self.event_service.update_by_id(event_id, kwargs)
        if result == None:
            abort(status.HTTP_404_NOT_FOUND)
        return result, status.HTTP_200_OK

    @use_kwargs(unrequire(UserEventRelationModelSchema().fields))
    @doc(description='partially update a event')
    @marshal_with(UserEventRelationModelSchema, code=status.HTTP_200_OK)
    def patch(self, event_id, **kwargs):
        _ = get_token_info()
        result = self.event_service.update_by_id(event_id, kwargs)
        if result == None:
            abort(status.HTTP_404_NOT_FOUND)
        return result, status.HTTP_200_OK


app.add_url_rule(
    '',
    view_func=UserEventResourceList.as_view('UserEventResourceList'),
    methods=['GET', 'POST']
)
app.add_url_rule(
    '/<int:event_id>',
    view_func=UserEventResourceDetail.as_view('UserEventResourceDetail'),
    methods=['GET', 'PUT', 'DELETE', 'PATCH']
)
