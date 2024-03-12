from enum import Enum

from reecheble_finance.domain.enums.currencies.currency import CurrencyEnum

__all__ = [
    "CurrencyType"
]


CurrencyType = Enum("CurrencyType", {ele: ele for ele in CurrencyEnum.get_all_members_aliases()})
