#!/bin/bash 
echo "deleting old pages"


for f in data/projects/*; do
  id=$(basename $f .json)
  j=$(cat $f | jq)
  hugo new projects/$id.md --cleanDestinationDir
  cp content/de/projects/$id.md content/en/projects/$id.md
done