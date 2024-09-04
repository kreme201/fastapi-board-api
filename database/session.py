from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session

from config import DATABASE_URL
from database.context import get_db_session_context

engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={
        "check_same_thread": False,
    },
)
session_factory = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine,
)
session: Session | scoped_session = scoped_session(
    session_factory,
    scopefunc=get_db_session_context,
)
