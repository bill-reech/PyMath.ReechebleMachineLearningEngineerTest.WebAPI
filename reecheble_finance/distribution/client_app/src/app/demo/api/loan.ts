export interface RepaymentHistory {
    id?: string,
    month?: number,
    equatedMonthlyInstallment?: number,
    principalPaid?: number,
    interestPaid?: number,
    loanBalance?: number
}

export interface Loan {
    id?: string,
    reference?: string;
    amount?: number;
    interest_rate?: number;
    originationDate?: string;
    dueDate?: string;
    duration?: string;
    equatedMonthlyInstallment?: string;
    repaymentHistory?: RepaymentHistory[];
}
