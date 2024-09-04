from sqlalchemy.ext.declarative import declarative_base

from database.session import session


class CustomBase:
    query = session.query_property()

    def save(self):
        session.add(self)
        return self

    def delete(self):
        session.delete(self)
        return self


Base = declarative_base(cls=CustomBase)
