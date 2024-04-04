export class RepaymentHistoryApiResponseModel {
    data: RepaymentHistory;
    message: string;
    status: [number, string];
}

export class RepaymentHistoriesApiResponseModel {
    data: RepaymentHistory[];
    message: string;
    status: [number, string];
}

export class RepaymentHistory {
    id?: string;
    month?: number;
    equatedMonthlyInstallment?: number;
    principalPaid?: number;
    interestPaid?: number;
    loanBalance?: number;

    constructor(id?: string, month?: number, equatedMonthlyInstallment?: number, principalPaid?: number, interestPaid?: number, loanBalance?: number) {
        this.id = id;
        this.month = month;
        this.equatedMonthlyInstallment = equatedMonthlyInstallment;
        this.principalPaid = principalPaid;
        this.interestPaid = interestPaid;
        this.loanBalance = loanBalance;
    }

    static transformToRepaymentHistory(repaymentHistoryApiModel: any): any {
        return new RepaymentHistory(
            repaymentHistoryApiModel.id,
            repaymentHistoryApiModel.month,
            repaymentHistoryApiModel.equated_monthly_instalment,
            repaymentHistoryApiModel.principal_paid,
            repaymentHistoryApiModel.interest_paid,
            repaymentHistoryApiModel.loan_balance
        );
    }

    transformToRepaymentHistoryApiModel(): any {
        return {
            id: this.id,
            month: this.month,
            equated_monthly_instalment: this.equatedMonthlyInstallment,
            principal_paid: this.principalPaid,
            interest_paid: this.interestPaid,
            loan_balance: this.loanBalance
        };
    }

    clone(): RepaymentHistory {
        return new RepaymentHistory(this.id, this.month, this.equatedMonthlyInstallment, this.principalPaid, this.interestPaid, this.loanBalance);
    }
}

export class LoanModelApiResponseModel {
    data: LoanModel;
    message: string;
    status: [number, string];
}

export class LoanModelsApiResponseModel {
    data: LoanModel[];
    message: string;
    status: [number, string];
}

export class LoanModel {
    id?: string;
    reference?: string;
    amount?: number;
    interestRate?: number;
    originationDate?: string;
    dueDate?: string;
    duration?: number;
    equatedMonthlyInstallment?: string;
    repaymentHistory?: RepaymentHistory[];

    constructor(id?: string, reference?: string, amount?: number, interestRate?: number, originationDate?: string, dueDate?: string, duration?: number, equatedMonthlyInstallment?: string, repaymentHistory?: RepaymentHistory[]) {
        this.id = id;
        this.reference = reference;
        this.amount = amount;
        this.interestRate = interestRate;
        this.originationDate = originationDate;
        this.dueDate = dueDate;
        this.duration = duration;
        this.equatedMonthlyInstallment = equatedMonthlyInstallment;
        this.repaymentHistory = repaymentHistory;
    }

    static transformToLoan(loanModelApiModel: any): any {
        const repaymentHistoryConverted = loanModelApiModel.repayment_history?.map((repaymentHistory: any) =>
            RepaymentHistory.transformToRepaymentHistory(repaymentHistory));

        return new LoanModel(
            loanModelApiModel.id,
            loanModelApiModel.reference,
            loanModelApiModel.request_amount,
            loanModelApiModel.interest_rate,
            loanModelApiModel.origination_date,
            loanModelApiModel.due_date,
            loanModelApiModel.payment_period_in_months,
            loanModelApiModel.equated_monthly_installment,
            repaymentHistoryConverted
        );
    }

    transformToLoanApiModel(): any {
        const repaymentHistoryConverted = this.repaymentHistory?.map((repaymentHistory) =>
            repaymentHistory.transformToRepaymentHistoryApiModel());

        return {
            id: this.id,
            reference: this.reference,
            request_amount: this.amount,
            interest_rate: this.interestRate,
            origination_date: this.originationDate,
            due_date: this.dueDate,
            payment_period_in_months: this.duration,
            equated_monthly_installment: this.equatedMonthlyInstallment,
            repayment_history: repaymentHistoryConverted
        };
    }

    clone(): LoanModel {
        const repaymentHistoryCloned = this.repaymentHistory?.map((repaymentHistory) =>
            repaymentHistory.clone());

        return new LoanModel(this.id, this.reference, this.amount, this.interestRate, this.originationDate, this.dueDate, this.duration, this.equatedMonthlyInstallment, repaymentHistoryCloned);
    }
}
