import { Component } from '@angular/core';
import { PredictionService } from '../services/prediction.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { ResultDialogComponent } from './result-dialog/result-dialog.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Spam r Ham?';
  emailText = '';
  predictResult = '';

  constructor(private snackBar: MatSnackBar,
    private predictionService: PredictionService) { }

  submitEmailText() {
    const result = this.predictionService.getPrediction(this.emailText)
      .subscribe((res) => {
        const data = `Confidence: ${res.confidence}, Is Spam? ${res.isSpam}`;
        this.showResultSnackBar(data);
      });
  }

  showResultSnackBar(data: string) {
    this.snackBar.openFromComponent(ResultDialogComponent, {
      duration: 3 * 1000,
      horizontalPosition: 'center',
      verticalPosition: 'bottom',
      data: data
    });
  }

  clearEmailText() {
    this.emailText = '';
  }

  logEvent(text: string) {
    console.log(text);
  }
}

