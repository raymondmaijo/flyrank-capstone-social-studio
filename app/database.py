from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import settings

Base = declarative_base()

SQLALCHEMY_DATABASE_URL = settings.database_url

connect_args = {"check_same_thread": False} if SQLALCHEMY_DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    # Import model modules only after Base is defined to avoid circular imports.
    import app.models.post  # noqa: F401
    import app.models.publish_history  # noqa: F401
    import app.models.review_event  # noqa: F401
    import app.models.schedule_slot  # noqa: F401
    import app.models.variant  # noqa: F401
    Base.metadata.create_all(bind=engine)
