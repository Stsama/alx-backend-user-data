#!/usr/bin/env python3
"""
6. Basic auth
"""

from api.v1.auth.auth import Auth
import binascii
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        returns the Base64 part of the Authorization header
        """
        if (authorization_header is None or
                not isinstance(authorization_header, str) or
                not authorization_header.startswith("Basic ")):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        returns the decoded value of a Base64 string
        """
        base_first = base64_authorization_header
        if base_first and isinstance(base_first, str):
            try:
                encode = base_first.encode('utf-8')
                base = base64.b64decode(encode)
                return base.decode('utf-8')
            except binascii.Error:
                return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        returns the user email and password from the Base64 decoded value
        """
        if (decoded_base64_authorization_header is None or
                not isinstance(decoded_base64_authorization_header, str) or
                ":" not in decoded_base64_authorization_header):
            return (None, None)
        string = str(decoded_base64_authorization_header)
        to_return = string.split(":")
        return (to_return[0], to_return[1])

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        returns the User instance based on his email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users_found = User.search({"email": user_email})
        except Exception:
            return None
        for user in users_found:
            if user.is_valid_password(user_pwd):
                return user

    def current_user(self, request=None) -> TypeVar('User'):
        """
        overloads Auth and retrieves the User instance for a request
        """
        auth_value = self.authorization_header(request)
        if not auth_value:
            return None
        auth_base_part = self.extract_base64_authorization_header(auth_value)
        if not auth_base_part:
            return None
        decoded_auth = self.decode_base64_authorization_header(auth_base_part)
        if not decoded_auth:
            return None
        email, pwd = self.extract_user_credentials(decoded_auth)
        if not email or not pwd:
            return None
        user_object = self.user_object_from_credentials(email, pwd)
        return user
