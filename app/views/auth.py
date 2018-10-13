import logging

import marshmallow
from app.models.UserModel import UserModelSchema
from app.models.UserModel import UserModel as User
from flask import Blueprint, abort, make_response
from flask_api import status
from sqlalchemy import and_
from marshmallow import fields
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from app.services.UserController import UserService
from app.util.db_tool import unrequire

logger = logging.getLogger(__name__)
app = Blueprint(
    'auth',
    __name__,
    url_prefix='/auth'
)

@doc(tags=['Users List view'])
class Auth(MethodResource):
    user_service = UserService()
    
    @use_kwargs({'user_name': fields.Str(), 'password': fields.Str()})
    @marshal_with(UserModelSchema, code=status.HTTP_200_OK)
    @doc(description='auth a user')
    def post(self, **kwargs):
        user_name = kwargs.get('user_name')
        password = kwargs.get('password')

        result = User.query.filter(and_(User.user_name == user_name, User.password == password)).one_or_none()
        if result is None:
            return status.HTTP_404_NOT_FOUND
        return result, status.HTTP_200_OK

app.add_url_rule(
    '',
    view_func=Auth.as_view('Auth'),
    methods=['POST']
)
