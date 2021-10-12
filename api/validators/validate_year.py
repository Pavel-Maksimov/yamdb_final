from datetime import datetime

from django.core.exceptions import ValidationError


def validate_year(value):
    """
    Validate year in Title model.
    Year should not be earlier than the current.
    """
    if value > datetime.now().year:
        raise ValidationError(
            'Год выхода произведения вне допустимого диапазона')
