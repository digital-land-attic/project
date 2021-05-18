#!/usr/bin/env python3

import csv
import yaml
import requests
from pathlib import Path

from frontmatter import Frontmatter

sheet = "Sheet1"
key = "1hOnXFXQFOt_pYIs6haCzym1eLPzBupvTQP0DWZh37ww"
CSV_URL = "https://docs.google.com/spreadsheets/d/%s/gviz/tq?tqx=out:csv&sheet={%s}" % (
    key,
    sheet,
)


def create_frontmatter(entry):
    frontmatter = {
        "name": entry.get("Name"),
        "type": entry.get("Type"),
        "author": entry.get("Author"),
        "date": entry.get("Date"),
    }
    return yaml.dump(frontmatter, default_flow_style=False)


def create_markdown(entry):
    # TODO return markdown as string
    md_string = f"""---
{create_frontmatter(entry)}---

{entry.get('Update')}
"""
    return md_string


session = requests.Session()
download = session.get(CSV_URL)
content = download.content.decode("utf-8")

for entry in csv.DictReader(content.splitlines()):
    project = entry["Project"]
    fname = entry["Name"].lower().replace(" ", "-")

    updates_dir = Path("projects/{}/updates".format(project))
    updates_dir.mkdir(exist_ok=True)

    markdown_file = Path("{}/{}".format(updates_dir, fname + ".md"))
    if markdown_file.is_file():
        continue

    markdown = create_markdown(entry)

    with open(markdown_file, "w") as f:
        f.write(markdown)
