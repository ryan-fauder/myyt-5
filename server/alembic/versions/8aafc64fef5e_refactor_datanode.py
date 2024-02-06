"""refactor datanode

Revision ID: 8aafc64fef5e
Revises: 6be955fea2fd
Create Date: 2024-02-04 21:21:09.614446

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8aafc64fef5e'
down_revision: Union[str, None] = '6be955fea2fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
