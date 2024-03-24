import {Component, OnInit} from '@angular/core';
import {Product} from 'src/app/demo/api/product';
import {MessageService} from 'primeng/api';
import {Table} from 'primeng/table';
import {LoanAccountApiResponseModel, LoanAccountModel} from "../../../api/loan-account-model";
import {LoanAccountService} from "../../../service/loan-account.service";
import {first} from "rxjs";

@Component({
    templateUrl: './loan-accounts.component.html',
    providers: [MessageService]
})
export class LoanAccountsComponent implements OnInit {

    loanAccountDialog: boolean = false;

    deleteProductDialog: boolean = false;

    deleteProductsDialog: boolean = false;

    loanAccounts: LoanAccountModel[];
    products: Product[] = [];

    loanAccount: LoanAccountModel;

    selectedProducts: Product[] = [];

    submitted: boolean = false;

    loanAccountFields: any[] = [];

    statuses: any[] = [];

    constructor(private messageService: MessageService, private loanAccountService: LoanAccountService) {
    }

    ngOnInit() {

        this.loanAccountService.getLoanAccounts()
            .pipe(first())
            .subscribe(
                (accounts: LoanAccountModel[]) => {
                    this.loanAccounts = accounts;
                },
                (error: any) => {
                    console.error(error);
                }
            );

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
        this.deleteProductsDialog = true;
    }

    editProduct(product: LoanAccountModel) {
        this.loanAccount = product.clone();
        this.loanAccountDialog = true;
    }

    deleteProduct(product: LoanAccountModel) {
        this.deleteProductDialog = true;
        this.loanAccount = product.clone();
    }

    confirmDeleteSelected() {
        this.deleteProductsDialog = false;
        this.loanAccounts = this.loanAccounts.filter(val => !this.selectedProducts.includes(val));
        this.messageService.add({severity: 'success', summary: 'Successful', detail: 'Products Deleted', life: 3000});
        this.selectedProducts = [];
    }

    confirmDelete() {
        this.deleteProductDialog = false;
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
                        detail: 'Loan Account Created',
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
}
