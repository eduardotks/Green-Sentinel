import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnInit {
  selectedTab: Number;
  repos: Array<any>;
  kudos: Array<any>;

  constructor(
  ) {
  }

  async ngOnInit() {
  }
}
