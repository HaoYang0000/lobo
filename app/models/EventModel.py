from app.models.BaseModel import BaseMeta, BaseModelExtended, BaseSchema
from marshmallow import fields
from sqlalchemy import Column, UniqueConstraint, text
from sqlalchemy.dialects import mysql


class EventModel(BaseModelExtended):
    __tablename__ = 'events'

    name = Column(
        mysql.VARCHAR(255),
        nullable=False
    )

    status = Column(
        mysql.VARCHAR(255),
        nullable=False
    )

    date = Column(
        mysql.TIMESTAMP,
        nullable=False
    )
    
    def __repr__(self):
        return (
            "EventModel(\
                id='{id}', \
                name='{name}, \
                status='{status}, \
                date='{date} \
                ')"
        ).format(
            id=self.id,
            name=self.name,
            status=self.status,
            date=self.date
        )

class EventModelSchema(BaseSchema):
    id = fields.Integer(dump_only=True)

    class Meta(BaseMeta):
        model = EventModel
