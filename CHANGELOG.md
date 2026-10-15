# CHANGELOG

Toutes les modifications notables de ce projet sont documentées ici.

## [2.0.0] — 2026-10-15

Testé sur tinyMediaManager 5.3.2.

### Breaking

- Renommage `Koromerzin-TV-CSV/` → `Koromerzhin-TV-CSV/` (faute de frappe, cohérence avec `Koromerzhin-Movie-CSV/`). Les chemins d'installation existants doivent être mis à jour.
- Sortie CSV désormais quotée RFC 4180 (tous les champs entre `"`) : les consommateurs qui découpaient sur `;` nu doivent parser en CSV strict.

### Ajouté

- Template séries étendu : 3 → 12 colonnes (TVDB, année, première diffusion `yyyy-MM-dd`, statut, saisons, épisodes, durée, genres, certification).
- `examples/example-movie.csv` et `examples/example-tv.csv` (incluent des lignes pièges avec `;`).
- `tools/check_csv.py` : validation d'un export contre son `list.jmte` (en-tête + nombre de colonnes, quoting strict).
- `template.conf` : descriptions réelles + `url` du dépôt.

### Corrigé

- Films : `${movie.movieSet}` (objet, rendu non garanti) → `${movie.movieSetTitle}` (chaîne documentée).
- README : procédure d'import réelle (Tools → Open content folder → `templates/` → Export), au lieu des « scripts » inexistants.

## [1.0.0] — historique

- Templates initiaux : films 9 champs non quotés, séries 3 champs.
