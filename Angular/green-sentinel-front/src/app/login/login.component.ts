import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent implements OnInit {
  constructor() {}

  abc;

  data;

  async ngOnInit() {
    // this.abc = fetch('http://127.0.0.1:8000/sensor/').then((response) =>
    //   response.json()
    // );
  
    // example consuming code
    this.data = await this.teste(
      "http://127.0.0.1:8000/sensor/"
    );

    // this.abc = fetch('http://127.0.0.1:8000/sensor/', {mode: 'no-cors'}).then((response) => response.json()).then((data) => console.log(data));
  }

  async teste(
    request: RequestInfo
  ): Promise<any> {
    const response = await fetch(request, {mode: 'no-cors'});
    const body = await response.json();
    return body;
  }
}
