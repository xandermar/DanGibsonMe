import { Component } from '@angular/core';
import { Router, NavigationEnd } from '@angular/router';

// Declare gtag globally
declare const gtag: (...args: unknown[]) => void;

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  title = 'dangibson-me';

  constructor(private router: Router) {
    // Track page views on route change
    this.router.events.subscribe((event) => {
      if (event instanceof NavigationEnd) {
        gtag('config', 'G-EQ67EPWCH3', {
          page_path: event.urlAfterRedirects,
        });
      }
    });
  }
}
