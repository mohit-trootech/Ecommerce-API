# Generate Model Field Types For Context Data
from dataclasses import dataclass
from django.core.validators import RegexValidator


@dataclass
class FieldTypes:

    def get_field_types(self, fields: list):
        field_types = {}

        for field in fields:
            field_types[field.name] = field.__class__.__name__

        return field_types

    def get_field_pattern(self, fields: list):
        field_patterns = {}
        for field in fields:
            if field.validators:
                for validator in field.validators:
                    if isinstance(validator, RegexValidator):
                        field_patterns[field.name] = validator.regex.pattern
        return field_patterns


_field_types = FieldTypes()
