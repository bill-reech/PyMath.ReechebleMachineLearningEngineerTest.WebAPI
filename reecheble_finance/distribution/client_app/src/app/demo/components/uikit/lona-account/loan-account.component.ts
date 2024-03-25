import {Component, ElementRef, OnInit, ViewChild} from '@angular/core';
import {Product} from 'src/app/demo/api/product';
import {ProductService} from 'src/app/demo/service/product.service';
import {Table} from 'primeng/table';
import {ConfirmationService, MessageService} from 'primeng/api';

interface expandedRows {
    [key: string]: boolean;
}

@Component({
    templateUrl: './loan-account.component.html',
    providers: [MessageService, ConfirmationService]
})
export class LoanAccountComponent implements OnInit {

    statuses: any[] = [];

    products: Product[] = [];

    expandedRows: expandedRows = {};

    isExpanded: boolean = false;

    loading: boolean = true;

    @ViewChild('filter') filter!: ElementRef;

    constructor(private productService: ProductService) {
    }

    ngOnInit() {
        this.productService.getProductsWithOrdersSmall().then(data => this.products = data);
    }

    expandAll() {
        if (!this.isExpanded) {
            this.products.forEach(product => product && product.name ? this.expandedRows[product.name] = true : '');

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
