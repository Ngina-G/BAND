import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {UserService} from './user.service';
 
@Injectable()
export class NotesService {
 
  constructor(private http: HttpClient, private _userService: UserService) {
  }
 
  // send a POST request to the API to create a new blog post
  create(note:any, token:string) {
    let httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': 'JWT ' + this._userService.token
      })
    };
    return this.http.post('/api/Notes', JSON.stringify(note), httpOptions);
  }
 
}