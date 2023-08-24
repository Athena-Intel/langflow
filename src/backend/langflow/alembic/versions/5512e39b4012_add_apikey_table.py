"""Add ApiKey table

Revision ID: 5512e39b4012
Revises: 0a534bdfd84b
Create Date: 2023-08-23 21:05:51.042203

"""

import contextlib
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = "5512e39b4012"
down_revision: Union[str, None] = "0a534bdfd84b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with contextlib.suppress(sa.exc.OperationalError):
        op.create_table(
            "apikey",
            sa.Column("api_key", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
            sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
            sa.Column("create_at", sa.DateTime(), nullable=False),
            sa.Column("last_used_at", sa.DateTime(), nullable=True),
            sa.Column("id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
            sa.PrimaryKeyConstraint("id"),
            sa.UniqueConstraint("id"),
        )
        op.create_index(op.f("ix_apikey_api_key"), "apikey", ["api_key"], unique=True)

    with contextlib.suppress(sa.exc.OperationalError):
        op.create_table(
            "user",
            sa.Column("id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
            sa.Column("username", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
            sa.Column("password", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
            sa.Column("is_active", sa.Boolean(), nullable=False),
            sa.Column("is_superuser", sa.Boolean(), nullable=False),
            sa.Column("create_at", sa.DateTime(), nullable=False),
            sa.Column("updated_at", sa.DateTime(), nullable=False),
            sa.Column("last_login_at", sa.DateTime(), nullable=True),
            sa.PrimaryKeyConstraint("id"),
            sa.UniqueConstraint("id"),
        )
        op.create_index(op.f("ix_user_username"), "user", ["username"], unique=True)
    with contextlib.suppress(sa.exc.OperationalError):
        op.drop_table("flowstyle")
    with contextlib.suppress(sa.exc.OperationalError):
        op.drop_index("ix_component_frontend_node_id", table_name="component")
        op.drop_index("ix_component_name", table_name="component")
        op.drop_table("component")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "component",
        sa.Column("id", sa.CHAR(length=32), nullable=False),
        sa.Column("frontend_node_id", sa.CHAR(length=32), nullable=False),
        sa.Column("name", sa.VARCHAR(), nullable=False),
        sa.Column("description", sa.VARCHAR(), nullable=True),
        sa.Column("python_code", sa.VARCHAR(), nullable=True),
        sa.Column("return_type", sa.VARCHAR(), nullable=True),
        sa.Column("is_disabled", sa.BOOLEAN(), nullable=False),
        sa.Column("is_read_only", sa.BOOLEAN(), nullable=False),
        sa.Column("create_at", sa.DATETIME(), nullable=False),
        sa.Column("update_at", sa.DATETIME(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_component_name", "component", ["name"], unique=False)
    op.create_index(
        "ix_component_frontend_node_id", "component", ["frontend_node_id"], unique=False
    )
    op.create_table(
        "flowstyle",
        sa.Column("color", sa.VARCHAR(), nullable=False),
        sa.Column("emoji", sa.VARCHAR(), nullable=False),
        sa.Column("flow_id", sa.CHAR(length=32), nullable=True),
        sa.Column("id", sa.CHAR(length=32), nullable=False),
        sa.ForeignKeyConstraint(
            ["flow_id"],
            ["flow.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.drop_index(op.f("ix_user_username"), table_name="user")
    op.drop_table("user")
    op.drop_index(op.f("ix_apikey_api_key"), table_name="apikey")
    op.drop_table("apikey")
    # ### end Alembic commands ###
