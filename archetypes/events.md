---
title: "{{ replace .Name "-" " " | title }}"
correlaidx: false # set to true to change design of event page to blue/red
start: {{ .Date }} # edit date in ISO Format, e.g. 2022-09-06, leave time part alone -> specify start time in eventTime 
eventTime: "" # start / end time of event, free text, e.g. 15:30-16:00
place: "" #optional: set place of event
eventRegistration: "https://pretix.eu/correlaid" # leave empty if not needed
tags: [] 
languages: ["english"]
---

## The event / Das Event

## The speakers / Referent*innen 


