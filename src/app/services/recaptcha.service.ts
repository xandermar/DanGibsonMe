import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

interface Grecaptcha {
  execute(siteKey: string, options: { action: string }): Promise<string>;
}

declare global {
  interface Window {
    grecaptcha: Grecaptcha;
  }
}

@Injectable({
  providedIn: 'root',
})
export class RecaptchaService {
  private scriptLoaded = false;

  loadScript(): Promise<void> {
    return new Promise((resolve, reject) => {
      if (this.scriptLoaded) {
        resolve();
        return;
      }

      const script = document.createElement('script');
      script.src = `https://www.google.com/recaptcha/api.js?render=${environment.recaptchaSiteKey}`;
      script.async = true;
      script.defer = true;
      script.onload = () => {
        this.scriptLoaded = true;
        resolve();
      };
      script.onerror = () => reject('Failed to load reCAPTCHA script');
      document.head.appendChild(script);
    });
  }

  execute(action: string): Promise<string> {
    return this.loadScript().then(() =>
      window.grecaptcha.execute(environment.recaptchaSiteKey, { action })
    );
  }
}
