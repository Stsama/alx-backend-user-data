#!/usr/bin/env python3
"""
Auth class
"""


from flask import request
from typing import List, TypeVar
from api.v1.views import User


class Auth:
    """
    class to manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        verify if the authorization is reqquired
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        verify if the authorization is present
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        verified who is the current_user
        """
        return None
