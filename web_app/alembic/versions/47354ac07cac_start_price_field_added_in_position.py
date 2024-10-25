"""start_price field added in position

Revision ID: 47354ac07cac
Revises: b705d1435b64
Create Date: 2024-10-24 14:40:35.737516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47354ac07cac'
down_revision = 'b705d1435b64'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('position', sa.Column('start_price', sa.Float(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('position', 'start_price')
    # ### end Alembic commands ###
