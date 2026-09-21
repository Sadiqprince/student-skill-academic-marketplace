"""rename created at column

Revision ID: 4a056840de3e
Revises: 0a76bc460b2a
Create Date: 2026-09-21 13:45:10.999393

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4a056840de3e'
down_revision: Union[str, Sequence[str], None] = '0a76bc460b2a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "users",
        "created-at",
        new_column_name="created_at",
    )


def downgrade() -> None:
    op.alter_column(
        "users",
        "created_at",
        new_column_name="created-at",
    )
