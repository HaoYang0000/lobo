from app.models.BaseModel import BaseMeta, BaseModelExtended, BaseSchema
from marshmallow import fields
from sqlalchemy import Column, UniqueConstraint, text, ForeignKey
from sqlalchemy.dialects import mysql


class UserServiceRelationModel(BaseModelExtended):
    __tablename__ = 'user_service'

    user_id = Column(
        mysql.INTEGER(unsigned=True, display_width=11),
        ForeignKey('users.id', name='fk_user_service_id1')
    )

    service_id = Column(
        mysql.INTEGER(unsigned=True, display_width=11),
        ForeignKey('services.id', name='fk_user_service_id2')
    )
    
    def __repr__(self):
        return (
            "ServiceModel(\
                id='{id}', \
                user_id='{user_id}, \
                service_id='{service_id} \
                ')"
        ).format(
            id=self.id,
            user_id=self.user_id,
            service_id=self.service_id
        )

class UserServiceRelationModelSchema(BaseSchema):
    id = fields.Integer(dump_only=True)

    class Meta(BaseMeta):
        model = UserServiceRelationModel
