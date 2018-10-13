from app.models.BaseModel import BaseMeta, BaseModelExtended, BaseSchema
from marshmallow import fields
from sqlalchemy import Column, UniqueConstraint, text, ForeignKey
from sqlalchemy.dialects import mysql


class ConversationContentModel(BaseModelExtended):
    __tablename__ = 'conversation_contents'

    content = Column(
        mysql.VARCHAR(255),
        nullable=True
    )

    is_read = Column(
        mysql.BOOLEAN,
        nullable=True,
        default=False
    )
    
    conversation_id = Column(
        mysql.INTEGER(unsigned=True, display_width=11),
        ForeignKey('conversations.id', name='fk_conversation_content_id')
    )

    def __repr__(self):
        return (
            "ConversationContentModel(\
                id='{id}', \
                content='{content}, \
                is_read='{is_read}  \
                ')"
        ).format(
            id=self.id,
            content=self.content,
            is_read=self.is_read
        )

class ConversationContentModelSchema(BaseSchema):
    id = fields.Integer(dump_only=True)

    class Meta(BaseMeta):
        model = ConversationContentModel
