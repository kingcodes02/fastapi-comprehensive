"""add content to post table

Revision ID: 5921a0dc5a5d
Revises: 4240c57b5d6c
Create Date: 2022-12-20 13:52:00.339499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5921a0dc5a5d'
down_revision = '4240c57b5d6c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
