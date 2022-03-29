"""empty message

Revision ID: 854f720197e6
Revises: 
Create Date: 2022-03-20 21:20:50.792303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '854f720197e6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', sa.String(length=1000), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.drop_column('type')

    # ### end Alembic commands ###