import {NgModule} from '@angular/core';
import {LocationStrategy, PathLocationStrategy} from '@angular/common';
import {AppComponent} from './app.component';
import {AppRoutingModule} from './app-routing.module';
import {AppLayoutModule} from './layout/app.layout.module';
import {NotfoundComponent} from './components/notfound/notfound.component';
import {ProductService} from './services/product.service';
import {LoanAccountService} from "./services/loan-account.service";
import {LoanService} from "./services/loan.service";

@NgModule({
    declarations: [AppComponent, NotfoundComponent],
    imports: [AppRoutingModule, AppLayoutModule],
    providers: [
        {provide: LocationStrategy, useClass: PathLocationStrategy},
        ProductService,
        LoanAccountService,
        LoanService
    ],
    bootstrap: [AppComponent],
})
export class AppModule {
}
