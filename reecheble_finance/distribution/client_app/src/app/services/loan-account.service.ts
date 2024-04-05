import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {
    LoanAccountApiResponseModel,
    LoanAccountApiResponseModelData,
    LoanAccountsApiResponseModel
} from "../models/loan-account-model";
import {catchError, Observable, throwError} from "rxjs";
import {map} from "rxjs/operators";

@Injectable()
export class LoanAccountService {

    private apiEndpoint = 'http://0.0.0.0:8000/latest';

    constructor(private http: HttpClient) {
    }

    getLoanAccounts(): Observable<LoanAccountApiResponseModelData[]> {
        let url = `${this.apiEndpoint}/account/all_accounts`;

        return this.http.get<LoanAccountsApiResponseModel>(url)
            .pipe(
                map(response => {
                    const loanAccounts: LoanAccountApiResponseModelData[] = response.data.map(data =>
                        LoanAccountApiResponseModelData.transformToLoanAccountApiResponseModel(data));
                    return loanAccounts;
                }),
                catchError(this.handleError)
            );
    }

    addLoanAccount(userAccount: LoanAccountApiResponseModelData): Observable<LoanAccountApiResponseModel> {
        let url = `${this.apiEndpoint}/account/add_account`;

        return this.http.post<LoanAccountApiResponseModel>(url, userAccount.transformToLoanAccountApiRequestModel())
            .pipe(
                map(response => {
                    response.data = LoanAccountApiResponseModelData.transformToLoanAccountApiResponseModel(response.data);
                    return response;
                }),
                catchError(this.handleError)
            );
    }

    private handleError(err: HttpErrorResponse): Observable<never> {
        // Handle the error as before
        return throwError(() => new Error('Something bad happened; please try again later.'));
    }
}
