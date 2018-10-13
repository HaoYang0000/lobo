import logging

import marshmallow
from app.models.UserModel import UserModelSchema
from app.models.UserModel import UserModel as User
from flask import Blueprint, abort, make_response
from flask_api import status
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from app.services.UserController import UserService
from app.util.db_tool import unrequire

logger = logging.getLogger(__name__)
app = Blueprint(
    'users',
    __name__,
    url_prefix='/users'
)
@doc(tags=['Users List view'])
class UserResourceList(MethodResource):
    user_service = UserService()
    @marshal_with(UserModelSchema(many=True), code=status.HTTP_200_OK)
    @doc(description='return all users')
    def get(self, **kwargs):
        result = self.user_service.get_all()
        return result, status.HTTP_200_OK

    @use_kwargs(UserModelSchema().fields)
    @marshal_with(UserModelSchema, code=status.HTTP_201_CREATED)
    @doc(description='Create a new user')
    def post(self, **kwargs):
        new_user = self.user_service.create(**kwargs)
        return new_user, status.HTTP_201_CREATED

@doc(tags=['Users detail view'])
class UserResourceDetail(MethodResource):
    user_service = UserService()
    @marshal_with(UserModelSchema, code=status.HTTP_200_OK)
    @doc(description='return user with id')
    def get(self, user_id, **kwargs):
        result = self.user_service.get_by_id(user_id)
        if result == None:
            abort(status.HTTP_404_NOT_FOUND)
        return result, status.HTTP_200_OK
    
    @marshal_with(None, code=status.HTTP_204_NO_CONTENT)
    @doc(description='delete a user')
    def delete(self, user_id, **kwargs):
        result = self.user_service.delete_by_id(user_id)
        if result == False:
            abort(status.HTTP_404_NOT_FOUND)
        return make_response('', status.HTTP_204_NO_CONTENT)
    
    @use_kwargs(UserModelSchema().fields)
    @marshal_with(UserModelSchema, code=status.HTTP_200_OK)
    @doc(description='update a existing user')
    def put(self, user_id, **kwargs):
        result = self.user_service.update_by_id(user_id, kwargs)
        if result == None:
            abort(status.HTTP_404_NOT_FOUND)
        return result, status.HTTP_200_OK

    @use_kwargs(unrequire(UserModelSchema().fields))
    @doc(description='partially update a recurring frequency')
    @marshal_with(UserModelSchema, code=status.HTTP_200_OK)
    def patch(self, user_id, **kwargs):
        result = self.user_service.update_by_id(user_id, kwargs)
        if result == None:
            abort(status.HTTP_404_NOT_FOUND)
        return result, status.HTTP_200_OK

app.add_url_rule(
    '',
    view_func=UserResourceList.as_view('UserResourceList'),
    methods=['GET', 'POST']
)
app.add_url_rule(
    '/<int:user_id>',
    view_func=UserResourceDetail.as_view('UserResourceDetail'),
    methods=['GET', 'PUT', 'DELETE', 'PATCH']
)
