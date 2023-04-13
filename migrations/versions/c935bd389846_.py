"""empty message

Revision ID: c935bd389846
Revises: bcf02e505cfc
Create Date: 2023-03-30 14:57:49.629033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c935bd389846'
down_revision = 'bcf02e505cfc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('work', schema=None) as batch_op:
        batch_op.add_column(sa.Column('emplyed', sa.String(length=40), nullable=True))
        batch_op.drop_column('emplyed_as')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('work', schema=None) as batch_op:
        batch_op.add_column(sa.Column('emplyed_as', sa.VARCHAR(length=40), nullable=True))
        batch_op.drop_column('emplyed')

    # ### end Alembic commands ###