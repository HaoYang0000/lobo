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
    
    user_id = Column(
        mysql.INTEGER(unsigned=True, display_width=11),
        ForeignKey('users.id', name='fk_review_user_id')
    )

    def __repr__(self):
        return (
            "EventModel(\
                id='{id}', \
                text='{text}, \
                rate='{rate}, \
                user_id='{event_id} \
                ')"
        ).format(
            id=self.id,
            text=self.text,
            rate=self.rate,
            user_id=self.user_id
        )

class ReviewModelSchema(BaseSchema):
    id = fields.Integer(dump_only=True)

    class Meta(BaseMeta):
        model = ReviewModel
