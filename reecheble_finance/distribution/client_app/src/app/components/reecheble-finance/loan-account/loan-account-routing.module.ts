import {NgModule} from '@angular/core';
import {RouterModule} from '@angular/router';
import {LoanAccountComponent} from './loan-account.component';
import {LoanAccountResolver} from "./loan-account.resolver";

@NgModule({
    imports: [RouterModule.forChild([
        {path: '', resolve: {accountLoansResolverModel: LoanAccountResolver}, component: LoanAccountComponent}
    ])],
    exports: [RouterModule]
})
export class LoanAccountRoutingModule {
}
