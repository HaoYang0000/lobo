import logging

from app.models.EventModel import EventModelSchema
from flask import Blueprint, abort, make_response
from flask_api import status
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from app.services.db.EventController import EventService
from app.util.db_tool import unrequire
from libs.parameters import RequestParams

logger = logging.getLogger(__name__)
app = Blueprint(
    'events',
    __name__,
    url_prefix='/events'
)
@doc(tags=['Events List view'])
class EventResourceList(MethodResource):
    event_service = EventService()
    @marshal_with(EventModelSchema(many=True), code=status.HTTP_200_OK)
    @use_kwargs({
        **RequestParams.pagination_params(),
        **unrequire(EventModelSchema().fields)
    })
    @doc(description='return all events')
    def get(self, **kwargs):
        page = kwargs.pop('page')
        limit = kwargs.pop('limit')

        return self.event_service.get_multiple(
            page=page,
            limit=limit,
            kwarg_filters=kwargs
        ), status.HTTP_200_OK

    @use_kwargs(EventModelSchema().fields)
    @marshal_with(EventModelSchema, code=status.HTTP_201_CREATED)
    @doc(description='Create a new event')
    def post(self, **kwargs):
        new_service = self.event_service.create(**kwargs)
        return new_service, status.HTTP_201_CREATED

@doc(tags=['Events detail view'])
class EventResourceDetail(MethodResource):
    event_service = EventService()
    @marshal_with(EventModelSchema, code=status.HTTP_200_OK)
    @doc(description='return event with id')
    def get(self, event_id, **kwargs):
        result = self.event_service.get_by_id(event_id)
        if result == None:
            abort(status.HTTP_404_NOT_FOUND)
        return result, status.HTTP_200_OK
    
    @marshal_with(None, code=status.HTTP_204_NO_CONTENT)
    @doc(description='delete a event')
    def delete(self, event_id, **kwargs):
        result = self.event_service.delete_by_id(event_id)
        if result == False:
            abort(status.HTTP_404_NOT_FOUND)
        return make_response('', status.HTTP_204_NO_CONTENT)
    
    @use_kwargs(EventModelSchema().fields)
    @marshal_with(EventModelSchema, code=status.HTTP_200_OK)
    @doc(description='update a existing event')
    def put(self, event_id, **kwargs):
        result = self.event_service.update_by_id(event_id, kwargs)
        if result == None:
            abort(status.HTTP_404_NOT_FOUND)
        return result, status.HTTP_200_OK

    @use_kwargs(unrequire(EventModelSchema().fields))
    @doc(description='partially update a event')
    @marshal_with(EventModelSchema, code=status.HTTP_200_OK)
    def patch(self, event_id, **kwargs):
        result = self.event_service.update_by_id(event_id, kwargs)
        if result == None:
            abort(status.HTTP_404_NOT_FOUND)
        return result, status.HTTP_200_OK

app.add_url_rule(
    '',
    view_func=EventResourceList.as_view('EventResourceList'),
    methods=['GET', 'POST']
)
app.add_url_rule(
    '/<int:event_id>',
    view_func=EventResourceDetail.as_view('EventResourceDetail'),
    methods=['GET', 'PUT', 'DELETE', 'PATCH']
)
