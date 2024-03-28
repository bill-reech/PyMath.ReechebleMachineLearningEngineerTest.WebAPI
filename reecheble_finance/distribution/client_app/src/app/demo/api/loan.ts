export interface RepaymentHistory {
    id?: string,
    productCode?: string,
    date?: string,
    amount?: number,
    quantity?: number,
    customer?: string,
    status?: string
}

export interface Loan {
    reference?: string;
    amount?: number;
    interest_rate?: number;
    originationDate?: string;
    dueDate?: string;
    duration?: string;
    equatedMonthlyInstallment?: string;
    orders?: RepaymentHistory[];
}
