import {Component, OnInit} from '@angular/core';
import {Product} from 'src/app/demo/api/product';
import {MessageService} from 'primeng/api';
import {Table} from 'primeng/table';
import {ApiResponse, LoanAccount} from "../../../api/loan-account";
import {LoanAccountService} from "../../../service/loan-account.service";

@Component({
    templateUrl: './loan-accounts.component.html',
    providers: [MessageService]
})
export class LoanAccountsComponent implements OnInit {

    productDialog: boolean = false;

    deleteProductDialog: boolean = false;

    deleteProductsDialog: boolean = false;

    userAccounts: LoanAccount[] = [];
    products: Product[] = [];

    userAccount: LoanAccount;

    selectedProducts: Product[] = [];

    submitted: boolean = false;

    cols: any[] = [];

    statuses: any[] = [];

    constructor(private messageService: MessageService, private loanAccountService: LoanAccountService) {
    }

    ngOnInit() {
        this.cols = [
            {field: 'product', header: 'Product'},
            {field: 'price', header: 'Price'},
            {field: 'category', header: 'Category'},
            {field: 'rating', header: 'Reviews'},
            {field: 'inventoryStatus', header: 'Status'}
        ];
    }

    openNew() {
        this.userAccount = new LoanAccount();
        this.submitted = false;
        this.productDialog = true;
    }

    deleteSelectedProducts() {
        this.deleteProductsDialog = true;
    }

    editProduct(product: LoanAccount) {
        this.userAccount = product.clone();
        this.productDialog = true;
    }

    deleteProduct(product: LoanAccount) {
        this.deleteProductDialog = true;
        this.userAccount = product.clone();
    }

    confirmDeleteSelected() {
        this.deleteProductsDialog = false;
        this.userAccounts = this.userAccounts.filter(val => !this.selectedProducts.includes(val));
        this.messageService.add({severity: 'success', summary: 'Successful', detail: 'Products Deleted', life: 3000});
        this.selectedProducts = [];
    }

    confirmDelete() {
        this.deleteProductDialog = false;
        this.userAccounts = this.userAccounts.filter(val => val.id !== this.userAccount.id);
        this.messageService.add({severity: 'success', summary: 'Successful', detail: 'Product Deleted', life: 3000});
        this.userAccount = new LoanAccount();
    }

    hideDialog() {
        this.productDialog = false;
        this.submitted = false;
    }

    addLoanAccount(): void {
        this.submitted = true;

        this.loanAccountService.addLoanAccount(this.userAccount)
            .subscribe({
                next: (response: ApiResponse) => {
                    this.messageService.add({
                        severity: 'success',
                        summary: 'Successful',
                        detail: 'Loan Account Created',
                        life: 3000
                    });
                    this.productDialog = false;
                },
                error: error => {
                    console.error('There was an error!', error);
                }
            });

        this.productDialog = false;
    }

    onGlobalFilter(table: Table, event: Event) {
        table.filterGlobal((event.target as HTMLInputElement).value, 'contains');
    }
}
