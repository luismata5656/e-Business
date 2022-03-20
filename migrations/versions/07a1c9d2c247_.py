"""empty message

Revision ID: 07a1c9d2c247
Revises: 2292ffcc8365
Create Date: 2022-03-07 16:09:31.408238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07a1c9d2c247'
down_revision = '2292ffcc8365'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product_orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('order_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('product_orders_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'orders', ['order_id'], ['id'])
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product_orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('product_orders_user_id_fkey', 'users', ['user_id'], ['id'])
        batch_op.drop_column('order_id')

    # ### end Alembic commands ###