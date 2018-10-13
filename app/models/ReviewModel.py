from app.models.BaseModel import BaseMeta, BaseModelExtended, BaseSchema
from marshmallow import fields
from sqlalchemy import Column, UniqueConstraint, text, ForeignKey
from sqlalchemy.dialects import mysql


class ReviewModel(BaseModelExtended):
    __tablename__ = 'reviews'

    text = Column(
        mysql.VARCHAR(255),
        nullable=True
    )

    rate = Column(
        mysql.INTEGER,
        nullable=True
    )
    
    event_id = Column(
        mysql.INTEGER(unsigned=True, display_width=11,nullable=True),
        ForeignKey('events.id', name='fk_review_event_id')
    )

    service_id = Column(
        mysql.INTEGER(unsigned=True, display_width=11,nullable=True),
        ForeignKey('services.id', name='fk_review_service_id')
    )

    def __repr__(self):
        return (
            "EventModel(\
                id='{id}', \
                text='{text}, \
                rate='{rate}, \
                event_id='{event_id}, \
                service_id='{service_id} \
                ')"
        ).format(
            id=self.id,
            text=self.text,
            rate=self.rate,
            event_id=self.event_id,
            service_id=self.service_id
        )

class ReviewModelSchema(BaseSchema):
    id = fields.Integer(dump_only=True)

    class Meta(BaseMeta):
        model = ReviewModel
