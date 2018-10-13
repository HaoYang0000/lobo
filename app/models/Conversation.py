from app.models.BaseModel import BaseMeta, BaseModelExtended, BaseSchema
from marshmallow import fields
from sqlalchemy import Column, UniqueConstraint, text, ForeignKey
from sqlalchemy.dialects import mysql


class ConversationModel(BaseModelExtended):
    __tablename__ = 'conversations'
    
    user_id_one = Column(
        mysql.INTEGER(unsigned=True, display_width=11),
        ForeignKey('users.id', name='fk_conversation_user_id_one')
    )

    user_id_two = Column(
        mysql.INTEGER(unsigned=True, display_width=11),
        ForeignKey('users.id', name='fk_conversation_user_id_two')
    )

    def __repr__(self):
        return (
            "ConversationModel(\
                id='{id}', \
                user_id_one='{user_id_one}, \
                user_id_two='{user_id_two} \
                ')"
        ).format(
            id=self.id,
            user_id_one=self.user_id_one,
            user_id_two=self.user_id_two
        )

class ConversationModelSchema(BaseSchema):
    id = fields.Integer(dump_only=True)

    class Meta(BaseMeta):
        model = ConversationModel
