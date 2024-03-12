"""
Enumeration module. This is the parent module for all the enum modules defined within the application.

.. note:: All application enums should be declared withing this module. Anything else is an architecture violation.
"""

from .currencies import *
from .database_types import *
from .logging import *
from .router_tags import *
from .multi_attribute_value_enumeration import *
