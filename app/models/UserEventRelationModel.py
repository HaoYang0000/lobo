from app.models.BaseModel import BaseMeta, BaseModelExtended, BaseSchema
from marshmallow import fields
from sqlalchemy import Column, UniqueConstraint, text, ForeignKey
from sqlalchemy.dialects import mysql


class UserEventRelationModel(BaseModelExtended):
    __tablename__ = 'user_event'

    user_id = Column(
        mysql.INTEGER(unsigned=True, display_width=11),
        ForeignKey('users.id', name='fk_user_event_id1')
    )

    event_id = Column(
        mysql.INTEGER(unsigned=True, display_width=11),
        ForeignKey('events.id', name='fk_user_event_id2')
    )
    
    def __repr__(self):
        return (
            "ServiceModel(\
                id='{id}', \
                user_id='{user_id}, \
                event_id='{event_id} \
                ')"
        ).format(
            id=self.id,
            user_id=self.user_id,
            event_id=self.event_id
        )

class UserEventRelationModelSchema(BaseSchema):
    id = fields.Integer(dump_only=True)

    class Meta(BaseMeta):
        model = UserEventRelationModel
