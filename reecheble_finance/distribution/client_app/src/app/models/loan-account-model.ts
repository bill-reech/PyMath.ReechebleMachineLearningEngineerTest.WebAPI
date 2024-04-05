export class LoanAccountApiResponseModel {
    data: LoanAccountApiResponseModelData;
    message: string;
    status: [number, string];
}

export class LoanAccountsApiResponseModel {
    data: LoanAccountApiResponseModelData[];
    message: string;
    status: [number, string];
}


export class LoanAccountApiResponseModelData {
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

    static transformToLoanAccountApiResponseModel(loanAccountApiModel: any): any {
        return new LoanAccountApiResponseModelData(
            loanAccountApiModel.id,
            loanAccountApiModel.account_number,
            loanAccountApiModel.first_name,
            loanAccountApiModel.last_name,
            loanAccountApiModel.email_address
        );
    }

    transformToLoanAccountApiRequestModel(): any {
        return {
            id: this.id,
            account_number: this.accountNumber,
            first_name: this.firstName,
            last_name: this.lastName,
            email_address: this.emailAddress
        };
    }

    clone(): LoanAccountApiResponseModelData {
        return new LoanAccountApiResponseModelData(this.id, this.accountNumber, this.firstName, this.lastName, this.emailAddress);
    }
}
