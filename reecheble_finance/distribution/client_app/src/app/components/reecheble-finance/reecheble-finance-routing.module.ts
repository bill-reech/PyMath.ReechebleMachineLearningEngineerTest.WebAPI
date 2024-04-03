import {NgModule} from '@angular/core';
import {RouterModule} from '@angular/router';

@NgModule({
    imports: [RouterModule.forChild([
        {
            path: 'loan-account/:account_number',
            data: {breadcrumb: 'Loan'},
            loadChildren: () => import('./loan-account/loan-account.module').then(m => m.LoanAccountModule)
        },
        {
            path: 'loan-accounts',
            loadChildren: () => import('./loan-accounts/loan-accounts.module').then(m => m.LoanAccountsModule)
        },
        {path: '**', redirectTo: '/notfound'}
    ])],
    exports: [RouterModule]
})
export class ReechebleFinanceRoutingModule {
}
