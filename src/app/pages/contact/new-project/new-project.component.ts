import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-new-project',
  templateUrl: './new-project.component.html',
  styleUrls: ['./new-project.component.scss']
})
export class NewProjectComponent implements OnInit {

  hiringForm = {
    firstName: '',
    lastName: '',
    yourCompanyName: '',
    projectCompanyName: '',
    email: '',
    phone: '',
    jobDescription: '',
    rateRange: '',
    employmentType: '',
    workLocation: '',
    projectLocation: ''
  };

  submitting = false;
  submitSuccess = false;
  submitError = false;

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
  }

  submitHiringForm(event: Event) {
    event.preventDefault();
    
    this.submitting = true;
    this.submitSuccess = false;
    this.submitError = false;

    const formData = new FormData();
    formData.append('firstName', this.hiringForm.firstName);
    formData.append('lastName', this.hiringForm.lastName);
    formData.append('yourCompanyName', this.hiringForm.yourCompanyName);
    formData.append('projectCompanyName', this.hiringForm.projectCompanyName);
    formData.append('email', this.hiringForm.email);
    formData.append('phone', this.hiringForm.phone);
    formData.append('jobDescription', this.hiringForm.jobDescription);
    formData.append('rateRange', this.hiringForm.rateRange);
    formData.append('employmentType', this.hiringForm.employmentType);
    formData.append('workLocation', this.hiringForm.workLocation);
    if (this.hiringForm.projectLocation) {
      formData.append('projectLocation', this.hiringForm.projectLocation);
    }

    this.http.post('https://forms.xdm.io/dangibson.php', formData).subscribe({
      next: (response) => {
        this.submitting = false;
        this.submitSuccess = true;
        // Reset form
        this.hiringForm = {
          firstName: '',
          lastName: '',
          yourCompanyName: '',
          projectCompanyName: '',
          email: '',
          phone: '',
          jobDescription: '',
          rateRange: '',
          employmentType: '',
          workLocation: '',
          projectLocation: ''
        };
      },
      error: (error) => {
        this.submitting = false;
        this.submitError = true;
        console.error('Form submission error:', error);
        console.error('Error status:', error.status);
        console.error('Error message:', error.message);
        console.error('Error details:', error.error);
      }
    });
  }

}
