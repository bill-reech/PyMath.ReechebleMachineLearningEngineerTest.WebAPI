import {RouterModule} from '@angular/router';
import {NgModule} from '@angular/core';
import {NotfoundComponent} from './components/notfound/notfound.component';
import {AppLayoutComponent} from "./layout/app.layout.component";

@NgModule({
    imports: [
        RouterModule.forRoot([
            {
                path: '', component: AppLayoutComponent,
                children: [
                    {
                        path: 'reecheble-finance',
                        loadChildren: () => import('./components/reecheble-finance/reecheble-finance.module').then(m => m.ReechebleFinanceModule)
                    }
                ]
            },
            {path: 'auth', loadChildren: () => import('./components/auth/auth.module').then(m => m.AuthModule)},
            {
                path: 'landing',
                loadChildren: () => import('./components/landing/landing.module').then(m => m.LandingModule)
            },
            {path: 'notfound', component: NotfoundComponent},
            {path: '**', redirectTo: '/notfound'},
        ], {scrollPositionRestoration: 'enabled', anchorScrolling: 'enabled', onSameUrlNavigation: 'reload'})
    ],
    exports: [RouterModule]
})
export class AppRoutingModule {
}
