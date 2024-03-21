import json

from pymongo import MongoClient

from reecheble_finance.application.sdk.dtos.add_loan_application.add_loan_application_response_dto import (
    AddLoanApplicationResponseDTO
)
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

    def get(self, **filters):
        pass

    def get_many(self, **filters):
        pass

    def update(self, **kwargs):
        pass

    def delete(self, id_):
        pass

    def sync(self) -> None:
        pass

    def add(self, *, request) -> AddLoanApplicationResponseDTO:
        # TODO: There has to be a better way to do serialization for MongoDB. Dates are the ones causing problems here.
        self.collection.insert_one(json.loads(request.json()))
        return request
