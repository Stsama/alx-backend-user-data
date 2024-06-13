#!/usr/bin/env python3
"""
Hash password
"""


import bcrypt
from db import DB
from user import User
from typing import TypeVar
from db import DB
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """
    Hash password
    """
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
