"""Init

Revision ID: 569af9f28454
Revises: e68d2680218c
Create Date: 2023-10-17 20:35:24.559516

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '569af9f28454'
down_revision: Union[str, None] = 'e68d2680218c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('enabledUser', sa.Enum('true', 'false', name='enum_user'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'enabledUser')
    # ### end Alembic commands ###
