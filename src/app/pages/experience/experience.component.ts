import { AfterViewInit, Component, HostListener } from '@angular/core';

@Component({
  selector: 'app-experience',
  templateUrl: './experience.component.html',
  styleUrls: ['./experience.component.scss'],
})
export class ExperienceComponent implements AfterViewInit {
  showBackToTop = false;

  ngAfterViewInit(): void {
    this.updateBackToTopVisibility();
  }

  @HostListener('window:scroll')
  onWindowScroll(): void {
    this.updateBackToTopVisibility();
  }

  scrollToTop(): void {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  private updateBackToTopVisibility(): void {
    this.showBackToTop = window.scrollY > 200;
  }
}
