"""Add tested field to Flashcard

Revision ID: b60dc956c2b4
Revises: 298c26ae795e
Create Date: 2024-07-01 05:23:30.337380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b60dc956c2b4'
down_revision = '298c26ae795e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_flashcard')
    with op.batch_alter_table('flashcard', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tested', sa.Boolean(), nullable=False, server_default=sa.false()))
        batch_op.alter_column('question',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.Text(),
               existing_nullable=False)
        batch_op.alter_column('answer',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.Text(),
               existing_nullable=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_file', sa.String(length=20), nullable=False, server_default='default.jpg'))

    # ### end Alembic commands ###

    # Remove server_default after setting the initial values
    with op.batch_alter_table('flashcard', schema=None) as batch_op:
        batch_op.alter_column('tested', server_default=None)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('image_file')

    with op.batch_alter_table('flashcard', schema=None) as batch_op:
        batch_op.alter_column('answer',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=200),
               existing_nullable=False)
        batch_op.alter_column('question',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=200),
               existing_nullable=False)
        batch_op.drop_column('tested')

    op.create_table('_alembic_tmp_flashcard',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('question', sa.TEXT(), nullable=False),
    sa.Column('answer', sa.TEXT(), nullable=False),
    sa.Column('date_posted', sa.DATETIME(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('tested', sa.BOOLEAN(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###