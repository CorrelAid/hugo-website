---
title: "Hackathon Stifterhelfen"
date: 2018-09-08T23:33:29+02:00
image: stifterhelfen.jpg
summary: "Ende August hat sich ein Team aus 8 Freiwilligen zu einem Hackathon in München getroffen. In einer Kooperation von CorrelAid und PwC wurde ein Dashboard zur Visalierung von Geschäftsprozessen realisiert."
draft: true
---

Das Potential von Datenanalyse demokratisieren. Wir haben uns Anfang des Jahres gefragt, wie wir auf dieser Mission auch Unternehmen einbeziehen können. Letzten Monat haben wir deshalb ein neues Format getestet: Wir veranstalten einen Hackathon mit engagierten AnalystInnen aus unserem Netzwerk und MitarbeiterInnen aus Data-Science-Abteilungen von Unternehmen.

Zusammen arbeiten wir mehrere Tage intensiv an Problemstellungen von zivilgesellschaftlichen Organisationen. Für unseren Piloten haben wir uns mit PricewaterhouseCoopers (PwC) zusammengetan, um eine Organisation zu unterstützen, welche die Zivilgesellschaft digitalisiert.
Die Zivilgesellschaft digitalisieren

Stifter-helfen stellt Software-Lizenzen für gemeinnützige Organisationen zu einem Bruchteil der Kosten bereit, die üblicherweise für die Nutzung dieser Programme anfallen würden. Hierfür kooperieren sie innerhalb eines globalen Netzwerkes von auf IT fokussierten Non-Profits mit einer Vielzahl von Softwareunternehmen, die als „Stifter“ ihre Software vergünstigt für gemeinnützige Organisationen bereitstellen. Non-Profits aus Deutschland, Österreich oder der Schweiz können sich mit dem Nachweis der Gemeinnützigkeit bei Stifter-helfen anmelden.

Bei Stifter-helfen arbeitet im Hintergrund eine Datenbank. Das Ziel des Hackathons war es, Stifter-helfen die direkte Auswertung ihrer Daten zu ermöglichen. So soll die Reichweite erhöht werden, damit noch mehr Vereine und Hilfsorganisationen von dem Angebot profitieren.

Kick-Off

Nachdem alle Teilnehmer*innen in der Münchner PwC Zentrale angekommen waren, gab es eine Vorstellungsrunde. Stifter-helfen und CorrelAid haben ihre Vereinszwecke präsentiert, unsere Gastgeber stellten den Geschäftsbereich „Forensic Services“ vor. Anschließend wurden die Anforderungen an das Analyseprojekt zusammen mit Stifter-helfen besprochen.

Konkret ging es um eine Aufstellung der Lizenznehmer und zugehöriger Umsätze nach Kriterien wie z.B. dem Zweck der Gemeinnützigkeit, die Art der Softwarelizenzen usw. Außerdem sollten noch Potenziale zur weiteren Förderung sowie Gemeinsamkeiten zwischen ähnlichen Vereinen analysiert werden.

Umsetzung

Nachdem die Mitarbeiterinnen von Stifter-helfen uns von Ihren Vorstellungen erzählt hatten, entschied sich das Entwickler*innenteam nach kurzer technischer Diskussion für ein Browser-basiertes Dashboard als User-Interface. Innerhalb der nächsten drei Tage arbeiteten wir im PwC-Office München fleißig an der Implementierung von Datenbank (MS SQL), Backend (Python) und Frontend (vue.js/js).

Der Hauptteil der Reportgenerierung sollte dabei in einer Microsoft-SQL-Datenbank mithilfe von sogenannten stored procedures, einer Art erweiterten View, stattfinden. Das Backend wurde mit dem bekannten Python-Microframework Flask gebaut. Es stellt die REST API für das Frontend bereit, die die Daten aus der Datenbank lädt und ein grundliegendes Usermanagement ermöglicht. Außerdem wird hier auch die Authentifizierung der User mittels eines Logins übernommen.

Das Frontend stellt die grafische Nutzeroberfläche bereit und verbindet die Interface-Elemente wie Buttons und Input-Felder zu API-Calls auf das Backend. Die Plots, welche ebenfalls im Frontend angesiedelt sind, wurden mithilfe von plotly.js erstellt. Für die Gestaltung der Website selbst haben wir vue.js verwendet.