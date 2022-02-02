---
title: 'What''s out there? #2'
date: '2017-08-19T00:00:00+02:00'
image: 509-whats-out-there.jpg
summary: Wissenswertes aus der Data Science-Welt.
categories:
- Data Science
- What's out there
author:
  name: Marcus
  image: marcus-s.jpg
  description: Marcus Seuser studierte Geographie und Geoinformatik an den Universitäten
    Leipzig und Tübingen. Sein Studienschwerpunkt war die Einbindung von Methoden
    der Geoinformatik in der Humangeographie, wobei er sich mit Modellierung von Städtewachstum
    und der Vorhersage von Bürgerkriegsrisiken beschäftigt hat. Er arbeitet hauptberuflich
    als Datenanalyst für die Managementberatung conmobility und ist externer Mitarbeiter
    der Universität Frankfurt im Fachbereich Humangeographie.
  twitter: ''
  facebook: https://www.facebook.com/https://de-de.facebook.com/Mogli.Marcus
  github: ''
  email: marcus.seuser@gmx.de
  website: ''
meta:
  title: 'CorrelAid - What''s out there? #1'
  description: Die meisten Menschen, die sich mit Daten beschäftigen, haben schon
    von der Faustregel gehört, dass sich das Datenvolumen etwa alle zwei Jahre verdoppelt.
    Wir haben es hier also mit exponentiellem Wachstum zu tun, und ähnlich verhält
    es sich auch mit Informationen rund um Data Science, Algorithmen, Programmiersprachen
    und Anwendungsfällen.
  image: 509-whats-out-there.jpg
  keywords: CorrelAid, whats out there?, Data Scientist, Visualisierungen, ML -Konzepte
    & Algorithmen
slug: whats-out-there-2
---

Von der Faustregel, dass sich das Datenvolumen etwa alle zwei Jahre
verdoppelt, haben die meisten Menschen, die sich mit Daten beschäftigen,
vermutlich schon gehört. Wir haben es hier mit exponentiellem Wachstum
zu tun. Ganz ähnlich verhält es sich auch mit Informationen rund um Data
Science, Algorithmen, Programmiersprachen und ihren Anwendungsfällen. In
der alltäglichen Flut an interessanten und nützlichen Ressourcen kann
man schonmal die Orientierung verlieren. Aber nicht mit uns!

An dieser Stelle präsentiert Marcus Seuser jeden Monat sein Best-Of an
Ressourcen rund um Data Science. Für euch durchforstet er Blogs, Feeds,
Journalartikel und Podcasts, um mit euch am Puls der Community zu fühlen
und euch den Einstieg in die Welt der Data Science zu vereinfachen. Die
Beiträge sind thematisch geordnet und enthalten zu jedem der Unterpunkte
einige weiterführende Links.


### Data-Projects

#### 1. Good, Evil, Ugly, Beautiful: The Game of Thrones Chart {#1-good-evil-ugly-beautiful-the-game-of-thrones-chart}

