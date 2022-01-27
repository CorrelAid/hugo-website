---
title: "Die Visualisierung von Wahlumfrageergebnissen"
date: 2017-09-20T00:00:00+02:00
image: "509-graphical-perception-political-polls.jpg"
summary: "Wie stellen wir Wahlumfragen am Verständlichsten dar?"
categories:       
    - Bundestagswahl 2017
author: 
    name:           "Richard Traunmüller"
    image:          "richard-traunmueller.jpg"
    description:    "I am a Visiting Professor of Quantitative Methods in the Social and Behavioral Sciences at the University of Mannheim and currently on leave from Goethe University Frankfurt, where I hold an Assistant Professorship for Empirical Democracy Research. My work on religion and politics and quantitative methodology has been published in Comparative Political Studies, Comparative Politics, European Journal of Political Research, European Sociological Review, and Political Analysis, amongst others. Please feel free to contact me via Mail. "
    twitter:        ""
    facebook:       ""
    github:         ""
    email:          "traunmueller@soz.uni-frankfurt.de"
    website:        ""
meta:
    title: "CorrelAid - Die Visualisierung von Wahlumfrageergebnissen"
    description: "Wahlumfragen sind wichtige politische Informationsquellen und bedeutende
                  Werkzeuge der politischen Selbstbeobachtung. Damit sie diesen Zweck aber
                  auch erfüllen, kommt es darauf wie ihre Ergebnisse kommuniziert werden."
    image: "509-graphical-perception-political-polls.jpg"
    keywords: "CorrelAid, Data4Good, Polls, Wahlumfragen, politische Selbstbeobachtung, Graphical Perception"
---


Wahlumfragen sind wichtige politische Informationsquellen und bedeutende
Werkzeuge der politischen Selbstbeobachtung. Damit sie diesen Zweck aber
auch erfüllen, kommt es darauf wie ihre Ergebnisse kommuniziert werden.
Visualisierungen gehören zu den einfachsten und zugleich mächtigsten
Werkzeugen statistische Sachverhalte verständlich zu machen. Wie sollen
wir Wahlumfrageergebnisse also graphisch darstellen, damit sie Bürger,
Journalisten und Politexperten am besten verstehen?

### Sind *dot plots* besser als Balkendiagramme? {#sind-dot-plots-besser-als-balkendiagramme-}

Die klassische Studie Graphical Perception von Cleveland und McGill
(1984) war die erste, welche die Effektivität verschiedener
Graphikformate systematisch untersucht hat. Im Rahmen ihrer Experimente
kamen sie zu einem einflussreichen Ranking visueller Objekte: so sei
etwa „Position entlang einer gemeinsamen Skala“ eine akkuratere Methode
quantitative Werte in visuelle Objekte zu übersetzen, als „Länge“. Viele
interpretieren dieses Resultat dahingehend, dass *dot plots* einem
Balkendiagramm vorzuziehen sind, etwa wenn man die Wähleranteile der
Parteien darstellen möchte. Es ist richtig, dass Cleveland selbst *dot
plots* präferiert. Doch kurioserweise waren *dot plots* nie teil des
klassischen Experiments – diese Präferenz ist somit unbegründet und das
empirische Verdikt steht bislang noch aus. (Dass dies bislang niemandem
aufgefallen zu sein scheint, sagt für sich genommen bereits einiges über
unseren Wissensstand aus. Doch das ist ein anderes Thema und soll ein
anderes Mal erläutert werden.)

### Sind Liniendiagramme besser als Balkendiagramme? {#sind-liniendiagramme-besser-als-balkendiagramme-}

