"""empty message

Revision ID: 78ff93a19fbf
Revises: 6602aadecf53
Create Date: 2018-11-13 17:22:54.221786

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '78ff93a19fbf'
down_revision = '6602aadecf53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('unions', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True,
               autoincrement=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('unions', 'id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###
