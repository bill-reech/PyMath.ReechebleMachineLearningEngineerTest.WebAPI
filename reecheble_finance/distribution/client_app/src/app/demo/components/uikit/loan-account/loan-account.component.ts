import {Component, ElementRef, OnInit, ViewChild} from '@angular/core';
import {ProductService} from 'src/app/demo/service/product.service';
import {Table} from 'primeng/table';
import {ConfirmationService, MessageService} from 'primeng/api';
import {Loan} from "../../../api/loan";

interface expandedRows {
    [key: string]: boolean;
}

@Component({
    templateUrl: './loan-account.component.html',
    providers: [MessageService, ConfirmationService]
})
export class LoanAccountComponent implements OnInit {

    statuses: any[] = [];

    loans: Loan[] = [];

    expandedRows: expandedRows = {};

    isExpanded: boolean = false;

    loading: boolean = true;

    @ViewChild('filter') filter!: ElementRef;

    constructor(private productService: ProductService) {
    }

    ngOnInit() {
        this.productService.getProductsWithOrdersSmall().then(data => this.loans = data);
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
