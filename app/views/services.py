import logging

from app.models.ServiceModel import ServiceModelSchema
from flask import Blueprint, abort, make_response
from flask_api import status
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from app.services.db.ServiceController import ServiceService
from app.util.db_tool import unrequire
from libs.parameters import RequestParams

logger = logging.getLogger(__name__)
app = Blueprint(
    'services',
    __name__,
    url_prefix='/services'
)
@doc(tags=['Services List view'])
class ServiceResourceList(MethodResource):
    service_service = ServiceService()
    @marshal_with(ServiceModelSchema(many=True), code=status.HTTP_200_OK)
    @use_kwargs({
        **RequestParams.pagination_params(),
        **unrequire(ServiceModelSchema().fields)
    })
    @doc(description='return all services')
    def get(self, **kwargs):
        page = kwargs.pop('page')
        limit = kwargs.pop('limit')

        return self.service_service.get_multiple(
            page=page,
            limit=limit,
            kwarg_filters=kwargs
        ), status.HTTP_200_OK

    @use_kwargs(ServiceModelSchema().fields)
    @marshal_with(ServiceModelSchema, code=status.HTTP_201_CREATED)
    @doc(description='Create a new service')
    def post(self, **kwargs):
        new_service = self.service_service.create(**kwargs)
        return new_service, status.HTTP_201_CREATED

@doc(tags=['Services detail view'])
class ServiceResourceDetail(MethodResource):
    service_service = ServiceService()
    @marshal_with(ServiceModelSchema, code=status.HTTP_200_OK)
    @doc(description='return service with id')
    def get(self, service_id, **kwargs):
        result = self.service_service.get_by_id(service_id)
        if result == None:
            abort(status.HTTP_404_NOT_FOUND)
        return result, status.HTTP_200_OK
    
    @marshal_with(None, code=status.HTTP_204_NO_CONTENT)
    @doc(description='delete a service')
    def delete(self, service_id, **kwargs):
        result = self.service_service.delete_by_id(service_id)
        if result == False:
            abort(status.HTTP_404_NOT_FOUND)
        return make_response('', status.HTTP_204_NO_CONTENT)
    
    @use_kwargs(ServiceModelSchema().fields)
    @marshal_with(ServiceModelSchema, code=status.HTTP_200_OK)
    @doc(description='update a existing service')
    def put(self, service_id, **kwargs):
        result = self.service_service.update_by_id(service_id, kwargs)
        if result == None:
            abort(status.HTTP_404_NOT_FOUND)
        return result, status.HTTP_200_OK

    @use_kwargs(unrequire(ServiceModelSchema().fields))
    @doc(description='partially update a recurring frequency')
    @marshal_with(ServiceModelSchema, code=status.HTTP_200_OK)
    def patch(self, service_id, **kwargs):
        result = self.service_service.update_by_id(service_id, kwargs)
        if result == None:
            abort(status.HTTP_404_NOT_FOUND)
        return result, status.HTTP_200_OK

app.add_url_rule(
    '',
    view_func=ServiceResourceList.as_view('ServiceResourceList'),
    methods=['GET', 'POST']
)
app.add_url_rule(
    '/<int:service_id>',
    view_func=ServiceResourceDetail.as_view('ServiceResourceDetail'),
    methods=['GET', 'PUT', 'DELETE', 'PATCH']
)
