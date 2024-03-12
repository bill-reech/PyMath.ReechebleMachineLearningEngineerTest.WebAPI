"""
Abstract domain parser.
"""

from __future__ import annotations

from functools import wraps
from abc import ABC, abstractmethod
from typing import Union, Mapping, Any, AbstractSet, Dict, Type

from pydantic import BaseModel, Field

from reecheble_finance.domain.enums.multi_attribute_value_enumeration import MultiAttributeValueEnumBase

__all__ = [
    "IntStr",
    "AbstractSetIntStr",
    "DictStrAny",
    "MappingIntStrAny",
    "AbstractDomainParser",
    "BaseDomainParserMixin",
    "Field",
]


IntStr = Union[int, str]
AbstractSetIntStr = AbstractSet[IntStr]
DictStrAny = Dict[str, Any]
MappingIntStrAny = Mapping[IntStr, Any]

basemodel_hidden_attributes = [
    'copy'
]


def hide_attributes_from_lookup(*attrs):
    """
    Class decorator to hide the given attributes from attribute lookup.
    Attributes names defined when calling the wrapper will raise an AttributeError.
    """

    def exclude_attributes(cls):
        original_getattr = cls.__getattribute__

        @wraps(cls)
        def getattribute__(self, name):
            if name in set(attrs):
                raise AttributeError('The thing you are looking for is not here.')
            return original_getattr(self, name)
        cls.__getattribute__ = getattribute__
        return cls
    return exclude_attributes


class AbstractDomainParser(ABC):
    """
    Abstract domain parser for generic models.
    """

    @classmethod
    @abstractmethod
    def from_orm(cls, obj):
        ...

    @abstractmethod
    def dict(self):
        ...

    @abstractmethod
    def json(self):
        ...

    @classmethod
    @abstractmethod
    def parse_obj(cls: Type[BaseDomainParserMixin], obj: Any) -> BaseDomainParserMixin:
        ...

    @classmethod
    def get_multi_attribute_enum_alias(cls, *, alias, enumeration: Type[MultiAttributeValueEnumBase]):
        enum = enumeration.get_by_alias(alias=alias)
        if enum is None:
            raise ValueError(f"Value must be one of {[ele for ele in enumeration.get_all_members_aliases()]}")
        return enum.alias


@hide_attributes_from_lookup(*basemodel_hidden_attributes)
class BaseDomainParserMixin(BaseModel, AbstractDomainParser):
    """
    Abstract mixin class for a domain entity. The class inherits from a pydantic BaseModel which is used
    for parsing data used by the domain models. Any behaviour or attributes of the Basemodel class to be
    used within the domain must be redefined in this base class to avoid broken behaviour.
    """

    @classmethod
    def from_orm(cls, obj) -> BaseDomainParserMixin:
        # Implement own 'from_orm' class method if not using the pydantic BaseModel.
        return super().from_orm(obj)

    def dict(self, *args, **kwargs) -> DictStrAny:
        # Implement own 'dict' instance method if not using the pydantic BaseModel.
        return super().dict(*args, **kwargs)

    def json(self, *args, **kwargs) -> str | bytes:
        # Implement own 'dict' instance method if not using the pydantic BaseModel.
        return super().json(*args, **kwargs)

    @classmethod
    def parse_obj(cls: Type[BaseDomainParserMixin], obj: Any) -> BaseDomainParserMixin:
        # Implement own 'parse_obj' class method if not using the pydantic BaseModel.
        return super().parse_obj(obj=obj)
