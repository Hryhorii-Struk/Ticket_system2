"""add logging of hours

Revision ID: 70820003badd
Revises: 253ae54f5788
Create Date: 2024-05-26 12:27:42.182034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70820003badd'
down_revision = '253ae54f5788'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('flicket_post', sa.Column('hours', sa.Numeric(), server_default='0', nullable=True))
    op.add_column('flicket_topic', sa.Column('hours', sa.Numeric(), server_default='0', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('flicket_topic', 'hours')
    op.drop_column('flicket_post', 'hours')
    # ### end Alembic commands ###
