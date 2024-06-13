#!/usr/bin/env python3
"""
Hash password
"""


import bcrypt


def _hash_password(password: str) -> str:
    """
    Hash password
    """
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed
