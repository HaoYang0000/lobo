import logging

from flask import Blueprint
from flask_api import status
from sqlalchemy import and_
from marshmallow import fields
from flask_apispec import doc, marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from app.services.twilio import send_sms
from app.models.Conversation import ConversationModel
from app.services.db.ConversationController import ConversationService
from app.models.UserModel import UserModelSchema
from app.models.Conversation import ConversationModelSchema
from app.main import db
from sqlalchemy import or_
from app.util.db_tool import unrequire
from libs.security import get_token_info

logger = logging.getLogger(__name__)
app = Blueprint(
    'conversation',
    __name__,
    url_prefix='/api/conversations'
)

@doc(tags=['Create conversation'])
class ConversationList(MethodResource):
    conversation_service = ConversationService()
    @use_kwargs({**unrequire(ConversationModelSchema().fields)})
    @marshal_with(ConversationModelSchema, code=status.HTTP_201_CREATED)
    @doc(description='generate a conversation from two users')
    def post(self, **kwargs):
        _ = get_token_info()
        self.conversation_service.create(**kwargs)
        return []

@doc(tags=['Grab all the unread conversations belong to a user'])
class ConversationDetail(MethodResource):
    conversation_service = ConversationService()
    @marshal_with(ConversationModelSchema(many=True), code=status.HTTP_200_OK)
    @doc(description='generate a conversation from two users')
    def get(self, user_id, **kwargs):
        _ = get_token_info()
        filter = and_(
            or_(
                ConversationModel.user_id_one == user_id,
                ConversationModel.user_id_two == user_id
            )
        )
        result_set = self.conversation_service.get_multiple(filters=[filter])

        for conversation in result_set:
            self.conversation_service.update_by_id(conversation.id, {'is_read' : True})

        return result_set

app.add_url_rule(
    '',
    view_func=ConversationList.as_view('ConversationList'),
    methods=['POST']
)
app.add_url_rule(
    '/<int:user_id>',
    view_func=ConversationDetail.as_view('ConversationDetail'),
    methods=['GET']
)


