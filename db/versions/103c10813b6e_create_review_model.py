"""Create review model

Revision ID: 103c10813b6e
Revises: f682ac0ab9a5
Create Date: 2018-10-13 14:59:05.571748

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '103c10813b6e'
down_revision = 'f682ac0ab9a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', mysql.INTEGER(display_width=11, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('text', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('rate', mysql.INTEGER(), nullable=True),
    sa.Column('event_id', mysql.INTEGER(display_width=11, unsigned=True), nullable=True),
    sa.Column('service_id', mysql.INTEGER(display_width=11, unsigned=True), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], name='fk_review_event_id'),
    sa.ForeignKeyConstraint(['service_id'], ['services.id'], name='fk_review_service_id'),
    sa.PrimaryKeyConstraint('id'),
    mysql_charset='utf8mb4',
    mysql_collate='utf8mb4_unicode_ci',
    mysql_engine='InnoDB'
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
    op.drop_table('reviews')
    # ### end Alembic commands ###
