"""empty message

Revision ID: b2c11c8328f8
Revises: 9696966017d5
Create Date: 2019-02-13 17:54:45.825099

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b2c11c8328f8'
down_revision = '9696966017d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('members', sa.Column('is_active', sa.Boolean(), nullable=False))
    op.alter_column('members', 'is_delete',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('members', 'is_delete',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    op.drop_column('members', 'is_active')
    # ### end Alembic commands ###
