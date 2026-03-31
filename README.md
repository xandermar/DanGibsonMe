# DanGibson.Me (Angular)

Personal site built with Angular (v13) and Bootstrap.

## Pages / Routes

Routes are defined in `src/app/app-routing.module.ts`.

- `/` — Home
- `/experience` — Experience page (includes a Table of Contents and an in-page “Back to Top” control)
- `/portfolio` — Portfolio page (includes a Table of Contents and an in-page “Back to Top” control)
- `/contact` — Contact landing page
- `/contact/schedule-call` — Schedule a call
- `/contact/new-project` — New project inquiry

## How the site works

### UI

- Angular SPA rendered from `src/index.html` and bootstrapped via `src/main.ts`.
- Styling is primarily `src/styles.scss` plus per-component styles.
- Uses Bootstrap + FontAwesome (see `package.json`).

### Table of Contents / anchor links

The Experience and Portfolio pages use in-page anchors (`#fragment`) for their Table of Contents.
Angular router is configured with `anchorScrolling: 'enabled'` so fragment links scroll correctly.

### Contact forms (EmailJS + reCAPTCHA v3)

- reCAPTCHA v3 is loaded dynamically by `src/app/services/recaptcha.service.ts`.
- Email sending is handled via EmailJS (package `@emailjs/browser`).

Configure EmailJS credentials in:

- `src/environments/environment.ts`
- `src/environments/environment.prod.ts`

`recaptchaSiteKey` is public and can be committed. EmailJS keys are currently blank by default.

### Resume PDF

`npm run generate-resume` runs `generate_resume.py` (Python) to create `resume.pdf` and copies it into `src/assets/resume.pdf`.

Notes:

- The script expects an activated virtualenv at `.venv/bin/activate`.
- It uses ReportLab; install with `pip install reportlab` inside that venv.

## Local development

### Prerequisites

- Node.js + npm
	- This repo is Angular 13 / TypeScript 4.6; Node 16 is the safest baseline.
	- Newer Node versions can work, but dependency peer rules may be stricter.

### Install

```bash
npm install
```

### Run the dev server

```bash
npm start
```

Then open `http://localhost:4200/`.

If port 4200 is already in use:

```bash
npm start -- --port 4201
```

## Quality

```bash
npm run lint
npm run lint:fix
```

Formatting:

```bash
npm run format
npm run format:check
```

## Tests

```bash
npm test
```

## Build

```bash
npm run build
```

Build output lands in `dist/`.

## Deploy

Quick reference:

```bash
npm run deploy

npm run lint
npm run lint:fix

npm run format
npm run format:check
```

The deploy command is:

```bash
npm run deploy
```

What it does (see `package.json`):

1. Generates the resume PDF (`npm run generate-resume`)
2. Builds production Angular output (`ng build --prod --aot --base-href=/`)
3. Writes `www.dangibson.me` into the generated `CNAME`
4. Publishes `dist/DanGibsonMe-alpha` via `angular-cli-ghpages`

Deployment requirements:

- GitHub Pages (or equivalent) must be set up for the repo.
- Your git credentials must allow pushing the deployment branch used by `angular-cli-ghpages`.

## Nx note (why `ng` points to `nx`)

This repo includes Nx CLI “decoration” (`decorate-angular-cli.js`) so `ng` commands run through Nx for caching/optimizations.
You can keep using `ng`/`npm run build`/`npm start` normally.
