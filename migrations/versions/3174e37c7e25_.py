"""empty message

Revision ID: 3174e37c7e25
Revises: 55477c6896f2
Create Date: 2022-08-20 20:35:23.836440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3174e37c7e25'
down_revision = '55477c6896f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.drop_column('Artist', 'looking_for_venue')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('looking_for_venue', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('Artist', 'seeking_venue')
    # ### end Alembic commands ###
