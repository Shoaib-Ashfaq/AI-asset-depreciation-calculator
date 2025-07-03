from backend.database.db import engine, Base
from backend.database.migrations.assets import Assets

# Migrate.
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
