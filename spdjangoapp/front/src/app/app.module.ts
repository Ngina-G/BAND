import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { HttpClientModule } from '@angular/common/http';    
import { FormsModule } from '@angular/forms';    
import { UserService } from './core/services/user.service';
import { LoginPageComponent } from './core/authentication/login-page/login-page.component';
import { ProtectedPageComponent } from './core/authentication/protected-page/protected-page.component';    
 
@NgModule({
  declarations: [
    AppComponent,
    LoginPageComponent,
    ProtectedPageComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
  ],
  providers: [UserService],
  bootstrap: [AppComponent]
})
export class AppModule { }
