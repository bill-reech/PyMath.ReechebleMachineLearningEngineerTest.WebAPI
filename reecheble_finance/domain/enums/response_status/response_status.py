from enum import unique

from reecheble_finance.domain.enums.multi_attribute_value_enumeration import MultiAttributeValueEnumBase

__all__ = [
    "ResponseStatusEnum"
]


@unique
class ResponseStatusEnum(MultiAttributeValueEnumBase):
    success = 1, "success"
    fail = 2, "fail"
    pending = 3, "pending"
