import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {catchError, Observable, throwError} from "rxjs";
import {map} from "rxjs/operators";
import {LoanModel, LoanModelApiResponseModel, LoanModelsApiResponseModel} from "../models/loan-model";
import {LoanRequestModel, LoanResponseModel} from "../models/loan-request-model";
import {LoanInstallmentApiResponseModel, LoanInstallmentRequestModel} from "../models/loan-installment-model";
import {LoanAccountsApiResponseModel} from "../models/loan-account-model";

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

    addLoanRequest(loanRequestModel: LoanRequestModel): Observable<LoanResponseModel> {
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

    getAccountLoanById(id: string): Observable<LoanModel> {
        let url = `${this.apiEndpoint}/loan/get_loan/${id}`;

        return this.http.get<LoanModelApiResponseModel>(url)
            .pipe(
                map(response => {
                    return LoanModel.transformToLoan(response.data);
                }),
                catchError(this.handleError)
            );
    }

    addLoanInstallmentRequest(loanInstallmentRequestModel: LoanInstallmentRequestModel): Observable<LoanInstallmentApiResponseModel> {
        let url = `${this.apiEndpoint}/loan/pay_loan`;

        return this.http.post<LoanAccountsApiResponseModel>(url, loanInstallmentRequestModel.transformToLoanInstallmentRequestApiModel())
            .pipe(
                map(response => {
                    return LoanInstallmentRequestModel.transformApiResponseToLoanInstallmentResponseModel(response);
                }),
                catchError(this.handleError)
            );
    }

    private handleError(err: HttpErrorResponse): Observable<never> {
        // Handle the error as before
        return throwError(() => new Error('Something bad happened; please try again later.'));
    }

}
