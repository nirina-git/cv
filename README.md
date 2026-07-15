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

## Analytics (Umami, optionnel)

Le site peut embarquer le script [Umami](https://umami.is/) (statistiques légères, sans cookies). Il n'est inclus dans le HTML que si les deux variables sont fournies **au build** (voir `.env.example`) :

- `PUBLIC_UMAMI_SRC` — URL du script de l'instance (ex. `https://analytics.rmnjs.org/script.js`)
- `PUBLIC_UMAMI_WEBSITE_ID` — identifiant du site dans Umami

### Déployer Umami sur le VPS via Dokploy

1. Dans Dokploy, créer un projet **umami** avec un service *Docker Compose* et le compose officiel :
   PostgreSQL + `ghcr.io/umami-software/umami:postgresql-latest` (voir [docs Umami](https://umami.is/docs/install)). Définir `DATABASE_URL` et un `APP_SECRET` aléatoire.
2. Exposer le service sur un sous-domaine (ex. `analytics.rmnjs.org`) via le reverse-proxy Dokploy, avec certificat TLS.
3. Se connecter à Umami (admin/umami par défaut — changer le mot de passe), créer le site
   *nirina.rmnjs.org* et récupérer son **Website ID**.
4. Dans le service Dokploy du CV, renseigner les deux variables comme **build args** :
   `PUBLIC_UMAMI_SRC=https://analytics.rmnjs.org/script.js` et `PUBLIC_UMAMI_WEBSITE_ID=<id>`, puis redéployer.

## Licence

[MIT](LICENSE.txt)
