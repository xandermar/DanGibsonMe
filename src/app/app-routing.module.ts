import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { ExperienceComponent } from './pages/experience/experience.component';
import { PortfolioComponent } from './pages/portfolio/portfolio.component';
import { ContactComponent } from './pages/contact/contact.component';
import { ScheduleCallComponent } from './pages/contact/schedule-call/schedule-call.component';
import { NewProjectComponent } from './pages/contact/new-project/new-project.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'experience', component: ExperienceComponent },
  { path: 'portfolio', component: PortfolioComponent },
  { path: 'contact', component: ContactComponent },
  { path: 'contact/schedule-call', component: ScheduleCallComponent },
  { path: 'contact/new-project', component: NewProjectComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
