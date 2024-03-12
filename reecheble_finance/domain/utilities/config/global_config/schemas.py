from typing import Union, Optional

from pydantic import validator

from reecheble_finance.domain.enums.database_types.database_types import DatabaseTypesEnum
from reecheble_finance.domain.abstract_domain.abstract_domain_parser_mixin import BaseDomainParserMixin

__all__ = [
    "DatabaseDetails",
    "Databases",
    "DatabaseType",
    "GlobalConfiguration"
]


class DatabaseDetails(BaseDomainParserMixin):
    server_name: Optional[str]
    database_name: Optional[str]
    database_user: Optional[str]
    database_user_password: Optional[str]
    server_port: Union[str, None]

    class Config:
        fields = {
            "server_name": "serverName",
            "database_name": "databaseName",
            "database_user": "databaseUser",
            "database_user_password": "databaseUserPassword",
            "server_port": "serverPort"
        }

    @validator("server_port", pre=True, always=True)
    def validate_port(cls, value):
        if isinstance(value, str):
            return None
        return value


class Databases(BaseDomainParserMixin):
    microsoft_sql_server: DatabaseDetails = DatabaseDetails()
    mysql_server: DatabaseDetails = DatabaseDetails()


class DatabaseType(BaseDomainParserMixin):
    name: DatabaseTypesEnum

    @validator("name", pre=True, always=True)
    def validate_default_database(cls, value):
        if isinstance(value, str):
            return DatabaseTypesEnum.get_by_alias(alias=value)
        raise ValueError(f"Value must be one of {[ele for ele in DatabaseType.get_all_members_aliases()]}")


class GlobalConfiguration(BaseDomainParserMixin):
    databases: Databases = Databases()
    default_database: DatabaseType
