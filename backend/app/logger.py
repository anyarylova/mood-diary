# backend/app/logger.py

import logging

logger = logging.getLogger("mood_diary")
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# File handler
file_handler = logging.FileHandler("mood_diary.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def redact_sensitive(data: dict) -> dict:
    redacted = data.copy()
    if 'password' in redacted:
        redacted['password'] = '***REDACTED***'
    if 'token' in redacted:
        redacted['token'] = '***REDACTED***'
    return redacted
