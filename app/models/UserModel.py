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

    hashed_password = Column(
        mysql.TEXT,
        nullable=False
    )

    first_name = Column(
        mysql.VARCHAR(255),
        nullable=True
    )

    last_name = Column(
        mysql.VARCHAR(255),
        nullable=True
    )

    birthday = Column(
        mysql.VARCHAR(255),
        nullable=True
    )

    phone = Column(
        mysql.VARCHAR(255),
        nullable=False
    )

    address = Column(
        mysql.VARCHAR(255),
        nullable=False
    )

    longitude = Column(
        mysql.FLOAT,
        nullable=True
    )

    latitude = Column(
        mysql.FLOAT,
        nullable=True
    )

    language = Column(
        mysql.VARCHAR(255),
        nullable=False
    )

    is_guide = Column(
        mysql.BOOLEAN,
        nullable=False,
        default=False
    )
    
    def __repr__(self):
        return (
            "UserModel(\
                id='{id}', \
                is_guide='{is_guide}', \
                user_name='{user_name}, \
                hashed_password='{hashed_password}, \
                first_name='{first_name}, \
                last_name='{last_name}, \
                phone='{phone}, \
                birthday='{birthday}, \
                address='{address}, \
                longitude='{longitude}, \
                latitude='{latitude}, \
                language='{language}' \
                ')"
        ).format(
            id=self.id,
            user_name=self.user_name,
            hashed_password=self.hashed_password,
            first_name=self.first_name,
            last_name=self.last_name,
            phone=self.phone,
            birthday=self.birthday,
            address=self.address,
            longitude=self.longitude,
            latitude=self.latitude,
            language=self.language,
            is_guide=self.is_guide
        )


class UserModelSchema(BaseSchema):
    id = fields.Integer(dump_only=True)
    distance = fields.Float(dump_only=True)

    class Meta(BaseMeta):
        model = UserModel
        exclude = ['hashed_password']


class UserAuthSchema(BaseSchema):

    class Meta(BaseMeta):
        model = UserModel
        exclude = ['hashed_password']
        dump_only = ['id', 'jwt']

class UserServiceSchema(BaseSchema):
    category = fields.String(dump_only=True)
    name = fields.String(dump_only=True)
    is_expert = fields.Boolean(dump_only=True)

    class Meta(BaseMeta):
        model = UserModel
        exclude = ['hashed_password']

class UserEventSchema(BaseSchema):
    name = fields.String(dump_only=True)
    status = fields.String(dump_only=True)

    class Meta(BaseMeta):
        model = UserModel
        exclude = ['hashed_password']

class UserReviewSchema(BaseSchema):
    rate = fields.Integer(dump_only=True)
    text = fields.String(dump_only=True)

    class Meta(BaseMeta):
        model = UserModel
        exclude = ['hashed_password']

