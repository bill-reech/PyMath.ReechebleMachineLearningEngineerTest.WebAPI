import {NgModule} from '@angular/core';
import {RouterModule} from '@angular/router';
import {LoanComponent} from './loan.component';

@NgModule({
    imports: [RouterModule.forChild([
        {path: '', component: LoanComponent}
    ])],
    exports: [RouterModule]
})
export class LoanRoutingModule {
}
