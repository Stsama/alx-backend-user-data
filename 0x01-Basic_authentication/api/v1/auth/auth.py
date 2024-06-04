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
        check = path
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            check += "/"
        if path in excluded_paths or check in excluded_paths:
            return False
        return True

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
