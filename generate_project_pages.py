import json
from pprint import pprint
from urllib.request import urlopen
from datetime import date, datetime
import os

URL = "https://correlaid.github.io/projects/projects.json"

MD_TEMPLATE = """---
title: "{0}"
date: {1}
project_id_path: "{2}"
lang: "{3}"
---
# {0}
"""

# get list of projects from github pages
j = urlopen(URL)
projects = json.loads(j.read())
for proj in projects:
    # get filename of markdown
    basename = proj['project_id_path'] + ".md"


    for lang in ["de", "en"]:
        md = MD_TEMPLATE.format(proj['title'], 
                datetime.now().isoformat("T", "seconds") + "+02:00", 
                proj['project_id_path'],
                lang
        )
        file_path = "content/" + lang + "/projects/" + basename.lower()

        with open(file_path, "w+") as f:
            f.write(md)
            print("created " + file_path)