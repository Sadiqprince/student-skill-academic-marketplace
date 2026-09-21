"""make password hash nullable

Revision ID: 0a76bc460b2a
Revises: 19844f6836d3
Create Date: 2026-09-21 13:12:58.196681

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0a76bc460b2a'
down_revision: Union[str, Sequence[str], None] = '19844f6836d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "users",
        "password_hash",
        existing_type=sa.VARCHAR(length=255),
        nullable=True,
    )


def downgrade() -> None:
    op.alter_column(
        "users",
        "password_hash",
        existing_type=sa.VARCHAR(length=255),
        nullable=False,
    )
