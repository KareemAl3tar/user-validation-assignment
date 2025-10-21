import re
from datetime import datetime


class UserValidation:

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validates if the provided email is in a proper format."""
        if not email or not isinstance(email, str):
            return False

        # Simple regex for standard email structure
        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
        return bool(re.match(pattern, email.strip()))

    @staticmethod
    def validate_username(username: str) -> bool:
        """Validates username (3–20 chars, letters/numbers/underscore only)."""
        if not username or not isinstance(username, str):
            return False

        pattern = r'^[A-Za-z0-9_]{3,20}$'
        return bool(re.match(pattern, username))

    @staticmethod
    def validate_phone_number(phone: str) -> bool:
        """
        Validates Egyptian phone number (starts with 010, 011, 012, 015 or
        2010, 2011, 2012, 2015 — 11 digits total or 12 if it starts with 20).
        """
        if not phone or not isinstance(phone, str):
            return False

        if not phone.isdigit():
            return False

        # Valid Egyptian mobile prefixes
        local_pattern = r'^(010|011|012|015)\d{8}$'
        country_pattern = r'^(2010|2011|2012|2015)\d{8}$'

        return bool(re.match(local_pattern, phone)) or bool(re.match(country_pattern, phone))

    @staticmethod
    def validate_national_id(national_id: str) -> bool:
        """
        Validates Egyptian national ID (14 digits with valid date and governorate code).
        """
        if not national_id or not isinstance(national_id, str):
            return False

        if not national_id.isdigit() or len(national_id) != 14:
            return False

        century = national_id[0]
        if century not in ['2', '3']:
            return False

        year = int(national_id[1:3])
        month = int(national_id[3:5])
        day = int(national_id[5:7])
        governorate = int(national_id[7:9])

        # Validate date part
        try:
            # year is arbitrary century-based, so just check month/day validity
            datetime(2000, month, day)
        except ValueError:
            return False

        # Governorate code between 01–88
        if not (1 <= governorate <= 88):
            return False

        return True
