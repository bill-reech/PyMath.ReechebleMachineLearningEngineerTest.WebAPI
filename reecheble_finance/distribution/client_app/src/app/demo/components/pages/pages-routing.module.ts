import {NgModule} from '@angular/core';
import {RouterModule} from '@angular/router';

@NgModule({
    imports: [RouterModule.forChild([
        {path: 'crud', loadChildren: () => import('./crud/crud.module').then(m => m.CrudModule)},
        {
            path: 'feature-management',
            loadChildren: () => import('./feature-management/feature-management.module').then(m => m.FeatureManagementModule)
        },
        {
            path: 'loan-account-management',
            loadChildren: () => import('./loan-management/loan-management.module').then(m => m.LoanManagementModule)
        },
        {
            path: 'loan-accounts',
            loadChildren: () => import('./loan-accounts/loan-accounts.module').then(m => m.LoanAccountsModule)
        },
        {path: 'empty', loadChildren: () => import('./empty/emptydemo.module').then(m => m.EmptyDemoModule)},
        {
            path: 'timeline',
            loadChildren: () => import('./timeline/timelinedemo.module').then(m => m.TimelineDemoModule)
        },
        {path: '**', redirectTo: '/notfound'}
    ])],
    exports: [RouterModule]
})
export class PagesRoutingModule {
}
