#!/usr/bin/env python

from openpyxl import load_workbook
from pyglottolog import Glottolog, fts

repo = Glottolog("../glottolog")

def glottolog_url(languoid):
    return f"https://glottolog.org/resource/languoid/id/{languoid.id}"


def lookup(name):
    count, results = fts.search_langs(repo, f"language:{name}")
    return results

wb = load_workbook("omaa_languages.xlsx")

ws = wb.active

for row in ws:
    crate_id = row[0].value
    name = row[1].value
    alt_name = row[2].value
    languoids = lookup(name)
    print(f"## {name}")
    print("")
    for l in languoids:
        url = glottolog_url(l)
        print(f"* [{l.id} {l.name} {l.level}]({url})")
    print("")
