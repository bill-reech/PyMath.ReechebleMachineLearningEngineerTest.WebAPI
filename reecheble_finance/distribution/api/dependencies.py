from reecheble_finance.distribution.api.schemas import PathDependency
from reecheble_finance.infrastructure.data_access.database.databases_tools.contexts.context_types import (
    PyMongoDbContext)

__all__ = [
    "router_path_dependency"
]


def router_path_dependency():
    yield PathDependency(context=PyMongoDbContext)
