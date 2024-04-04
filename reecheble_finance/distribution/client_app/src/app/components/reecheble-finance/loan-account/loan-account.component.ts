import {Component, ElementRef, OnInit, ViewChild} from '@angular/core';
import {Table} from 'primeng/table';
import {ConfirmationService, MessageService} from 'primeng/api';
import {LoanModel} from "../../../models/loan-model";
import {ActivatedRoute} from "@angular/router";
import {LoanService} from "../../../services/loan.service";
import {catchError, first, tap} from "rxjs";

interface expandedRows {
    [key: string]: boolean;
}

@Component({
    templateUrl: './loan-account.component.html',
    providers: [MessageService, ConfirmationService]
})
export class LoanAccountComponent implements OnInit {

    loans: LoanModel[];

    expandedRows: expandedRows = {};

    isExpanded: boolean = false;

    loading: boolean = true;

    accountNumber: string;

    @ViewChild('filter') filter!: ElementRef;

    constructor(private loanService: LoanService, private route: ActivatedRoute) {
    }

    ngOnInit() {
        this.setAccountNumber();
        this.getAllAccountLoans(this.accountNumber);
    }

    setAccountNumber() {
        this.route.params.subscribe(params => {
            this.accountNumber = params['account_number']
        });
    }

    getAllAccountLoans(accountNumber: string) {
        this.loanService.getAccountLoans(accountNumber).pipe(
            first(),
            tap((loans: LoanModel[]) => {
                this.loans = loans;
            }),
            catchError((error: any) => {
                console.error(error);
                return [];
            })
        ).subscribe();
    }

    calculateAverageRequestAmount(): number {
        const totalAmount = this.loans
            .map(loanModel => loanModel.amount || 0)
            .reduce((partialSum, amount) => partialSum + amount, 0);

        return totalAmount / this.loans.length;
    }

    getLatestLoanAmount(): number {
        if (!this.loans.length) return 0; // Array is empty

        const sortedLoans = this.loans.sort(
            (a, b) => new Date(b.originationDate || 0).getTime() - new Date(a.originationDate || 0).getTime()
        );

        const latestLoanAmount = sortedLoans[0].amount;

        return latestLoanAmount || 0;
    }

    getLatestLoanTerms(): number {
        if (!this.loans.length) return 0; // Array is empty

        const sortedLoans = this.loans.sort(
            (a, b) => new Date(b.originationDate || 0).getTime() - new Date(a.originationDate || 0).getTime()
        );

        const latestLoanTerms = sortedLoans[0].duration;

        return latestLoanTerms || 0;
    }

    getNumberOfLoans(): number {
        return this.loans.length;
    }

    calculateAverageInterestRate(): number {
        if (!this.loans.length) return 0; // Array is empty

        const totalInterestRate = this.loans
            .map(loanModel => loanModel.interestRate || 0)
            .reduce((partialSum, interestRate) => partialSum + interestRate, 0);

        return totalInterestRate / this.loans.length;
    }

    calculateAverageDuration(): number {
        if (!this.loans.length) return 0; // Array is empty

        const totalDuration = this.loans
            .map(loanModel => Number(loanModel.duration) || 0)
            .reduce((partialSum, duration) => partialSum + duration, 0);

        return totalDuration / this.loans.length;
    }

    calculateTotalPayments(): number {
        if (!this.loans.length) return 0; // Array is empty

        return this.loans
            .map(loanModel => loanModel.repaymentHistory.length)
            .reduce((partialSum, numPayments) => partialSum + numPayments, 0);
    }

    shouldDisplayInstallmentButton(loanModel: LoanModel): boolean {
        if (!loanModel.repaymentHistory.length) return true; // RepaymentHistory is empty

        let runningBalance = loanModel.repaymentHistory[loanModel.repaymentHistory.length - 1].loanBalance
        return runningBalance > 0;

    }

    expandAll() {
        if (!this.isExpanded) {
            this.loans.forEach(loan => loan && loan.reference ? this.expandedRows[loan.reference] = true : '');

        } else {
            this.expandedRows = {};
        }
        this.isExpanded = !this.isExpanded;
    }

    clear(table: Table) {
        table.clear();
        this.filter.nativeElement.value = '';
    }

}
