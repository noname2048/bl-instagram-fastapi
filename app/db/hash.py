from passlib.context import CryptContext

context = CryptContext(schemes="bcrypt", deprecated="auto")


class Hash:
    def bcrypt(password: str):
        return context.hash(password)

    def verify(plain_password, hashed_password):
        return context.verify(plain_password, hashed_password)
