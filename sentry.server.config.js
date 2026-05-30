import * as Sentry from "@sentry/astro";

Sentry.init({
  dsn: "https://544bee4c777ee8697e6bcf63b586d1a3@o4511478654631936.ingest.de.sentry.io/4511478661447760",
  tracesSampleRate: 1.0,
});
