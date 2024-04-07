import {ActivatedRouteSnapshot, ResolveFn, RouterStateSnapshot} from "@angular/router";
import {inject} from "@angular/core";
import {Observable} from "rxjs";
import {map} from "rxjs/operators";
import {LoanService} from "../../../services/loan.service";
import {AccountLoansResolverModel} from "../../../models/account-loans-resolver-model";

export const LoanAccountResolver: ResolveFn<Observable<AccountLoansResolverModel>> = (
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot,
) => {
    const accountNumber = route.paramMap.get('account_number')!;

    return inject(LoanService)
        .getAccountLoans(accountNumber)
        .pipe(map(accountLoans => (new AccountLoansResolverModel(accountLoans, accountNumber))));
};
