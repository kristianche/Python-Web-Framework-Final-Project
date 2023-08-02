from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator

import re


def check_password_capital_letter(value):
    pattern = r'[A-Z]+'
    if re.search(value, pattern):
        raise ValidationError('Password must contain at least one capital letter!')


def check_password_number(value):
    pattern = r'\d+'
    if re.search(value, pattern):
        raise ValidationError('Password must contain at least one number!')


def check_password_lowercase_letter(value):
    pattern = r'[a-z]'
    if re.search(value, pattern):
        raise ValidationError('Password must contain at least one lowercase letter!')


def check_password_special_symbol(value):
    pattern = r".*[^a-zA-Z0-9].*+"
    if re.search(value, pattern):
        raise ValidationError('Password must contain at least one special symbol!')


class CheckStartsWithCapitalLetter(BaseValidator):
    def __init__(self, text):
        super().__init__(text)
        self.text = text

    def __call__(self, value):
        if not value[0] == value[0].upper():
            raise ValidationError(self.text)
