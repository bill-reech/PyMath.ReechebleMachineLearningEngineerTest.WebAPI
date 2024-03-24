import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {LoanAccountApiResponseModel, LoanAccountModel, LoanAccountsApiResponseModel} from "../api/loan-account-model";
import {catchError, Observable, throwError} from "rxjs";
import {map} from "rxjs/operators";

@Injectable()
export class LoanAccountService {

    private apiEndpoint = 'http://0.0.0.0:8000/latest';

    constructor(private http: HttpClient) {
    }

    getLoanAccounts(): Observable<LoanAccountModel[]> {
        let url = `${this.apiEndpoint}/account/all_accounts`;

        return this.http.get<LoanAccountsApiResponseModel>(url)
            .pipe(
                map(response => {
                    const loanAccounts: LoanAccountModel[] = response.data.map(data =>
                        LoanAccountModel.transformToLoanAccount(data));
                    return loanAccounts;
                }),
                catchError(this.handleError)
            );
    }

    addLoanAccount(userAccount: LoanAccountModel): Observable<LoanAccountApiResponseModel> {
        let url = `${this.apiEndpoint}/account/add_account`;

        return this.http.post<LoanAccountApiResponseModel>(url, userAccount.transformToLoanAccountApiModel())
            .pipe(
                map(response => {
                    response.data = LoanAccountModel.transformToLoanAccount(response.data);
                    return response;
                }),
                catchError(this.handleError)
            );
    }

    private handleError(err: HttpErrorResponse): Observable<never> {
        // Handle the error as before
        return throwError(() => new Error('Something bad happened; please try again later.'));
    }

    getLoanAccountById(id: string) {

    }
}
