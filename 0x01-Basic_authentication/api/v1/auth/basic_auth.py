#!/usr/bin/env python3
"""
6. Basic auth
"""

from api.v1.auth.auth import Auth
import binascii
import base64


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
