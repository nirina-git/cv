# CV — Nirina Ramamonjisoa

CV/portfolio imprimable, en ligne sur [nirina.rmnjs.org](https://nirina.rmnjs.org).

Basé sur le template [Smilesharks/dev-portfolio](https://github.com/Smilesharks/dev-portfolio) (lui-même inspiré de [BartoszJarocki/cv](https://github.com/BartoszJarocki/cv) et [midudev/minimalist-portfolio-json](https://github.com/midudev/minimalist-portfolio-json)).

## Stack

- [**Astro**](https://astro.build/) + [**Tailwind CSS**](https://tailwindcss.com/) + TypeScript
- [**hotkeypad**](https://github.com/pheralb/hotkeypad) — palette de commandes (`Cmd/Ctrl + K`)
- Contenu au format [JSON Resume](https://jsonresume.org/schema/) dans `cv.json`

## Développement

```bash
npm install
npm run dev       # http://localhost:4321
```

| Commande          | Action                                              |
| :---------------- | :-------------------------------------------------- |
| `npm run dev`     | Serveur de développement sur `localhost:4321`       |
| `npm run build`   | Vérifie les types (`astro check`) et build `./dist/` |
| `npm run preview` | Prévisualisation locale du build                    |

## Contenu

Tout le contenu du CV (expériences, compétences, projets…) se modifie dans `cv.json`.

Le thème de couleurs se choisit via `basics.theme` dans `cv.json` (`default`, `blue`, `red`, `green`, `cyber`), avec variantes dark automatiques. Les thèmes sont définis dans les feuilles de style du projet.

## Déploiement

Le site est déployé sur un VPS via [Dokploy](https://dokploy.com/) à partir du `Dockerfile` (build Astro multi-stage servi par nginx) :

```bash
docker build -t cv .
docker run -p 8080:80 cv
```

Le workflow GitHub Actions (`.github/workflows/ci.yml`) vérifie que le build passe sur chaque push/PR ; le déploiement est déclenché côté Dokploy.

## Licence

[MIT](LICENSE.txt)
