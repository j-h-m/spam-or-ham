import { Component } from '@angular/core';
import { PredictionService } from '../services/prediction.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Spam r Ham?';
  emailText = '';
  predictResult = '';

  constructor(private predictionService: PredictionService) { }

  submitEmailText() {
    this.logEvent(this.emailText);
    const result = this.predictionService.getPrediction(this.emailText)
      .subscribe((res) => {
        this.logEvent(res);
        this.predictResult = res;
      });
  }

  clearEmailText() {
    this.emailText = '';
  }

  logEvent(text: string) {
    console.log(text);
  }
}

