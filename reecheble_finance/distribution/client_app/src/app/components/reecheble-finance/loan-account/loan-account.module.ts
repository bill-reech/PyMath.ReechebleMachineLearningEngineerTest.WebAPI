import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {FormsModule} from '@angular/forms';
import {LoanAccountComponent} from './loan-account.component';
import {LoanAccountRoutingModule} from './loan-account-routing.module';
import {TableModule} from 'primeng/table';
import {ButtonModule} from 'primeng/button';
import {InputTextModule} from 'primeng/inputtext';
import {ToggleButtonModule} from 'primeng/togglebutton';
import {RippleModule} from 'primeng/ripple';
import {MultiSelectModule} from 'primeng/multiselect';
import {DropdownModule} from 'primeng/dropdown';
import {ProgressBarModule} from 'primeng/progressbar';
import {ToastModule} from 'primeng/toast';
import {SliderModule} from 'primeng/slider';
import {RatingModule} from 'primeng/rating';
import {CalendarModule} from "primeng/calendar";
import {DialogModule} from "primeng/dialog";

@NgModule({
    imports: [
        CommonModule,
        LoanAccountRoutingModule,
        FormsModule,
        TableModule,
        RatingModule,
        ButtonModule,
        SliderModule,
        InputTextModule,
        ToggleButtonModule,
        RippleModule,
        MultiSelectModule,
        DropdownModule,
        ProgressBarModule,
        ToastModule,
        CalendarModule,
        DialogModule
    ],
    declarations: [LoanAccountComponent]
})
export class LoanAccountModule {
}
