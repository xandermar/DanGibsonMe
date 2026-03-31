import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../../environments/environment';
import * as emailjs from '@emailjs/browser';

@Component({
  selector: 'app-new-project',
  templateUrl: './new-project.component.html',
  styleUrls: ['./new-project.component.scss']
})
export class NewProjectComponent implements OnInit {

  isW2 = false;

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

  private async sendW2AutoReply(firstName: string, email: string): Promise<void> {
    const emailJsConfig = environment.emailjs;

    if (!emailJsConfig?.publicKey || !emailJsConfig?.serviceId || !emailJsConfig?.templateId) {
      console.warn('EmailJS not configured; skipping W2 auto-reply email.');
      return;
    }

    const body = `Hi ${firstName},

A present, I'm currently seeking C2C opportunities. Please let me know if the opportunity you submitted will allow C2C or if you may have other opportunities open to such.

Please see my resume here:
https://www.dangibson.me/assets/resume.pdf

Thanks a bunch for your interest in me!

-- Dan Gibson
`;

    try {
      await emailjs.send(
        emailJsConfig.serviceId,
        emailJsConfig.templateId,
        {
          to_email: email,
          to_name: firstName,
          subject: 'New Project for Dan Gibson',
          message: body,
          from_name: 'Dan Gibson',
          from_email: 'daniel.gibson@xandermar.com',
          reply_to: 'daniel.gibson@xandermar.com',
        },
        { publicKey: emailJsConfig.publicKey }
      );
    } catch (error) {
      console.error('W2 auto-reply email send failed:', error);
    }
  }

  submitHiringForm(event: Event) {
    event.preventDefault();

    this.submitting = true;
    this.submitSuccess = false;
    this.submitError = false;

    const submittedFirstName = this.hiringForm.firstName;
    const submittedEmail = this.hiringForm.email;
    const submittedEmploymentType = this.hiringForm.employmentType;

    if (submittedEmploymentType === 'W2' && this.isW2 === false) {
      void this.sendW2AutoReply(submittedFirstName, submittedEmail);
    }

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
