import {Component, ElementRef, OnInit, ViewChild} from '@angular/core';
import {Table} from 'primeng/table';
import {ConfirmationService, MessageService} from 'primeng/api';
import {LoanModel} from "../../../models/loan-model";
import {ActivatedRoute} from "@angular/router";
import {LoanService} from "../../../services/loan.service";
import {expandedRowsModel} from "../../../models/common/expanded-rows-model";
import {LoanRequestModel, LoanResponseModel} from "../../../models/loan-request-model";
import {LoanInstallmentApiResponseModel, LoanInstallmentRequestModel} from "../../../models/loan-installment-model";

@Component({
    templateUrl: './loan-account.component.html',
    providers: [MessageService, ConfirmationService]
})
export class LoanAccountComponent implements OnInit {

    loans: LoanModel[] = [];

    expandedRows: expandedRowsModel = {};

    isExpanded: boolean = false;

    loading: boolean = true;

    accountNumber: string;

    submitted: boolean = false;

    loanInstallmentSubmitted: boolean = false;

    loanRequestDialog: boolean = false;

    loanInstallmentRequestDialog: boolean = false;

    loanRequest: LoanRequestModel;

    loanInstallmentRequest: LoanInstallmentRequestModel;


    @ViewChild('filter') filter!: ElementRef;

    constructor(
        private loanService: LoanService,
        private route: ActivatedRoute,
        private messageService: MessageService) {
    }

    ngOnInit() {
        this.route.data.subscribe((data: {
            accountLoansInfo: { accountLoans: LoanModel[], accountNumber: string }
        }) => {
            this.loans = data.accountLoansInfo.accountLoans;
            this.accountNumber = data.accountLoansInfo.accountNumber;
        });
    }

    calculateAverageRequestAmount(): number {
        const totalAmount = this.loans
            .map(loanModel => loanModel.amount || 0)
            .reduce((partialSum, amount) => partialSum + amount, 0);

        return totalAmount / this.loans.length;
    }

    getLatestLoanAmount(): number {
        if (!this.loans.length) return 0; // Array is empty

        const sortedLoans = this.sortAccountLoansByOriginationDate();

        const latestLoanAmount = sortedLoans[0].amount;

        return latestLoanAmount || 0;
    }

    getLatestLoanTerms(): number {
        if (!this.loans.length) return 0; // Array is empty

        const sortedLoans = this.sortAccountLoansByOriginationDate();

        const latestLoanTerms = sortedLoans[0].duration;

        return latestLoanTerms || 0;
    }

    sortAccountLoansByOriginationDate(): LoanModel[] {
        return this.loans.sort(
            (a, b) => new Date(b.originationDate || 0).getTime() - new Date(a.originationDate || 0).getTime()
        );
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
            .map(loanModel => {
                if (loanModel.repaymentHistory.length == 0) return 0;
                return Math.max(...loanModel.repaymentHistory.map(repayment => Number(repayment.month)));
            })
            .reduce((sum, maxMonth) => sum + maxMonth, 0)
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

    addLoanRequest() {
        this.submitted = true;

        this.loanService.addLoanRequest(this.loanRequest)
            .subscribe({
                next: (response: LoanResponseModel) => {
                    if (response.data == null) {
                        this.messageService.add({
                            severity: 'error',
                            summary: 'Error',
                            detail: "Ooopsie, it seems there was a glitch in the matrix.",
                            life: 3000
                        });
                    } else {
                        this.messageService.add({
                            severity: 'success',
                            summary: 'Successful',
                            detail: 'LoanModel Account Created',
                            life: 3000
                        });
                        this.loanRequestDialog = false;
                    }
                },
                error: error => {
                    console.error('There was an error!', error);
                }
            });

        this.loanRequestDialog = false;
    }

    addLoanInstallmentRequest() {
        this.loanInstallmentSubmitted = true;

        this.loanService.addLoanInstallmentRequest(this.loanInstallmentRequest)
            .subscribe({
                next: (response: LoanInstallmentApiResponseModel) => {
                    if (response.data == null) {
                        this.messageService.add({
                            severity: 'error',
                            summary: 'Error',
                            detail: "Ooopsie, it seems there was a glitch in the matrix.",
                            life: 3000
                        });
                    } else {
                        this.messageService.add({
                            severity: 'success',
                            summary: 'Successful',
                            detail: 'LoanModel Account Created',
                            life: 3000
                        });

                        this.loanInstallmentRequestDialog = false;
                    }
                },
                error: error => {
                    console.error('There was an error!', error);
                }
            });

        this.loanInstallmentRequestDialog = false;
    }

    clear(table: Table) {
        table.clear();
        this.filter.nativeElement.value = '';
    }

    hideDialog() {
        this.loanRequestDialog = false;
        this.submitted = false;
    }

    openLoanApplicationRequestDialog(accountNumber: string) {
        this.loanRequest = new LoanRequestModel(accountNumber);
        this.submitted = false;
        this.loanRequestDialog = true;
    }

    openLoanInstallmentPaymentDialog(reference: string, equatedMonthlyInstallment: number) {
        this.loanInstallmentRequest = new LoanInstallmentRequestModel(reference, equatedMonthlyInstallment);
        this.loanInstallmentSubmitted = false;
        this.loanInstallmentRequestDialog = true;
    }
}
