import {NgModule} from '@angular/core';
import {RouterModule} from '@angular/router';
import {LoanAccountComponent} from './loan-account.component';

@NgModule({
    imports: [RouterModule.forChild([
        {path: '', component: LoanAccountComponent}
    ])],
    exports: [RouterModule]
})
export class LoanAccountRoutingModule {
}
