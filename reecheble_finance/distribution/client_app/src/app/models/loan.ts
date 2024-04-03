export class RepaymentHistory {
    id?: string;
    month?: number;
    equatedMonthlyInstallment?: number;
    principalPaid?: number;
    interestPaid?: number;
    loanBalance?: number
}

export class Loan {
    id?: string;
    reference?: string;
    amount?: number;
    interestRate?: number;
    originationDate?: string;
    dueDate?: string;
    duration?: string;
    equatedMonthlyInstallment?: string;
    repaymentHistory?: RepaymentHistory[];
}
