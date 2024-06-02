#!/usr/bin/env python3
"""
filtered_logger.py
"""

from typing import List
import re


def filter_datum(fields: List[int], redaction: str,
                 message: str, separator: str) -> str:
    """ Replacing """
    for f in fields:
        message = re.sub(rf"{f}=(.*?)\{separator}",
                         f'{f}={redaction}{separator}', message)
    return message
