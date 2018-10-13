from app.main import db
from marshmallow_sqlalchemy import ModelSchema
from sqlalchemy import Column, text
from sqlalchemy.dialects import mysql

class BaseModel(db.Model):
    __abstract__ = True

    __table_args__ = (
        {
            'mysql_engine': 'InnoDB',
            'mysql_charset': 'utf8mb4',
            'mysql_collate': 'utf8mb4_unicode_ci'
        }
    )

class BaseModelExtended(BaseModel):
    __abstract__ = True

    id = Column(
        mysql.INTEGER(unsigned=True, display_width=11),
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    created_at = Column(
        mysql.TIMESTAMP,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP")
    )
    updated_at = Column(
        mysql.TIMESTAMP,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )

class BaseSchema(ModelSchema):
    def __init__(self, wrap=True, *args, **kwargs):
        self.wrap = wrap
        super().__init__(*args, **kwargs)

class BaseMeta:
    include_fk = True
    dateformat = '%Y-%m-%d %H:%M:%S'
    sqla_session = db.session
    strict = True
