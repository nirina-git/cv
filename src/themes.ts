/*
 * Thèmes visuels du CV, au choix du visiteur (bouton dans l'en-tête).
 * Le thème actif est posé en data-theme sur <html> ; les styles propres à
 * chaque thème passent par les variantes Tailwind classic: / retro:
 * (global.css) et par les palettes de themes.css.
 *
 * Ajouter un thème : l'ajouter ici, déclarer sa palette dans themes.css et
 * sa variante dans global.css.
 */

export const THEMES = {
	classic: {
		label: "Classique",
		avatar: "/me_avatar.jpg",
		favicon: "/favicon.svg",
	},
	retro: {
		label: "Rétro",
		avatar: "/me_avatar_pixel.png",
		favicon: "/favicon-retro.svg",
	},
} as const;

export type ThemeName = keyof typeof THEMES;

export const DEFAULT_THEME: ThemeName = "classic";

/* Mode de couleur : parcouru dans cet ordre à chaque clic sur l'icône */
export const MODES = ["system", "light", "dark"] as const;

export type Mode = (typeof MODES)[number];

/* Clés localStorage (« theme » garde le mode, nom historique) */
export const STORAGE_KEYS = {
	theme: "style",
	mode: "theme",
} as const;
