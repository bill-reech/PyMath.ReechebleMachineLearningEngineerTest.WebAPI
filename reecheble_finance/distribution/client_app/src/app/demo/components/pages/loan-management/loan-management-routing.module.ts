import {NgModule} from '@angular/core';
import {RouterModule} from '@angular/router';
import {LoanManagementComponent} from './loan-management.component';

@NgModule({
    imports: [RouterModule.forChild([
        {path: '', component: LoanManagementComponent}
    ])],
    exports: [RouterModule]
})
export class LoanManagementRoutingModule {
}
