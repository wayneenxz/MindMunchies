"""Add correct field to Flashcard

Revision ID: e7fdb0770271
Revises: b60dc956c2b4
Create Date: 2024-07-01 05:35:46.088645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7fdb0770271'
down_revision = 'b60dc956c2b4'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('flashcard', schema=None) as batch_op:
        batch_op.add_column(sa.Column('correct', sa.Boolean(), nullable=False, server_default=sa.sql.expression.false()))

    # ### end Alembic commands ###


def downgrade():
    with op.batch_alter_table('flashcard', schema=None) as batch_op:
        batch_op.drop_column('correct')

    # ### end Alembic commands ###
