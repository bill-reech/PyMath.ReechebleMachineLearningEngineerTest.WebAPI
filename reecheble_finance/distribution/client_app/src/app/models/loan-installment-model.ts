export class LoanInstallmentApiResponseModel {
    data: LoanInstallmentApiResponseData;
    message: string;
    status: [number, string];
}

export class LoanInstallmentApiResponseData {
    id: string;
    reference: string;
    outstandingBalance: number;
    interestPaid: number;
    principalPaid: number;
    amountPaid: number;
}

export class LoanInstallmentRequestModel {
    reference: string;
    installmentAmount: number;

    constructor(
        reference?: string,
        installmentAmount?: number) {
        this.reference = reference;
        this.installmentAmount = installmentAmount;
    }

    static transformToLoanInstallmentRequest(loanInstallmentRequest: any): any {
        return new LoanInstallmentRequestModel(
            loanInstallmentRequest.reference,
            loanInstallmentRequest.installment_amount
        );
    }

    transformToLoanInstallmentRequestApiModel(): any {
        return {
            reference: this.reference,
            installment_amount: this.installmentAmount
        };
    }

    static transformApiResponseToLoanInstallmentResponseModel(response: any): LoanInstallmentApiResponseModel {
        if (response.data == null) {
            return {
                data: null,
                message: response.message,
                status: response.status
            };
        }

        const loanInstallmentDetails: LoanInstallmentApiResponseData = {
            id: response.data.id,
            reference: response.data.reference,
            outstandingBalance: response.data.outstanding_balance,
            interestPaid: response.data.interest_paid,
            principalPaid: response.data.principal_paid,
            amountPaid: response.data.amount_paid
        };

        return {
            data: loanInstallmentDetails,
            message: response.message,
            status: response.status
        };
    }

    clone(): LoanInstallmentRequestModel {
        return new LoanInstallmentRequestModel(
            this.reference,
            this.installmentAmount
        )
    }
}
