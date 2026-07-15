import fr from "../../cv.fr.json";
import en from "../../cv.en.json";

export const locales = ["fr", "en"] as const;
export type Locale = (typeof locales)[number];
export const defaultLocale: Locale = "fr";

export type CV = typeof fr;

export function toLocale(locale: string | undefined): Locale {
	return locale === "en" ? "en" : defaultLocale;
}

export function getCV(locale: string | undefined): CV {
	return toLocale(locale) === "en" ? (en as CV) : fr;
}
