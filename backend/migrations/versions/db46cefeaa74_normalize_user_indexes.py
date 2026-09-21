"""normalize user indexes

Revision ID: db46cefeaa74
Revises: 4a056840de3e
Create Date: 2026-09-21 13:49:26.101910

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db46cefeaa74'
down_revision: Union[str, Sequence[str], None] = '4a056840de3e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_index("ix-users_email", table_name="users")
    op.drop_index("ix-users_id", table_name="users")

    op.create_index(
        "ix_users_email",
        "users",
        ["email"],
        unique=True,
    )
    op.create_index(
        "ix_users_id",
        "users",
        ["id"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index("ix_users_email", table_name="users")
    op.drop_index("ix_users_id", table_name="users")

    op.create_index(
        "ix-users_email",
        "users",
        ["email"],
        unique=True,
    )
    op.create_index(
        "ix-users_id",
        "users",
        ["id"],
        unique=False,
    )