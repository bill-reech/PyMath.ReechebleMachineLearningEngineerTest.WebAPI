import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {ApiResponse, LoanAccount} from "../api/loan-account";
import {catchError, Observable, throwError} from "rxjs";
import {map} from "rxjs/operators";

@Injectable()
export class LoanAccountService {

    private apiEndpoint = 'http://0.0.0.0:8000/latest';

    constructor(private http: HttpClient) {
    }

    getLoanAccounts() {

    }

    addLoanAccount(userAccount: LoanAccount): Observable<ApiResponse> {
        let url = `${this.apiEndpoint}/account/add_account`;

        return this.http.post<ApiResponse>(url, userAccount.transformToLoanAccountApiModel())
            .pipe(
                map(response => {
                    response.data = LoanAccount.transformToLoanAccount(response.data);
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
