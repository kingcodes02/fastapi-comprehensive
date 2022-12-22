"""create user table

Revision ID: 9a0deb8e435c
Revises: 5921a0dc5a5d
Create Date: 2022-12-20 13:56:46.065514

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a0deb8e435c'
down_revision = '5921a0dc5a5d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                              server_default=sa.text("now()"), nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email"))
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
