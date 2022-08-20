"""empty message

Revision ID: 8625a691064d
Revises: e9bac264af6a
Create Date: 2022-08-20 19:34:30.058475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8625a691064d'
down_revision = 'e9bac264af6a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.drop_column('Venue', 'looking_for_talent')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('looking_for_talent', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('Venue', 'seeking_talent')
    # ### end Alembic commands ###