"""added fitness table

Revision ID: 02e0a511c41f
Revises: 2bd252e177b6
Create Date: 2023-07-27 15:10:06.686325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02e0a511c41f'
down_revision = '2bd252e177b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fitness',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('exercise_name', sa.String(length=150), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('duration_minutes', sa.Integer(), nullable=False),
    sa.Column('calories_burned', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('random_joke', sa.String(), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fitness')
    # ### end Alembic commands ###
