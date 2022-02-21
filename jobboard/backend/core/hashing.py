from pydoc import plain
from click import pass_context
from passlib.context import CryptContext

pass_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher():
    """
    Hasher Class Object with direct static method
    These static methods can be invoked directy without initialization of the Hasher class

    example usage in python terminal:

    >> Hasher.get_password_hash('Hello')
    $2b$12$1RM4ZdEDs5Hq.XtoanGWheKuVxmcp4Ttr1GgJks9q09eRSSkWG/E2

    >> Hasher.verify_password('Hello', '$2b$12$1RM4ZdEDs5Hq.XtoanGWheKuVxmcp4Ttr1GgJks9q09eRSSkWG/E2')
    True
    """

    @staticmethod
    def get_password_hash(plain_password):
        return pass_context.hash(plain_password)

    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pass_context.verify(plain_password, hashed_password)
