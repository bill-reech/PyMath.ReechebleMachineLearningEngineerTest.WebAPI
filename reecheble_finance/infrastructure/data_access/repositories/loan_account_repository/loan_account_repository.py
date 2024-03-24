import json
from typing import List

from pymongo import MongoClient

from reecheble_finance.domain.models.loan_account import LoanAccount
from reecheble_finance.infrastructure.data_access.repositories.loan_account_repository.abstract_loan_account_repository import (
    AbstractLoanAccountRepository)


class LoanAccountRepository(AbstractLoanAccountRepository):

    def __init__(self, context: MongoClient) -> None:
        super().__init__(context=context)
        self.database = context['ReechebleFinance']
        self.collection = self.database['ReechebleLoanAccount']

    def list(self) -> List[LoanAccount]:
        return [LoanAccount(**account) for account in self.collection.find()]

    def get(self, **filters) -> LoanAccount:
        loan_account = self.collection.find_one({"account_number": str(filters.get("account_number"))})
        return LoanAccount(**loan_account)

    def get_many(self, **filters):
        pass

    def update(self, **kwargs) -> LoanAccount:
        update_loan_account: LoanAccount = kwargs.get("loan_account")
        self.collection.replace_one({
            "account_number": str(update_loan_account.account_number)},
            json.loads(update_loan_account.json()),
            upsert=True)
        return LoanAccount(**update_loan_account.dict())

    def delete(self, id_):
        pass

    def sync(self) -> None:
        pass

    def add(self, *, request: LoanAccount) -> LoanAccount:
        self.collection.insert_one(json.loads(request.json()))
        return self.get(account_number=request.account_number)
