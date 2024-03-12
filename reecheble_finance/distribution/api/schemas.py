from typing import Type

from pydantic import BaseModel

from reecheble_finance.infrastructure.data_access.context import ServiceContext

__all__ = [
    "PathDependency"
]


class PathDependency(BaseModel):
    context: Type[ServiceContext]
