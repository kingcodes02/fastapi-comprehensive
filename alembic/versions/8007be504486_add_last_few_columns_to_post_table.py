"""add last few columns to post table

Revision ID: 8007be504486
Revises: 92485ee01b1b
Create Date: 2022-12-20 14:39:14.021444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8007be504486'
down_revision = '92485ee01b1b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default="TRUE"),)
    op.add_column('posts', sa.Column("created_at", sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
