import logging

from flask import Blueprint
from flask_api import status
from sqlalchemy import and_
from marshmallow import fields
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from app.services.twilio import send_sms
from app.models.UserModel import UserModelSchema
from libs.security import get_token_info

logger = logging.getLogger(__name__)
app = Blueprint(
    'notification',
    __name__,
    url_prefix='/api/notification'
)

@doc(tags=['Send user notifications'])
class Notifcation(MethodResource):
    
    @use_kwargs({'to_number': fields.Str(), 'body': fields.Str()})
    @marshal_with(UserModelSchema, code=status.HTTP_200_OK)
    @doc(description='send a txt message to a user')
    def post(self, **kwargs):
        _ = get_token_info()
        number = kwargs.get('to_number', None)
        body = kwargs.get('body', None)

        if number is None or body is None:
            return status.HTTP_412_PRECONDITION_FAILED

        result = send_sms(to_number=number, body=body)
        return result, status.HTTP_200_OK

app.add_url_rule(
    '',
    view_func=Notifcation.as_view('Notifcation'),
    methods=['POST']
)
