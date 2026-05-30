import * as Sentry from "@sentry/astro";

Sentry.init({
  dsn: "https://544bee4c777ee8697e6bcf63b586d1a3@o4511478654631936.ingest.de.sentry.io/4511478661447760",
  tracesSampleRate: 1.0,
  replaysSessionSampleRate: 0.1,
  replaysOnErrorSampleRate: 1.0,
  integrations: [
    Sentry.browserTracingIntegration(),
    Sentry.replayIntegration(),
  ],
});

// TODO: remove after confirming events appear in Sentry dashboard
Sentry.captureMessage("Sentry pipeline test — page load", "info");
