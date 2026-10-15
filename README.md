# movie-csv-tinymm

Templates d'export CSV ([JMTE](https://www.tinymediamanager.org/docs/jmte)) pour **tinyMediaManager 5.x** (testé sur **5.3.2**) : un template films, un template séries.

## Structure du projet

- **Koromerzhin-Movie-CSV/** : export des films, une ligne par film.
  - `list.jmte` : template JMTE.
  - `template.conf` : configuration du template (`type=movie`, `extension=csv`).
- **Koromerzhin-TV-CSV/** : export des séries, une ligne par série.
  - `list.jmte` : template JMTE.
  - `template.conf` : configuration du template (`type=tv_show`, `extension=csv`).
- **examples/** : `example-movie.csv`, `example-tv.csv` — sorties attendues (avec lignes pièges contenant `;`).
- **tools/check_csv.py** : valide un CSV exporté contre son template (voir [Validation](#validation)).

### Colonnes exportées

Films (9) : `ID IMDb`, `ID TMDB`, `Titre`, `Saga`, `Année`, `Genre(s)`, `Durée`, `Pays`, `Tags`.

Séries (12) : `Titre`, `ID IMDb`, `ID TMDB`, `ID TVDB`, `Année`, `Première diffusion` (`yyyy-MM-dd`), `Statut`, `Saisons`, `Épisodes`, `Durée`, `Genre(s)`, `Certification`.

### Format

- Séparateur `;` (compatible Excel FR), fichier UTF-8.
- Tous les champs sont entourés de guillemets doubles (RFC 4180) : un `;` dans un titre ou un tag ne casse donc pas le CSV.
- Limite connue : un guillemet `"` dans une métadonnée (rare : titres, tags) n'est pas doublé par le moteur JMTE de TMM — le script `tools/check_csv.py` détecte ces lignes après export.

## Installation dans tinyMediaManager

Ne pas modifier les templates livrés avec TMM : ils sont écrasés à chaque démarrage.

1. Dans TMM : menu **Tools → Open content folder**, ouvrir le sous-dossier `templates/`.
2. Copier dedans les dossiers `Koromerzhin-Movie-CSV/` et `Koromerzhin-TV-CSV/` de ce dépôt.
3. Redémarrer TMM si besoin, puis : **Movies → Export movie list** (ou **TV Shows → Export TV show list**).
4. Choisir `Koromerzhin Movie CSV` / `Koromerzhin TV CSV`, choisir le dossier de sortie, exporter.

## Validation

Après export, vérifier le CSV (Python 3, sans dépendance) :

```sh
python3 tools/check_csv.py /chemin/vers/export-films.csv Koromerzhin-Movie-CSV/list.jmte
python3 tools/check_csv.py /chemin/vers/export-series.csv Koromerzhin-TV-CSV/list.jmte
```

Le script contrôle l'en-tête et le nombre de colonnes de chaque ligne (quoting strict) et sort en erreur sinon.

## Compatibilité

- Testé sur tinyMediaManager **5.3.2**.
- Champs utilisés conformes à la [doc JMTE TMM 5.x](https://www.tinymediamanager.org/docs/jmte) (`movie.*`, `tvShow.*`, renderer `date(yyyy-MM-dd)`).

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus d'informations.
