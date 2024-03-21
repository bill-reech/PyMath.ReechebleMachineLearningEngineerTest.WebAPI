import json

from pymongo import MongoClient

from reecheble_finance.domain.models.loan_account import LoanAccount
from reecheble_finance.infrastructure.data_access.repositories.loan_account_repository.abstract_loan_account_repository import (
    AbstractLoanAccountRepository)


class LoanAccountRepository(AbstractLoanAccountRepository):

    def __init__(self, context: MongoClient) -> None:
        super().__init__(context=context)
        self.database = context['ReechebleFinance']
        self.collection = self.database['ReechebleLoanAccount']

    def list(self):
        pass

    def get(self, **filters) -> LoanAccount:
        loan_account = self.collection.find_one({"id": str(filters.get("id"))})
        return LoanAccount(**loan_account)

    def get_many(self, **filters):
        pass

    def update(self, **kwargs) -> LoanAccount:
        update_loan_account: LoanAccount = kwargs.get("loan_account")
        self.collection.replace_one({"id": str(kwargs.get("id"))}, json.loads(update_loan_account.json()), upsert=True)
        return LoanAccount(**update_loan_account.dict())

    def delete(self, id_):
        pass

    def sync(self) -> None:
        pass

    def add(self, *, request: LoanAccount) -> LoanAccount:
        self.collection.insert_one(json.loads(request.json()))
        return self.get(id=request.id)
