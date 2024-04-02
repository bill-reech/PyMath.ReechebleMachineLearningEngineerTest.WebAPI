import {NgModule} from '@angular/core';
import {RouterModule} from '@angular/router';

@NgModule({
    imports: [RouterModule.forChild([
        {
            path: 'loan-account/:account_number',
            data: {breadcrumb: 'Loan'},
            loadChildren: () => import('./loan-account/loan-account.module').then(m => m.LoanAccountModule)
        },
        {path: '**', redirectTo: '/notfound'}
    ])],
    exports: [RouterModule]
})
export class ReechebleFinanceRoutingModule {
}
