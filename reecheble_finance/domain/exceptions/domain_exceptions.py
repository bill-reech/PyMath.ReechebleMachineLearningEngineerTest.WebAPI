from __future__ import annotations

__all__ = [
    "InvalidLoanRequestDomainException"
]


class InvalidLoanRequestDomainException(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
