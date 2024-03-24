export class LoanAccountApiResponseModel {
    data: LoanAccountModel;
    message: string;
    status: [number, string];
}

export class LoanAccountsApiResponseModel {
    data: LoanAccountModel[];
    message: string;
    status: [number, string];
}


export class LoanAccountModel {
    id?: string;
    accountNumber?: string
    firstName?: string;
    lastName?: string;
    emailAddress?: string;

    constructor(id?: string, accountNumber?: string, firstName?: string, lastName?: string, emailAddress?: string) {
        this.id = id;
        this.accountNumber = accountNumber;
        this.firstName = firstName;
        this.lastName = lastName;
        this.emailAddress = emailAddress;
    }

    static transformToLoanAccount(loanAccountApiModel: any): any {
        return new LoanAccountModel(
            loanAccountApiModel.id,
            loanAccountApiModel.account_number,
            loanAccountApiModel.first_name,
            loanAccountApiModel.last_name,
            loanAccountApiModel.email_address
        );
    }

    transformToLoanAccountApiModel(): any {
        return {
            id: this.id,
            account_number: this.accountNumber,
            first_name: this.firstName,
            last_name: this.lastName,
            email_address: this.emailAddress
        };
    }

    clone(): LoanAccountModel {
        return new LoanAccountModel(this.id, this.accountNumber, this.firstName, this.lastName, this.emailAddress);
    }
}
