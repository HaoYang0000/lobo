"""More model changes?

Revision ID: 369cd365eefd
Revises: 5f831dc77284
Create Date: 2018-10-13 22:15:19.134905

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '369cd365eefd'
down_revision = '5f831dc77284'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('conversation_contents', 'is_read',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.BOOLEAN(),
               existing_nullable=True)
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
    op.alter_column('conversation_contents', 'is_read',
               existing_type=sa.BOOLEAN(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    # ### end Alembic commands ###