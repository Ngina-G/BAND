import { Component, OnInit } from '@angular/core';
import {NotesService} from './core/services/notes.service'; 
import {UserService} from './core/services/user.service';
import {throwError} from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})


export class AppComponent{
  title = 'front';
}
