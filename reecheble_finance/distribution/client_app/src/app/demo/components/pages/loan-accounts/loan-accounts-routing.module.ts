import {NgModule} from '@angular/core';
import {RouterModule} from '@angular/router';
import {LoanAccountsComponent} from './loan-accounts.component';

@NgModule({
    imports: [RouterModule.forChild([
        {path: '', component: LoanAccountsComponent}
    ])],
    exports: [RouterModule]
})
export class LoanAccountsRoutingModule {
}
