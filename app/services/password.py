from passlib.context import CryptContext

password = CryptContext(schemes=["bcrypt"], deprecated="auto")
