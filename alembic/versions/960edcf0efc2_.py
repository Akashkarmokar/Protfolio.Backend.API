"""empty message

Revision ID: 960edcf0efc2
Revises: 2d9c31e522d4
Create Date: 2024-06-19 17:17:40.358965

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '960edcf0efc2'
down_revision: Union[str, None] = '2d9c31e522d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bios', 'note')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bios', sa.Column('note', sa.TEXT(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###