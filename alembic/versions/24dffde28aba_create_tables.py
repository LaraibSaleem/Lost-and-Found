"""create tables

Revision ID: 24dffde28aba
Revises: 
Create Date: 2021-04-08 13:08:07.999222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24dffde28aba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'User',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('uname', sa.String(255), nullable=False),
        sa.Column('pw', sa.Unicode(255)),
        )

    op.create_table(
        'Item',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('location', sa.String(255), nullable=True),
        sa.Column('description', sa.String(255), nullable=True),
        sa.Column('date', sa.Date(), nullable=True),
        )


def downgrade():
    op.drop_table('User')
    op.drop_table('Item')
