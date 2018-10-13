import logging

import marshmallow
from app.models.UserModel import UserModelSchema
from app.models.UserModel import UserModel as User
# from app.services.frequencies import FrequencyService
from flask import Blueprint, abort, make_response
from flask_api import status
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource

logger = logging.getLogger(__name__)
app = Blueprint(
    'users',
    __name__,
    url_prefix='/users'
)

@doc(tags=['Users List view'])
class UserResourceList(MethodResource):

    @marshal_with(UserModelSchema(many=True), code=status.HTTP_200_OK)
    @doc(description='return all users')
    def get(self, **kwargs):
        result = User.query.all()
        print (result)
        return result, status.HTTP_200_OK

@doc(tags=['Users detail view'])
class UserResourceDetail(MethodResource):
    pass

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
