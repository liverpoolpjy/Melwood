"""empty message

Revision ID: 2a6fd1a57b9d
Revises: 1daf5f61c0a5
Create Date: 2015-08-29 16:51:21.439098

"""

# revision identifiers, used by Alembic.
revision = '2a6fd1a57b9d'
down_revision = '1daf5f61c0a5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_preview')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_preview', sa.TEXT(), nullable=True))
    ### end Alembic commands ###
