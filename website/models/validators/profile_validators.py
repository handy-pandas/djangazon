from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_zip(value):
    if len(str(value)) < 5 or len(str(value)) > 5:
        pass
        raise ValidationError(
            _('Zip Code "%(value)s" must be 5 digits'),
            params={'value': value}
        )

def validate_phone(value):
    if len(str(value)) < 10 or len(str(value)) > 10:
        pass
        raise ValidationError(
            _('Phone Number "%(value)s" must be 10 digits'),
            params={'value': value}
        )