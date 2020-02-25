---
title: "Hackathon mit Stifter-Helfen und PwC"
date: 2018-09-09T00:00:00+02:00
image: "509-hackathon-stifter.jpg"
summary: "Ein Rückblick auf unsere Veranstaltung in München"
draft:      false
categories:       
    - Veranstaltungen
    - News
author: 
    name:           "CorrelAid"
    image:          "correlaid.jpg"
    description:    "CorrelAid ist seit Juli 2015 als gemeinnütziger Verein in Konstanz eingetragen. Wir haben derzeit ein ehrenamtliches Organisationsteam aus 15 Leuten und ein Netzwerk von 650 ehrenamtlichen Datenanalyst\*innen. Wir haben bereits über 10 Volunteering-Projekte mit kleinen und großen NPOs (u.a. Ashoka, europäisches Jugendparlament, streetfootballworld) initiert, über 50 Workshops für Datenanalyst\*innen durchgeführt, und zahlreiche Vorträge (u.a. bei Die Zeit, NPO-Tag von Microsoft, Bayreuther Dialoge) gehalten."
    twitter:        "https://twitter.com/correlaid"
    facebook:       "https://facebook.com/WeAreCorrelAid"
    github:         "https://github.com/correlaid"
    email:          "kontakt@correlaid.org"
    website:        "https://correlaid.org"
meta:
    title: "CorrelAid - Hackathon mit Stifter-Helfen und PwC"
    description: "Das Potential von Datenanalyse demokratisieren. Wir haben uns Anfang des
                  Jahres gefragt, wie wir auf dieser Mission auch Unternehmen einbeziehen
                  können. Letzten Monat haben wir deshalb ein neues Format getestet: Wir
                  veranstalten einen Hackathon mit engagierten Analyst\*innen aus unserem
                  Netzwerk und Mitarbeiter\*innen aus Data-Science-Abteilungen von
                  Unternehmen."
    image: "509-hackathon-stifter.jpg"
    keywords: "CorrelAid, Data4Good, Hackathon, München, PwC, PricewaterhouseCoopers, Stifter-helfen, VueJS, Dashboard, Python"
---


Das Potential von Datenanalyse demokratisieren. Wir haben uns Anfang des
Jahres gefragt, wie wir auf dieser Mission auch Unternehmen einbeziehen
können. Letzten Monat haben wir deshalb ein neues Format getestet: Wir
veranstalten einen Hackathon mit engagierten Analyst\*innen aus unserem
Netzwerk und Mitarbeiter\*innen aus Data-Science-Abteilungen von
Unternehmen.

Zusammen arbeiten wir mehrere Tage intensiv an Problemstellungen von
zivilgesellschaftlichen Organisationen. Für unseren Piloten haben wir
uns mit [PricewaterhouseCoopers
(PwC)](https://www.pwc.de/de/managementberatung/forensic-services.html)
zusammengetan, um eine Organisation zu unterstützen, welche die
Zivilgesellschaft digitalisiert.

### Die Zivilgesellschaft digitalisieren

[Stifter-helfen](https://www.stifter-helfen.de/) stellt
Software-Lizenzen für gemeinnützige Organisationen zu einem Bruchteil
der Kosten bereit, die üblicherweise für die Nutzung dieser Programme
anfallen würden. Hierfür kooperieren sie innerhalb eines globalen
Netzwerkes von auf IT fokussierten Non-Profits mit einer Vielzahl von
Softwareunternehmen, die als „Stifter“ ihre Software vergünstigt für
gemeinnützige Organisationen bereitstellen. Non-Profits aus Deutschland,
Österreich oder der Schweiz können sich mit dem Nachweis der
Gemeinnützigkeit bei Stifter-helfen anmelden.

Bei Stifter-helfen arbeitet im Hintergrund eine Datenbank. Das Ziel des
Hackathons war es, Stifter-helfen die direkte Auswertung ihrer Daten zu
ermöglichen. So soll die Reichweite erhöht werden, damit noch mehr
Vereine und Hilfsorganisationen von dem Angebot profitieren.

\
### Kick-Off

Nachdem alle Teilnehmer\*innen in der Münchner PwC Zentrale angekommen
waren, gab es eine Vorstellungsrunde. Stifter-helfen und CorrelAid haben
ihre Vereinszwecke präsentiert, unsere Gastgeber stellten den
Geschäftsbereich „Forensic Services“ vor. Anschließend wurden die
Anforderungen an das Analyseprojekt zusammen mit Stifter-helfen
besprochen.

Konkret ging es um eine Aufstellung der Lizenznehmer und zugehöriger
Umsätze nach Kriterien wie z.B. dem Zweck der Gemeinnützigkeit, die Art
der Softwarelizenzen usw. Außerdem sollten noch Potenziale zur weiteren
Förderung sowie Gemeinsamkeiten zwischen ähnlichen Vereinen analysiert
werden.

\
### Umsetzung

Nachdem die Mitarbeiterinnen von Stifter-helfen uns von Ihren
Vorstellungen erzählt hatten, entschied sich das Entwickler\*innenteam
nach kurzer technischer Diskussion für ein Browser-basiertes Dashboard
als User-Interface. Innerhalb der nächsten drei Tage arbeiteten wir im
PwC-Office München fleißig an der Implementierung von Datenbank (MS
SQL), Backend (Python) und Frontend (vue.js/js).

Der Hauptteil der Reportgenerierung sollte dabei in einer
Microsoft-SQL-Datenbank mithilfe von sogenannten *stored procedures*,
einer Art erweiterten *View*, stattfinden. Das Backend wurde mit dem
bekannten Python-Microframework [Flask](http://flask.pocoo.org/) gebaut.
Es stellt die *REST API* für das Frontend bereit, die die Daten aus der
Datenbank lädt und ein grundliegendes Usermanagement ermöglicht.
Außerdem wird hier auch die Authentifizierung der User mittels eines
Logins übernommen.

Das Frontend stellt die grafische Nutzeroberfläche bereit und verbindet
die Interface-Elemente wie Buttons und Input-Felder zu API-Calls auf das
Backend. Die Plots, welche ebenfalls im Frontend angesiedelt sind,
wurden mithilfe von plotly.js erstellt. Für die Gestaltung der Website
selbst haben wir [vue.js](https://vuejs.org/) verwendet.

\

{{< image 
    image="509-pwc_2.png"
>}}
Project Architecture
{{< /image >}}

### Abschluss

Zum Abschluss konnte das Team Stifter-helfen ein funktionsfähiges
Dashboard übergeben, mit dessen Hilfe sie erste Reports einsehen können.
Ein paar Themen blieben allerdings offen – also gibt es vielleicht in
Zukunft erneut eine Zusammenarbeit oder ein Projekt. Wir haben auf jeden
Fall alle viel gelernt und danken Stifter-helfen für ein interessantes
und nachhaltiges Projekt sowie PwC für die Unterstützung und
erstklassige Versorgung in München!

\

{{< image 
    image="509-pwc_3.png"
>}}
Web Interface
{{< /image >}}

------------------------------------------------------------------------


