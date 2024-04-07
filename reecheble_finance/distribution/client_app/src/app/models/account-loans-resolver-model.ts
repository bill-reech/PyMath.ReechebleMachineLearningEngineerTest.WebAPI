import {LoanModel} from "./loan-model";

export class AccountLoansResolverModel {
    accountLoans: LoanModel[];
    accountNumber: string

    constructor(accountLoans?: LoanModel[], accountNumber?: string) {
        this.accountLoans = accountLoans;
        this.accountNumber = accountNumber;
    }
}
