"""
Enumeration types bases.
"""

from __future__ import annotations
from typing import Optional, Any
from enum import Enum, unique

__all__ = [
    "MultiAttributeEnumValue",
    "MultiAttributeValueEnumBase",
    "InvalidValueIdentity"
]


class InvalidValueIdentity(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message


class MultiAttributeEnumValue:
    alias: Optional[str] = None
    description: Optional[str] = None
    value_identity: Optional[int] = None

    def __init__(self, value_identity: int, alias: str, description: Optional[str] = None) -> None:
        if not all([isinstance(value_identity, int), isinstance(alias, str)]):
            raise InvalidValueIdentity(
                f"Invalid argument types. Check if parameter types obey the __init__ calling signature."
            )
        self.value_identity = value_identity or self.__class__.value_identity
        self.alias = alias or self.__class__.alias
        self.description = description or self.__class__.description

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.value_identity}, {self.alias}, {self.description})"

    def __hash__(self):
        return hash(f"{self.value_identity}{self.alias}")

    def __eq__(self, other: MultiAttributeEnumValue):
        if isinstance(other, MultiAttributeEnumValue):
            integer_values_are_equal = (self.value_identity == other.value_identity)
            aliases_are_equal = (self.alias == other.alias)
            if all([integer_values_are_equal, aliases_are_equal]):
                return True
            return False


@unique
class MultiAttributeValueEnumBase(MultiAttributeEnumValue, Enum):

    @classmethod
    def get_by_alias(cls, alias: str) -> Optional[MultiAttributeValueEnumBase]:
        return cls.get_value_by_attribute(attr_name='alias', search_attr_value=alias)

    @classmethod
    def get_by_value_identity(cls, integer_value: int) -> Optional[MultiAttributeValueEnumBase]:
        return cls.get_value_by_attribute(attr_name='value_identity', search_attr_value=integer_value)

    @classmethod
    def get_value_by_attribute(
            cls,
            *,
            attr_name: str,
            search_attr_value: Any
    ) -> Optional[MultiAttributeValueEnumBase]:
        if search_attr_value is not None:
            for ele in cls.__members__.values():
                if getattr(ele, attr_name) == search_attr_value:
                    return ele
        return None

    @classmethod
    def get_all_members_aliases(cls):
        return [ele.alias for ele in cls.__members__.values()]
