"""empty message

Revision ID: 82d7d9191824
Revises: 5d39a5bf7344
Create Date: 2024-02-04 21:27:42.686651

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '82d7d9191824'
down_revision: Union[str, None] = '5d39a5bf7344'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
