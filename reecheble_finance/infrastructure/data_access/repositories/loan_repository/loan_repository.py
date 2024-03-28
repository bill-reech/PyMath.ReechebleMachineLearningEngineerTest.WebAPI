import json

from pymongo import MongoClient

from reecheble_finance.domain.models.loan_request import LoanRequest
from reecheble_finance.infrastructure.data_access.repositories.loan_repository.abstract_loan_repository import (
    AbstractLoanRepository
)


class LoanRepository(AbstractLoanRepository):

    def __init__(self, context: MongoClient) -> None:
        super().__init__(context=context)
        self.database = context['ReechebleFinance']
        self.collection = self.database['ReechebleLoan']

    def list(self):
        pass

    def get(self, **filters) -> LoanRequest:
        loan_request = self.collection.find_one({"reference": str(filters.get("reference"))})
        return LoanRequest(**loan_request)

    def get_many(self, **filters):
        pass

    def update(self, **kwargs) -> LoanRequest:
        update_loan_request: LoanRequest = kwargs.get("loan_request")
        self.collection.replace_one({"reference": str(update_loan_request.reference)},
                                    json.loads(update_loan_request.json()),
                                    upsert=True)
        return LoanRequest(**update_loan_request.dict())

    def delete(self, id_):
        pass

    def sync(self) -> None:
        pass

    def add(self, *, request: LoanRequest) -> LoanRequest:
        self.collection.insert_one(json.loads(request.json()))
        return self.get(reference=request.reference)
