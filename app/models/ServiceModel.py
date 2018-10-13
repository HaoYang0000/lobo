from app.models.BaseModel import BaseMeta, BaseModelExtended, BaseSchema
from marshmallow import fields
from sqlalchemy import Column, UniqueConstraint, text
from sqlalchemy.dialects import mysql


class ServiceModel(BaseModelExtended):
    __tablename__ = 'services'

    name = Column(
        mysql.VARCHAR(255),
        nullable=False
    )
    
    def __repr__(self):
        return (
            "ServiceModel(\
                id='{id}', \
                name='{name} \
                ')"
        ).format(
            id=self.id,
            name=self.name
        )

class ServiceModelSchema(BaseSchema):
    id = fields.Integer(dump_only=True)

    class Meta(BaseMeta):
        model = ServiceModel
