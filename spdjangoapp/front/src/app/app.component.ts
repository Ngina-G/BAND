import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApiService]
})
export class AppComponent {
  notes = [{title: 'test1'},{notes:'hi'}];

  constructor(private api: ApiService) {
    this.getNotes(); 
  }
  getNotes =  () => {
    this.api.getAllNotes().subscribe(
      data => {
        this.notes = data;
      },
      error => {
        console.log(error);
      }
    )
  }


}
