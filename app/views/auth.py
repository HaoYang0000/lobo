import logging
from hashlib import md5

from app.models.UserModel import UserAuthSchema
from app.models.UserModel import UserModel as User
from flask import Blueprint, abort
from flask_api import status
from sqlalchemy import and_
from marshmallow import fields
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from app.services.db.UserController import UserService
from libs.security import create_token

logger = logging.getLogger(__name__)
app = Blueprint(
    'auth',
    __name__,
    url_prefix='/api/auth'
)

@doc(tags=['Users List view'])
class Auth(MethodResource):
    user_service = UserService()
    
    @use_kwargs({'phone': fields.Str(), 'password': fields.Str()})
    @marshal_with(UserAuthSchema, code=status.HTTP_200_OK)
    @doc(description='auth a user')
    def post(self, **kwargs):
        phone = kwargs.get('phone')
        password = kwargs.get('password')

        salt = 'LoboLObOlOBo'
        hashed_password = md5(f"{password}{salt}".encode()).hexdigest()

        result = User.query.filter(
            and_(
                User.phone == phone,
                User.hashed_password == hashed_password)
        ).one_or_none()
        if result is None:
            return abort(status.HTTP_401_UNAUTHORIZED)
        else:
            result.jwt = create_token(user_id=result.id)
            return result, status.HTTP_200_OK

app.add_url_rule(
    '',
    view_func=Auth.as_view('Auth'),
    methods=['POST']
)
