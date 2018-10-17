"""empty message

Revision ID: 0632cad24de7
Revises: 09895464ee2b
Create Date: 2018-10-16 13:19:47.312091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0632cad24de7'
down_revision = '09895464ee2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('umusaruro', sa.Column('umwakaWisarura', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('umusaruro', 'umwakaWisarura')
    # ### end Alembic commands ###