Die bestehende Orthodoxie kategoriale Gruppenvergleiche mit
Balkendiagrammen vorzunehmen wurde vor kürzerer Zeit aber auch von
einigen anderen Visualisierungsexperten in Frage gestellt (Gelman 2010,
Fung 2005, 2010). Sie machen sich stattdessen für die Verwendung von
Liniendiagrammen stark, die ansonsten eigentlich für die Visualisierung
von Zeittrends vorgesehen sind. Genau wie bei *dot plots* kann bei
Liniendiagrammen die Y-Achse über der Null beginnen, was den visuellen
Vergleich kleiner Differenzen erleichtert. Bei Balkendiagrammen würde
dies eine Verzerrung des visuellen Eindrucks bedeuten. Wichtiger ist
jedoch, dass Liniendiagramme den Gruppenvergleich erleichtern, da die
Linien die zu vergleichenden Werte direkt miteinander verbinden und
damit der natürlichen Augenbewegung folgen und diese unterstützen. Dies
scheint insbesondere nützlich, wenn man zwei kategoriale Variablen
gleichzeitig vergleichen möchte: etwa die wahrgenommene Kompetenz der
Parteien in verschiedenen Politikbereichen.

{{< image-subtitle
    image="509-blogpost-fig3.png"
>}}
Abbildung 1: Balkendiagramm, *Dot Plot* und Liniendiagramm im Vergleich.
{{< /image-subtitle >}}


### Neue experimentelle Evidenz

Mein Kollege Felix Jäger und ich haben nun in einer Reihe von
crowd-sourced Experimenten zur Visualisierung von Wahlumfrageergebnissen
einige überraschende Entdeckungen gemacht: Tatsächlich ist das einfache
Balkendiagramm sowohl dem *dot plot* als auch einem Liniendiagramm
überlegen, wenn es darum geht die Ergebnisse politischer Umfragen zu
visualisieren und etwa Parteien miteinander zu vergleichen. Unsere
Probanden machten weniger Fehler und kamen schneller zu ihren Schlüssen.
Dies mag zunächst als wenig überraschend erscheinen – schließlich sind
Balkendiagramme die verbreitetste Visualisierungsmethode zur Darstellung
von Wahlumfrageergebnissen. Doch lässt sich aus der Verbreitung einer
Methode nur schlecht auch auf deren Effektivität schließen. Das
verbreitete, aber defizitäre Kuchendiagramm ist hier ein mahnendes
Beispiel.

Der Befund ist aber insbesondere deshalb bemerkenswert, weil er sowohl
verbreiteten Vorstellungen als auch neuen Vorschlägen von
Visualisierungsprofis widerspricht. Wir vermuten, dass sich der Vorteil
des einfachen Balkendiagramms auf dessen Bekanntheit zurückführen lässt:
die meisten Menschen kennen dieses Graphikformat und wissen wie es zu
verstehen ist. Dies verdeutlicht einen ganz zentralen Punkt: gute
Datenvisualisierung berücksichtigt stets das Zielpublikum. Ein weiterer
wichtiger Punkt der sich aus unseren Ergebnissen lernen lässt, ist dass
man Klassikern und vermeintlichen Standards der Datenvisualisierung
nicht blind folgen, sondern diese in konkreten Anwendungen experimentell
evaluieren sollte. Wir hoffen jedenfalls schon bald neue Erkenntnisse
zur angemessenen Visualisierung politisch relevanter Daten liefern zu
können.

### Literaturhinweise

-   Cleveland, Wiliam S. und McGill, Robert (1984): Graphical
    Perception: Theory, Experimentation, and Application to the
    Development of Graphical Methods. In: Journal of the American
    Statistical Association Vol. 79 (No. 387), pp. 531–554.
-   Fung, Kaiser (2005): On the popularity of bar charts.
    <http://junkcharts.typepad.com/junk_charts/2005/11/on_the_populari.html>
-   Fung, Kaiser (2010): Answering an open call.
    <http://junkcharts.typepad.com/junk_charts/2010/09/answering-an-open-call.html>
-   Gelman, Andrew (2010): Here’s how rumors get started: Lineplots,
    *dotplots*, and nonfunctional modernist architecture.
    <http://andrewgelman.com/2010/09/08/heres_how_rumor/>
-   Jäger, Felix und Traunmüller, Richard (2017): Graphical Perception
    of Political Polls. Unveröffentlichtes Manuskript. Goethe
    Universität Frankfurt.

------------------------------------------------------------------------


