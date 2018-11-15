"""empty message

Revision ID: 629271110dca
Revises: 83d5daa09f34
Create Date: 2018-11-13 16:53:29.308092

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '629271110dca'
down_revision = '83d5daa09f34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ibihano',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Igihano', sa.String(length=200), nullable=True),
    sa.Column('IgihanoAmount', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(length=200), nullable=True),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('done_date', sa.DateTime(), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ibindi',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ImifukaQuantity', sa.Integer(), nullable=True),
    sa.Column('ImifukaAmount', sa.Integer(), nullable=True),
    sa.Column('MituelleAmount', sa.Integer(), nullable=True),
    sa.Column('UmuceriGrade', sa.Integer(), nullable=True),
    sa.Column('UmuceriQuantity', sa.Integer(), nullable=True),
    sa.Column('UmuceriAmountGrade', sa.Integer(), nullable=True),
    sa.Column('Avence', sa.Integer(), nullable=True),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('done_date', sa.DateTime(), nullable=True),
    sa.Column('department_id', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.email'], ),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
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
    op.drop_table('ibindi')
    op.drop_table('ibihano')
    # ### end Alembic commands ###
