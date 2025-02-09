"""followers

Revision ID: 196aaf6ab98b
Revises: 8f5c469b2025
Create Date: 2020-06-05 22:42:06.135066

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '196aaf6ab98b'
down_revision = '8f5c469b2025'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
