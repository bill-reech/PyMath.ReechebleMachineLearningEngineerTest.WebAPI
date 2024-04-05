export class LoanResponseModel {
    data: LoanDetails;
    message: string;
    status: [number, string];
}

export class LoanDetails {
    id: string;
    reference: string;
    loanAmount: number;
    loanGranted: boolean;
    equatedMonthlyInstallment: number;
    loanOutstandingBalance: number;
    interestPaid: number;
    principalPaid: number;
    amountPaid: number;
}

export class LoanRequestModel {
    accountNumber: string;
    requestAmount: number;
    interestRate: number;
    paymentPeriodInMonths: number;

    constructor(
        accountNumber?: string,
        requestAmount?: number,
        interestRate?: number,
        paymentPeriodInMonths?: number) {
        this.accountNumber = accountNumber;
        this.requestAmount = requestAmount;
        this.interestRate = interestRate;
        this.paymentPeriodInMonths = paymentPeriodInMonths;
    }

    static transformToLoanRequest(loanRequestModel: any): any {
        return new LoanRequestModel(
            loanRequestModel.accountNumber,
            loanRequestModel.requestAmount,
            loanRequestModel.interestRate,
            loanRequestModel.paymentPeriodInMonths
        );
    }

    transformToLoanRequestApiModel(): any {
        return {
            account_number: this.accountNumber,
            request_amount: this.requestAmount,
            interest_rate: this.interestRate,
            payment_period_in_months: this.paymentPeriodInMonths
        };
    }

    static transformApiResponseToLoanResponseModel(response: any): LoanResponseModel {
        if (response.data == null) {
            return {
                data: null,
                message: response.message,
                status: response.status
            };
        }

        const loanDetails: LoanDetails = {
            id: response.data.id,
            reference: response.data.reference,
            loanAmount: response.data.loan_amount,
            loanGranted: response.data.loan_granted,
            equatedMonthlyInstallment: response.data.equated_monthly_installment,
            loanOutstandingBalance: response.data.loan_outstanding_balance,
            interestPaid: response.data.interest_paid,
            principalPaid: response.data.principal_paid,
            amountPaid: response.data.amount_paid
        };

        return {
            data: loanDetails,
            message: response.message,
            status: response.status
        };
    }

    clone(): LoanRequestModel {
        return new LoanRequestModel(
            this.accountNumber,
            this.requestAmount,
            this.interestRate,
            this.paymentPeriodInMonths
        )
    }
}


