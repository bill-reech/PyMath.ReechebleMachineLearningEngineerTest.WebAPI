import {NgModule} from '@angular/core';
import {RouterModule} from '@angular/router';
import {FeatureManagementComponent} from './feature-management.component';

@NgModule({
    imports: [RouterModule.forChild([
        {path: '', component: FeatureManagementComponent}
    ])],
    exports: [RouterModule]
})
export class FeatureManagementRoutingModule {
}
