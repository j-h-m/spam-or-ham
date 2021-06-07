import { Injectable } from '@angular/core';
import { environment } from '../environments/environment';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { HttpHeaders } from '@angular/common/http';
import { Result } from 'src/models/result';

@Injectable({
  providedIn: 'root'
})
export class PredictionService {
  apiUrl: string = '';

  constructor(private http: HttpClient) { 
    this.apiUrl = environment.api;
  }

  getPrediction(text: string): Observable<Result> {
    const httpOptions = {
      headers: new HttpHeaders({
        'Context-Type': 'application/json'
      })
    };

    return this.http.post<Result>(this.apiUrl, {
      'text': text
    }, httpOptions);
  }
}
