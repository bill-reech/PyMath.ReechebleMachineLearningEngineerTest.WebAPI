import {LoanModel} from "../../../models/loan-model";
import {LoanService} from "../../../services/loan.service";
import {ActivatedRouteSnapshot, ResolveFn, RouterStateSnapshot} from "@angular/router";
import {inject} from "@angular/core";
import {Observable} from "rxjs";
import {map} from "rxjs/operators";

export const LoanAccountResolver: ResolveFn<Observable<{ accountLoans: LoanModel[], accountNumber: string }>> = (
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot,
) => {
    const accountNumber = route.paramMap.get('account_number')!;
    return inject(LoanService).getAccountLoans(accountNumber).pipe(
        map(loans => ({accountLoans: loans, accountNumber: accountNumber}))
    );
};
