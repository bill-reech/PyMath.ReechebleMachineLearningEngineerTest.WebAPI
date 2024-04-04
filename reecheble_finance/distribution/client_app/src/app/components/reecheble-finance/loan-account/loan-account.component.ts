import {Component, ElementRef, OnInit, ViewChild} from '@angular/core';
import {ProductService} from 'src/app/demo/service/product.service';
import {Table} from 'primeng/table';
import {ConfirmationService, MessageService} from 'primeng/api';
import {LoanModel} from "../../../models/loan-model";
import {ActivatedRoute} from "@angular/router";

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

    accountId: string;

    @ViewChild('filter') filter!: ElementRef;

    constructor(private productService: ProductService, private route: ActivatedRoute) {
    }

    ngOnInit() {
        this.productService.getProductsWithOrdersSmall().then(data => this.loans = data);
        this.route.params.subscribe(params => {
            this.accountId = params['account_number']
        });
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
