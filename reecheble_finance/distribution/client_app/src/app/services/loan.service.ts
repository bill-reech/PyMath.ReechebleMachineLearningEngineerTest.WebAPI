import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {catchError, Observable, throwError} from "rxjs";
import {map} from "rxjs/operators";
import {LoanModel, LoanModelsApiResponseModel} from "../models/loan-model";
import {LoanRequestModel, LoanResponseModel} from "../models/loan-installment-model";

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

    addLoanInstallment(loanRequestModel: LoanRequestModel): Observable<LoanResponseModel> {
        let url = `${this.apiEndpoint}/loan/add_loan`;

        return this.http.post<LoanResponseModel>(url, loanRequestModel.transformToLoanRequestApiModel())
            .pipe(
                map(response => {
                    response = LoanRequestModel.transformApiResponseToLoanResponseModel(response);
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
