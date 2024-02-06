"""empty message

Revision ID: 5d39a5bf7344
Revises: 8aafc64fef5e
Create Date: 2024-02-04 21:23:36.469809

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5d39a5bf7344'
down_revision: Union[str, None] = '8aafc64fef5e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
