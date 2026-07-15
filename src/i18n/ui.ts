import { toLocale } from "./cv";

export const ui = {
	fr: {
		"section.about": "À propos",
		"section.experience": "Expérience",
		"section.projects": "Projets",
		"section.skills": "Compétences",
		"section.education": "Formation",
		"section.languages": "Langues",
		"section.certificates": "Certificats",
		"date.present": "Aujourd'hui",
		"experience.summary": "Résumé :",
		"experience.responsibilities": "Responsabilités :",
		"experience.achievements": "Réalisations :",
		"experience.seeMore": "Voir plus",
		"experience.seeLess": "Voir moins",
		"experience.technologies": "Technologies utilisées",
		"common.visit": "Voir",
		"hero.copied": "Copié !",
		"hero.call": "Appeler",
		"hero.visitProfile": "Voir le profil",
		"palette.pressPre": "Appuie sur",
		"palette.pressPost": "pour ouvrir la palette de commandes.",
		"palette.placeholder": "Rechercher une commande",
		"palette.print": "Imprimer le CV",
		"palette.visit": "Ouvrir",
		"theme.system": "Système",
		"theme.dark": "Sombre",
		"theme.light": "Clair",
	},
	en: {
		"section.about": "About",
		"section.experience": "Experience",
		"section.projects": "Projects",
		"section.skills": "Skills",
		"section.education": "Education",
		"section.languages": "Languages",
		"section.certificates": "Certificates",
		"date.present": "Present",
		"experience.summary": "Summary:",
		"experience.responsibilities": "Responsibilities:",
		"experience.achievements": "Achievements:",
		"experience.seeMore": "Show more",
		"experience.seeLess": "Show less",
		"experience.technologies": "Technologies used",
		"common.visit": "Visit",
		"hero.copied": "Copied!",
		"hero.call": "Call",
		"hero.visitProfile": "Visit profile",
		"palette.pressPre": "Press",
		"palette.pressPost": "to open the command palette.",
		"palette.placeholder": "Search command",
		"palette.print": "Print resume",
		"palette.visit": "Visit",
		"theme.system": "System",
		"theme.dark": "Dark",
		"theme.light": "Light",
	},
} as const;

export type UIKey = keyof (typeof ui)["fr"];

export function useTranslations(locale: string | undefined) {
	const l = toLocale(locale);
	return (key: UIKey): string => ui[l][key];
}
