from functools import wraps

from database.session import session


def transactional(func):
    @wraps(func)
    def _transactional(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e

        return result

    return _transactional
