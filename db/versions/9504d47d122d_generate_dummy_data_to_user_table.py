"""generate dummy data to user table

Revision ID: 9504d47d122d
Revises: a7748fca292a
Create Date: 2018-10-13 15:05:13.744879

"""
import re

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy.dialects import mysql
from sqlalchemy import String, Integer, Date, Float, Boolean
from faker import Faker
import random


# revision identifiers, used by Alembic.
revision = '9504d47d122d'
down_revision = 'a7748fca292a'
branch_labels = None
depends_on = None

def upgrade():
    fake = Faker()

    language_list = [
        "English",
        "French",
        "Finnish",
        "German",
        "Spanish",
        "Arabic",
        "Chinese",
        "Russian"
    ]

    # ### commands auto generated by Alembic - please adjust! ###
    my_table = table('users',
        column('id', Integer),
        column('user_name', String),
        column('password', String),
        column('first_name', String),
        column('last_name', String),
        column('birthday', String),
        column('phone', String),
        column('address', String),
        column('longitude', Float),
        column('latitude', Float),
        column('language', String),
        column('is_guide', Boolean)
    )
    # ### commands auto generated by Alembic - please adjust! ### 

    user_list = []
    for x in range(48):
        if x == 0:
            first_name = fake.first_name_male()
            user_list.append({
                'id' : int(x+1),
                'user_name': first_name,
                'password': fake.password(length=10),
                'first_name': first_name,
                'last_name': fake.last_name_male(),
                'birthday': fake.date_of_birth(),
                'phone': re.sub('[^0-9]', '', fake.phone_number()),
                'address': fake.address(),
                'latitude': fake.latitude(),
                'longitude': fake.longitude(),
                'language': random.choice(language_list),
                'is_guide': False
            })
        elif x == 1:
            first_name = fake.first_name_male()
            user_list.append({
                'id' : int(x+1),
                'user_name': first_name,
                'password': fake.password(length=10),
                'first_name': first_name,
                'last_name': fake.last_name_male(),
                'birthday': fake.date_of_birth(),
                'phone': fake.phone_number(),
                'address': fake.address(),
                'latitude': fake.latitude(),
                'longitude': fake.longitude(),
                'language': random.choice(language_list),
                'is_guide': True
            })
        else:
            first_name = fake.first_name_female()
            user_list.append({
                'id' : int(x+1),
                'user_name': first_name,
                'password': fake.password(length=10),
                'first_name': first_name,
                'last_name': fake.last_name_female(),
                'birthday': fake.date_of_birth(),
                'phone': fake.phone_number(),
                'address': fake.address(),
                'latitude': fake.latitude(),
                'longitude': fake.longitude(),
                'language': random.choice(language_list),
                'is_guide': True
            })
        # test user


    op.bulk_insert(my_table,
        user_list
    )


    op.alter_column('users', 'is_guide',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.BOOLEAN(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'is_guide',
               existing_type=sa.BOOLEAN(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False)
    # ### end Alembic commands ###
