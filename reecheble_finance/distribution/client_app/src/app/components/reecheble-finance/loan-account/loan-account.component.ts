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
