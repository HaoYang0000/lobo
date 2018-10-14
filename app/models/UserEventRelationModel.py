from app.models.BaseModel import BaseMeta, BaseModelExtended, BaseSchema
from marshmallow import fields
from sqlalchemy import Column, UniqueConstraint, text, ForeignKey
from sqlalchemy.dialects import mysql


class UserEventRelationModel(BaseModelExtended):
    __tablename__ = 'user_event'

    user_id_one = Column(
        mysql.INTEGER(unsigned=True, display_width=11),
        ForeignKey('users.id', name='fk_user_event_id4')
    )

    user_id_two = Column(
        mysql.INTEGER(unsigned=True, display_width=11),
        ForeignKey('users.id', name='fk_user_event_id3')
    )

    event_id = Column(
        mysql.INTEGER(unsigned=True, display_width=11),
        ForeignKey('events.id', name='fk_user_event_id2')
    )
    
    def __repr__(self):
        return (
            f"ServiceModel("
            f"id='{self.id}', "
            f"user_id_one='{self.user_id_one}', "
            f"user_id_two='{self.user_id_two}', "
            f"event_id='{self.event_id}' "
            f")"
        )


class UserEventRelationModelSchema(BaseSchema):
    id = fields.Integer(dump_only=True)

    class Meta(BaseMeta):
        model = UserEventRelationModel
