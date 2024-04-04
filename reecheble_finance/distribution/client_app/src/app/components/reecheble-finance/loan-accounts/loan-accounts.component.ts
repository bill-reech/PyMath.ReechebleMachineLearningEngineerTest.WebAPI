import {Component, OnInit} from '@angular/core';
import {MessageService} from 'primeng/api';
import {Table} from 'primeng/table';
import {LoanAccountApiResponseModel, LoanAccountModel} from "../../../models/loan-account-model";
import {LoanAccountService} from "../../../services/loan-account.service";
import {catchError, first, tap} from "rxjs";
import {Router} from "@angular/router";

@Component({
    templateUrl: './loan-accounts.component.html',
    styleUrls: ['./loan-accounts.component.css'],
    providers: [MessageService]
})
export class LoanAccountsComponent implements OnInit {

    loanAccountDialog: boolean = false;
    deleteLoanAccountDialog: boolean = false;
    deleteLoanAccountsDialog: boolean = false;
    loanAccounts: LoanAccountModel[];
    loanAccount: LoanAccountModel;
    selectedLoanAccounts: LoanAccountModel[];
    submitted: boolean = false;
    loanAccountFields: { field: string, header: string }[];

    constructor(
        private messageService: MessageService,
        private loanAccountService: LoanAccountService,
        private router: Router) {
    }

    ngOnInit() {
        this.loanAccountService.getLoanAccounts().pipe(
            first(),
            tap((accounts: LoanAccountModel[]) => {
                this.loanAccounts = accounts;
            }),
            catchError((error: any) => {
                console.error(error);
                return [];
            })
        ).subscribe();

        this.loanAccountFields = [
            {field: 'accountNumber', header: 'Account Number'},
            {field: 'firstName', header: 'First Name'},
            {field: 'lastName', header: 'Last Name'},
            {field: 'emailAddress', header: 'Email Address'}
        ];
    }

    openNew() {
        this.loanAccount = new LoanAccountModel();
        this.submitted = false;
        this.loanAccountDialog = true;
    }

    deleteSelectedProducts() {
        this.deleteLoanAccountsDialog = true;
    }

    editLoanAccount(loanAccountModel: LoanAccountModel) {
        this.loanAccount = loanAccountModel.clone();
        this.loanAccountDialog = true;
    }

    deleteLoanAccount(loanAccountModel: LoanAccountModel) {
        this.deleteLoanAccountDialog = true;
        this.loanAccount = loanAccountModel.clone();
    }

    confirmDeleteSelected() {
        this.deleteLoanAccountsDialog = false;
        this.loanAccounts = this.loanAccounts.filter(val => !this.selectedLoanAccounts.includes(val));
        this.messageService.add({severity: 'success', summary: 'Successful', detail: 'Products Deleted', life: 3000});
        this.selectedLoanAccounts = [];
    }

    confirmDelete() {
        this.deleteLoanAccountDialog = false;
        this.loanAccounts = this.loanAccounts.filter(val => val.id !== this.loanAccount.id);
        this.messageService.add({severity: 'success', summary: 'Successful', detail: 'Product Deleted', life: 3000});
        this.loanAccount = new LoanAccountModel();
    }

    hideDialog() {
        this.loanAccountDialog = false;
        this.submitted = false;
    }

    addLoanAccount(): void {
        this.submitted = true;

        this.loanAccountService.addLoanAccount(this.loanAccount)
            .subscribe({
                next: (response: LoanAccountApiResponseModel) => {
                    this.loanAccounts.push(response.data);
                    this.messageService.add({
                        severity: 'success',
                        summary: 'Successful',
                        detail: 'LoanModel Account Created',
                        life: 3000
                    });
                    this.loanAccountDialog = false;
                },
                error: error => {
                    console.error('There was an error!', error);
                }
            });

        this.loanAccounts = [...this.loanAccounts]
        this.loanAccountDialog = false;
        this.loanAccount = new LoanAccountModel();
    }

    onGlobalFilter(table: Table, event: Event) {
        table.filterGlobal((event.target as HTMLInputElement).value, 'contains');
    }

    goToDetail(accountNumber: string) {
        this.router.navigateByUrl('/reecheble-finance/loan-account/' + accountNumber);
    }
}
