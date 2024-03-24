export class ApiResponse {
    data: LoanAccount;
    message: string;
    status: [number, string];
}


export class LoanAccount {
    id?: string;
    firstName?: string;
    lastName?: string;
    emailAddress?: string;

    constructor(id?: string, firstName?: string, lastName?: string, emailAddress?: string) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
        this.emailAddress = emailAddress;
    }

    static transformToLoanAccount(loanAccountApiModel: any): any {
        return new LoanAccount(
            loanAccountApiModel.id,
            loanAccountApiModel.first_name,
            loanAccountApiModel.last_name,
            loanAccountApiModel.email_address
        );
    }

    transformToLoanAccountApiModel(): any {
        return {
            id: this.id,
            first_name: this.firstName,
            last_name: this.lastName,
            email_address: this.emailAddress
        };
    }

    clone(): LoanAccount {
        return new LoanAccount(this.id, this.firstName, this.lastName, this.emailAddress);
    }
}
