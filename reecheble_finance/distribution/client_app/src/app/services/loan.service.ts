import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {LoanAccountApiResponseModel, LoanAccountModel} from "../models/loan-account-model";
import {catchError, Observable, throwError} from "rxjs";
import {map} from "rxjs/operators";
import {LoanModel, LoanModelsApiResponseModel} from "../models/loan-model";

@Injectable()
export class LoanService {

    private apiEndpoint = 'http://0.0.0.0:8000/latest';

    constructor(private http: HttpClient) {
    }

    getAccountLoans(accountNumber: string): Observable<LoanModel[]> {
        let url = `${this.apiEndpoint}/loan/get_loans/${accountNumber}`;

        return this.http.get<LoanModelsApiResponseModel>(url)
            .pipe(
                map(response => {
                    const accountLoans: LoanModel[] = response.data.map(data =>
                        LoanModel.transformToLoan(data));
                    return accountLoans;
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

}
