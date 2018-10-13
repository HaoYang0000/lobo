from app.models.BaseModel import BaseMeta, BaseModelExtended, BaseSchema
from marshmallow import fields
from sqlalchemy import Column, UniqueConstraint, text
from sqlalchemy.dialects import mysql


class UserModel(BaseModelExtended):
    __tablename__ = 'users'

    user_name = Column(
        mysql.VARCHAR(255),
        nullable=False
    )

    password = Column(
        mysql.VARCHAR(255),
        nullable=False
    )

    first_name = Column(
        mysql.VARCHAR(255),
        nullable=False
    )

    last_name = Column(
        mysql.VARCHAR(255),
        nullable=False
    )

    phone = Column(
        mysql.VARCHAR(255),
        nullable=False
    )
    
    def __repr__(self):
        return (
            "UserModel(\
                id='{id}', \
                user_name='{user_name}, \
                password='{password}, \
                first_name='{first_name}, \
                last_name='{last_name}, \
                phone='{phone} \
                ')"
        ).format(
            id=self.id,
            user_name=self.user_name,
            password=self.password,
            first_name=self.first_name,
            last_name=self.last_name,
            phone=self.phone
        )


class UserModelSchema(BaseSchema):
    id = fields.Integer(dump_only=True)

    class Meta(BaseMeta):
        model = UserModel
