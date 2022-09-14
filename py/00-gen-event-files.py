import csv
import datetime
import os

import frontmatter
import requests
from markdownify import markdownify

# download event data
# url of published sheet with website events
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQFbsfbW8WSKrlJ1Mog0vTPbyOsuk9pbiQqsmn2iO75k6KaICj1R3Mz4m-YPlgoecY9VDiQjp-HDvF_/pub?gid=1746203328&single=true&output=tsv"
res = requests.get(url)
res.raise_for_status()

# parse csv
csv_string = res.content.decode(encoding="utf-8")
events = csv.DictReader(csv_string.splitlines(), delimiter="\t")

# TODO: add slugs
yaml_keys = ["start", "end", "title", "correlaidx", "tags", "id", "slug"]
for event in events:
    print("------")
    print(f"Processing Event {event['title']}")
    # only create files for events within three months (important for long-term event series)
    today = datetime.datetime.now().astimezone()
    start_dt = datetime.datetime.fromisoformat(event["start"])
    if (start_dt - today).days > 90:
        print(f"Skipping event because it's too far in the future ({start_dt})")
        continue

    # parse metadata into dictionary
    metadata = {key: event[key] for key in yaml_keys}
    if metadata.get("tags") != "":
        metadata["tags"] = metadata["tags"].split(sep=",")
    else: 
        del metadata["tags"]
    # get markdown from html
    content = markdownify(event.get("description", ""))

    # create a "Post" object and dump to file -> this creates a hugo compatible file
    post = frontmatter.Post(content)
    post.metadata = metadata

    # events are sorted into folders with yyyy-mm
    start_year_month = start_dt.strftime("%Y-%m")
    # if the event has a slug specified, use that. otherwise hash the id
    if event.get("slug") and event.get("slug") != "":
        file_prefix = event.get("slug")
    else: 
        file_prefix = str(abs(hash(event["id"])))[0:10] 

    # both languages
    for lang in ["de", "en"]:
        folder_path = f"content/{lang}/events/{start_year_month}/"
        # create folder if it doesnt exist
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

        # create file
        file_path = f"{folder_path}/{file_prefix}.md"
        with open(file_path, "w+") as f:
            f.write(frontmatter.dumps(post))