Natürlich bleibt auch der Blog von Correlaid nicht unberührt vom
GoT-Hype der neuen Staffel. Die [New York
Times](https://www.nytimes.com/interactive/2017/08/09/upshot/game-of-thrones-chart.html)
liefert ein interessantes Beispiel, wie sich mit einer einfachen
Umfrage-Methode und Dichte-Visualisierung ein Thema leicht zugänglich
und zugleich spannend darstellen lässt. Interaktive Visualisierungen
lassen sich mit Plotly ebenfalls sowohl für R als auch Python erstellen,
wobei (meiner Meinung nach) Bokeh für Python hier der wahre Held vom
Erdbeerfeld ist. Ausprobieren!


### ML-Konzepte & Algorithmen & Programmiersprachen

#### 1. Understanding Support Vector Machine {#1-understanding-support-vector-machine}

Ganz ohne Mitglied der NSA zu sein, bilde ich mir ein, manche Leser\*innen
letzte Woche beim Lesen meines Artikels aufstöhnen gehört zu haben:
„Ahh, schon wieder diese Decision-Trees. Kann der Typ eigentlich nix
anderes?“ Kann er! Diese Woche geht’s um Support Vector Machines (SVM),
die eine großartige Alternative zu Decision-Tree-Ansätzen darstellen,
allerdings schwieriger zu interpretieren sind und mehr Parameter-Tuning
benötigen (aber irgendwie sind wir dafür ja auch da, oder?). Sadanand
Singh behandelt in seinem feinen Tutorial die Implementierung von SVM
mittels scikit-learn in Python. Wer also einen ersten Blick riskieren
will, möge
[hier](https://sadanand-singh.github.io/posts/svmpython/#disqus_thread)
klicken.


#### 2. Understanding empirical Bayes estimation {#2-understanding-empirical-bayes-estimation}

„Bayessche Statistik, ist das nicht so schwammig und ohne
Anwendungsbezug?“. Nachdem ich ähnliche Äußerungen in letzter Zeit
häufiger gehört habe (stark die Frequentalisten sind in meinem
Freundeskreis), breche ich in dieser und den nächsten Ausgaben dieser
Serie ein paar Lanzen für Anwendungen mit dem Satz von Bayes. Ich lasse
das Ritterturnier daher mit [Sir David
Robinson](http://varianceexplained.org/r/empirical_bayes_baseball/)
beginnen, welcher anhand von Baseball Statistiken die Grundzüge von
Schätzungen mit Bayes erklärt und dabei gleich noch die Grundlage für
das viel beschworene A/B Testing bereitstellt. Fight!


#### 3. The Bias-Variance Dilemma {#3-the-bias-variance-dilemma}

Die Meisten meiner Leser\*innen wissen vermutlich schon, was mit
*Bias-Variance Tradeoff* oder eben *Dilemma* gemeint ist. Oder doch nur
so ungefähr? Im Fall des Falles: Bitte lest [das
hier](https://ml.berkeley.edu/blog/2017/07/13/tutorial-4/)! Es handelt
sich um einen unendlich unterhaltsamen Blogbeitrag mit vielen, teilweise
interaktiven Abbildungen und sogar ein paar Memes für die Digital
Natives unter uns. Ich konnte einfach nicht widerstehen.


#### 4. Tidyverse (von Frierike Preu) {#4-tidyverse-von-frierike-preu-}

Eine Masterarbeit, die ist lustig, eine Masterarbeit, die ist schön –
naja. In meinem Fall immerhin eine gute Gelegenheit, a) viel R Code zu
schreiben, b) viel zu prokrastinieren und c) mit meinen Kommiliton\*innen
über die neusten Features des Tidyverse abzunerden. Wenn es da bei euch
jetzt nicht klingelt, empfehle ich [„R for Data
Science“](http://r4ds.had.co.nz/), die [„tidy data“
Vignette](https://cran.r-project.org/web/packages/tidyr/vignettes/tidy-data.html)
oder zum Überblick [tidyverse.org](tidyverse.org). Für alle anderen zwei
Dinge, die ich in den letzten Wochen besonders spannend fand:

1.  Package
    [tidygraph](https://cran.r-project.org/web/packages/tidygraph/):
    tidy Netzwerkdaten heißt ein data frame für Kanten (Edges) und einer
    für Knoten (Nodes), sinnvolle Wrapperfunktionen, einheitliche
    Funktionsnamen und ultimative Pipe-Kompatibilität. Eine Einführung
    vom Autor gibt es
    [hier](http://www.data-imaginist.com/2017/Introducing-tidygraph/).
2.  Programming with dplyr: Es gibt nichts Schlimmeres in R (neben
    fehlenden Leerzeichen vor und hinter "&lt;" ;) ), als eine schöne
    Pipe Chain unterbrechen zu müssen, weil die eigens geschriebene
    Funktion nicht dplyr/Pipe kompatibel ist. [Dieser
    Artikel]((http://dplyr.tidyverse.org/articles/programming.html) gibt
    eine erste Einführung in die Programmierung mit dplyr - angereichert
    mit vielen Beispielen, die leicht auf die eigenen Probleme
    übertragbar sind.


### Ich und die Anderen

#### 1. Ich – Eigene Projekte für den Lebenslauf {#1-ich-eigene-projekte-f-r-den-lebenslauf}

Es wurde uns schon hundertmal gesagt, hier noch einmal zum Mitschreiben:
Data Scientist sind gesuchte Leute! Weniger häufig allerdings wird
angefügt, dass das Wörtchen „erfahrene“ dabei auch seine Rolle spielt.
Wie aber zu Erfahrung kommen, wenn man noch keinen Job hat? Das
Zauberwort heißt „Resume Projects“. Ergo Projekte, die man in seiner
Freizeit oder während des Studiums entwirft, bestenfalls mit einem
Thema, für das man brennt und an dem man seine technischen Talente
beweisen kann. Wer hierfür noch Ideen sucht möge einmal
[hier](https://blog.statsbot.co/data-scientist-resume-projects-806a74388ae6)
schauen.


#### 2. Die Anderen – Hörenswerte Data Science Podcasts {#2-die-anderen-h-renswerte-data-science-podcasts}

Data Science für alle Sinne. So will ich am Ende dieser Zeilen nun neben
euren Augen auch eure Ohren in Beschlag nehmen. Das Team von Byte
Academy hat eine [Liste der besten
Podcasts](http://byteacademy.co/blog/data-science-podcasts) zum Thema
Data Science zusammengestellt. Die Auswahl kommt dazu immer mit einem
kleinen Hörerprofil, so findet ihr gleich euren neuen Favoriten. Augen
zu und Ohren auf!

------------------------------------------------------------------------



