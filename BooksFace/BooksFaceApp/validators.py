from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator

import re


def check_password_capital_letter(value):
    pattern = r'[A-Z]'
    if not re.match(value, pattern):
        raise ValidationError('Password must contain at least one capital letter!')


def check_password_number(value):
    pattern = r'[0-9]'
    if not re.match(value, pattern):
        raise ValidationError('Password must contain at least one number!')


def check_password_lowercase_letter(value):
    pattern = r'[a-z]'
    if not re.match(value, pattern):
        raise ValidationError('Password must contain at least one lowercase letter!')


def check_password_special_symbol(value):
    pattern = r'[!@#$%^&*(),.?":{}|<>]'
    if not re.match(value, pattern):
        raise ValidationError('Password must contain at least one special symbol!')


class CheckStartsWithCapitalLetter(BaseValidator):
    def __init__(self, text):
        super().__init__(text)
        self.text = text

    def __call__(self, value):
        pattern = r'[A-Z]'
        if not re.match(value, pattern):
            raise ValidationError(self.text)
