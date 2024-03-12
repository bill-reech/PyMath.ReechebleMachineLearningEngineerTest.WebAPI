from enum import unique

from reecheble_finance.domain.enums.multi_attribute_value_enumeration import MultiAttributeValueEnumBase

__all__ = [
    "DatabaseTypesEnum"
]


@unique
class DatabaseTypesEnum(MultiAttributeValueEnumBase):
    mysql = 1, "mysql"
    microsoft_sql_server = 2, "mssql"
