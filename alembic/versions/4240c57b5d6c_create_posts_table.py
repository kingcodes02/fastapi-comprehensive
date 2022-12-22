"""create posts table

Revision ID: 4240c57b5d6c
Revises: 
Create Date: 2022-12-20 13:05:43.431749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4240c57b5d6c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts",
                    sa.Column("id", sa.Integer(),
                              nullable=False, primary_key=True),
                    sa.Column("title", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass
