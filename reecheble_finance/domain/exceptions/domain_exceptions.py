from __future__ import annotations

__all__ = [
    "LoanRequestDomainException"
]


class LoanRequestDomainException(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
