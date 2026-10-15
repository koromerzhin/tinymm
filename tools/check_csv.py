#!/usr/bin/env python3
"""Valide un CSV exporté par les templates tinyMediaManager de ce dépôt.

Vérifie (RFC 4180, séparateur `;`) :
- l'en-tête est identique à la première ligne du `list.jmte` du template,
- chaque ligne a le bon nombre de colonnes (quoting strict).

Usage :
    python3 tools/check_csv.py <export.csv> <template-list.jmte>

Exemple :
    python3 tools/check_csv.py /tmp/movies.csv Koromerzhin-Movie-CSV/list.jmte
"""

import csv
import sys


def read_header(path):
    with open(path, encoding="utf-8-sig") as f:
        first_line = f.readline()
    if not first_line.strip():
        raise ValueError(f"en-tête vide dans {path}")
    return next(csv.reader([first_line], delimiter=";", quotechar='"', strict=True))


def check(csv_path, jmte_path):
    expected = read_header(jmte_path)
    errors = []
    with open(csv_path, encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f, delimiter=";", quotechar='"', strict=True)
        try:
            actual = next(reader)
        except csv.Error as e:
            return [f"en-tête illisible : {e}"]
        if actual != expected:
            errors.append(f"en-tête inattendu : {actual} (attendu : {expected})")
        for lineno, row in enumerate(reader, start=2):
            if not row or all(not c.strip() for c in row):
                continue  # ignore les lignes vides (ex. fin de fichier TMM)
            if len(row) != len(expected):
                errors.append(
                    f"ligne {lineno} : {len(row)} colonnes au lieu de {len(expected)} : {row}"
                )
    return errors


def main(argv):
    if len(argv) != 3:
        print(__doc__)
        return 2
    try:
        errors = check(argv[1], argv[2])
    except (csv.Error, ValueError, OSError) as e:
        print(f"ERREUR : {e}")
        return 1
    if errors:
        print(f"{len(errors)} problème(s) dans {argv[1]} :")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK : {argv[1]} conforme au template {argv[2]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
