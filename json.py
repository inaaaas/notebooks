from alembic import op
import sqlalchemy as sa

revision = 'xxxx'
down_revision = 'prev_revision'

def upgrade():
    op.add_column('laptops', sa.Column('extra_specs', sa.JSON, nullable=True))
    op.execute("CREATE INDEX idx_laptops_extra_specs ON laptops USING GIN (extra_specs jsonb_path_ops)")

def downgrade():
    op.execute("DROP INDEX idx_laptops_extra_specs")
    op.drop_column('laptops', 'extra_specs')
