---
 title: "Informations-theorie und Markov Modelle"
 date: 2017-07-29T00:00:00+02:00
 image: sfi-3.jpg
 summary: "Makromuster in Daten erkennen"
 author: "Ramona"
---


Systeme, so wird allgemein angenommen, durchlaufen verschiedene
Zustandsformen. Gesellschaften wechseln zwischen kooperativen und
konfliktreichen Perioden (z.B. Frieden vs. B&uumlrgerkrieg), manche
Menschen ver&aumlndern sich mental sehr stark (z.B. Depression), und
Klimaperioden wechseln sich ab. Diese Makromuster lassen sich oftmals
nicht direkt aus den sichtbaren Verhaltensweisen der Systemkomponenten
ableiten. Zum Beispiel kann sich eine Gesellschaft trotz mehrerer
Hauseinbr&uumlche noch stets in einer kooperativen Periode befinden.
Neuronenaktivit&aumlt von depressiven Menschen kann der von
fr&oumlhlichen Menschen gleichen und w&aumlhrend einer Warmperiode kann
auch verst&aumlrkt Schnee fallen. Je nach Forschungsgebiet werden diese
Makromuster als Phasen, Epochen, Regime oder Zust&aumlnde bezeichnet.
Gemeint ist immer dasselbe.

In diesem Artikel lernen wir, wie wir mithilfe von Informationstheorie
Grenzen zwischen verschiedenen Makromustern eines Systems erkennen
k&oumlnnen. Warum ist das sinnvoll? Sobald wir wissen, wo Grenzen
zwischen Regimen verlaufen, k&oumlnnen wir herausfinden, warum sie
entstehen und wie wir sie kontrollieren k&oumlnnen. Zuerst st&uumlrzen
wir uns in die Theorie und danach befassen wir uns mit der Praxis.

Informationstheorie ist ein Bereich der Wahrscheinlichkeitstheorie und
Statistik, welche beschreibt, wie Systeme Informationen speichern und
bearbeiten. Informationen bezeichnen hier die Unsicherheit des Systems,
sich in einem bestimmten Zustand zu befinden. Wie unsicher bin ich mir,
dass es heute regnet? Diese Unsicherheit wird durch das Konzept Entropie
ausgedr&uumlckt. Je gr&ouml&szliger die Entropie, desto unsicherer sind
wir uns, in welchem Zustand sich das System befindet. Was den
Wetterzustand betrifft, so haben die Tropen eine geringere Entropie als
die gem&auml&szligigte Klimazone in Europa. Denn in den Tropen ist das
Wetter immer gleich, aber in Europa &aumlndert es sich mit den
Jahreszeiten. In Europa f&aumlllt es uns demnach schwerer anzugeben, wie
das Wetter heute wird, bevor wir aus dem Fenster oder auf unsere
Wetterapp geschaut haben.

Mithilfe von Markov-Modellen k&oumlnnen wir beschreiben, wie sich das
System durch den Zustandsraum bewegt. Dies ist ein erfundener Raum, der
alle Zust&aumlnde umfasst, in denen sich das System befinden kann. Zu
jedem Zeitpunkt w&aumlhlt das System einen Zustand abh&aumlngig von
vorangegangen Zust&aumlnden. Mithilfe dieser alten Trajekte im
Zustandsraum k&oumlnnen neue Zust&aumlnde des Systems vorhergesagt
werden, da alte und zuk&uumlnftige Zust&aumlnde Information teilen. Die
Zust&aumlnde im Zustandsraum sind f&uumlr uns nicht direkt sichtbar und
hei&szligen daher interne oder versteckte Zust&aumlnde. Wir haben es
hier mit einem Hidden Markov-Modell (HMM) zu tun. Jeder dieser internen
Zust&aumlnde ist mit einem externen Zustand verbunden. Dies ist der
Systemoutput, den wir messen k&oumlnnen. Das hei&szligt, sobald sich das
System in einem internen Zustand befindet, sehen wir das System in dem
zugeh&oumlrigen externen Zustand (siehe Abbildung 1).

\
![](1_state%20space.jpg){.img-responsive}*Abb.
1: Ein System im Zustandsraum. Zu jedem Zeitpunkt befindet sich das
System in einem anderen internen Zustand.*\
\
Betrachten wir das Ganze anhand eines Beispiels: Stellen wir uns die
Autorengemeinde einer Wikipedia-Seite als System vor (DeDeo, 2016). Wenn
ein Autor eine Wikipedia-Seite bearbeitet (Text hinzuf&uumlgen oder
l&oumlschen), k&oumlnnen andere Autoren diese Aktion entweder
akzeptieren oder umkehren und somit den Artikel zu einer fr&uumlheren
Form zur&uumlckkehren. Dies ist das f&uumlr uns unmittelbar messbare
Verhalten des Systems: eine Zeitreihe von
Akzeptieren-/Umkehren-Aktionen. Das System hat demnach zwei externe
Zust&aumlnde. Die Anzahl der internen Zust&aumlnde kennen wir
zun&aumlchst nicht. Die Bewegungen des Systems im internen Zustandsraum
geben uns Aufschluss &uumlber Makromuster des Systems. Im
Wikipedia-Beispiel w&aumlren das beispielsweise kooperative und
konfliktreiche Perioden (auf die Wahl und Interpretation der
Makrozust&aumlnde kommen wir sp&aumlter zur&uumlck).

Nach dieser Theorieeinheit sind wir nun gewappnet f&uumlr die Praxis.
Wie finden wir ein passendes HMM, um Makromuster aus unserem Datensatz
zu erkennen? Es gibt viele stand-alone Open-Source-Softwares oder
Packages f&uumlr Programmiersprachen, die anhand eines Datensatzes das
passende HMM f&uumlr uns berechnen. Da wir das Rad nicht neu erfinden
m&oumlchten, ist es sicherlich sinnvoll diese vorhandene Software zu
nutzen. Allerdings ist es ebenso sinnvoll, mit den zugrundeliegenden
Konzepten und Berechnungen vertraut zu sein.

Im ersten Schritt ermitteln wir mithilfe des
Akaike-Informationskriteriums die beste Anzahl der internen Zust&aumlnde
und deren &uumlbergangswahrscheinlichkeiten (mit welcher
Wahrscheinlichkeit p wechselt das System vom Zustand x in den Zustand
y). Somit erhalten wir das optimale HMM. Das
Akaike-Informationskriterium (AIK) vergleicht verschiedene HMM, d.h.
Wahrscheinlichkeitsverteilungen der internen Zust&aumlnde. F&uumlr jeden
internen Zustand im Zustandsraum stellen wir die Frage wie
wahrscheinlich es ist, dass sich das System in einem dieser Zust&aumlnde
befindet. Das Modell, das relativ gesehen den geringsten
Informationsverlust hat, um das echte System darzustellen, wird
ausgew&aumlhlt. Abbildungen 2 und 3 zeigen jeweils Beispiele einer
Wahrscheinlichkeitsverteilung und einer &uumlbergangsmatrix.

\
![](2_trannsition%20matrix.jpg){.img-responsive}
*Abb. 2: Beispiel einer &Uumlbergangsmatrix.*\
\
![](3_probability%20distribution.jpg){.img-responsive}
*Abb. 3: Eine H&aumlufigkeitsverteilung (links) kann anhand des
Datensatzes ermittelt werden. Daraus ergibt sich eine
Wahrscheinlichkeitsverteilung (rechts).*\
\
Um das AIK zu berechnen, generieren wir zun&aumlchst eine Anzahl von
Test-HMMs. F&uumlr jedes dieser HMMs berechnen wir die Maximum
Likelihood &Lcirc des Modells:

\
![](4_L_max.png){.img-responsive}\
![](5_explanation%20L_max.png){.img-responsive}\
Danach berechnen wir das AIC:

\
![](6_AIC.png){.img-responsive}\
![](7_explanation%20AIC.png){.img-responsive}\
Von allen Test-HMM w&aumlhlen wir jenes als optimale L&oumlsung, welches
das AIC minimiert.

Im zweiten Schritt berechnen wir die Viterbi-Pfadrekonstruktion, um die
zeitliche Abfolge der internen Zust&aumlnde des Systems zu finden.
Abh&aumlngig vom optimalen HMM und unserem Datensatz ermittelt die
Viterbi-Pfadrekonstruktion den wahrscheinlichsten Pfad des Systems im
internen Zustandsraum. Somit wissen wir, in welchem Zustand sich das
System zu jedem Zeitpunkt mit der gr&ouml&szligten Wahrscheinlichkeit
befindet.

Die Berechnungen f&uumlr die Viterbi-Pfadrekonstruktion beruhen auf
einem Ann&aumlherungswert, dessen Genauigkeit von der Anzahl der
verwendeten Eigenvektoren der &uumlbergangsmatrix abh&aumlngt. Die
&uumlbergangsmatrix erhalten wir durch das AIK. Die Anzahl ihrer
Eigenvektoren ist gleich der Anzahl ihrer Reihen oder Spalten (die
&uumlbergangsmatrix ist quadratisch), d.h. gleich der Anzahl der
internen Zust&aumlnde des HMM.

\
![](8_Viterbi.png){.img-responsive}\
![](9_explanation%20Viterbi.png){.img-responsive}\
Im dritten und letzten Schritt verwenden wir die Struktur der
Eigenvektoren der &uumlbergangsmatrix, um Makromuster zu erkennen. Der
zweite Eigenvektor der &uumlbergangsmatrix beschreibt die St&oumlrungen
(Perturbationen), die am l&aumlngsten brauchen, um abzuebben. Das
hei&szligt, das System balanciert sich letztendlich in einem
Gleichgewichtszustand. Dieser Gleichgewichtszustand ist eines der
unterliegenden Makromuster nach denen wir suchen. Abh&aumlngig vom Plus-
oder Minuszeichnen der Eigenvektorkomponenten teilen wir das System in
zwei Teilr&aumlume. Nehmen wir beispielsweise an, dass unser optimales
HMM f&uumlnf interne Zust&aumlnde hat und der zweite Eigenvektor der
zugeh&oumlrigen &uumlbergangsmatrix \[-2, -5, 6, -4, 5\] lautet. Dann
wissen wir, dass die internen Zust&aumlnde 1, 2 und 4 zum ersten
Teilraum zugeordnet werden k&oumlnnen und die Zust&aumlnde 3 und 5 zum
zweiten. Falls wir unser System in mehr als zwei Teilr&aumlume aufteilen
m&oumlchten, m&uumlssen wir die Zeichenanalyse mit h&oumlhergradigen
Eigenvektoren durchf&uumlhren. Auf diese Weise werden unsere zwei
Teilr&aumlume hierarchisch zerlegt und Substrukturen in den zwei
Teilr&aumlumen werden sichtbar. Mit dieser Methode k&oumlnnen wir alle
internen Zust&aumlnde Teilr&aumlumen zuordnen.

Es ist wichtig zu wissen, dass menschliches Denkverm&oumlgen
unerl&aumlsslich ist, um die Bedeutung dieser Teilr&aumlume zu
interpretieren. Der Computer liefert uns nur die Struktur der
Teilr&aumlume. Ob sie nun kooperativen und konfliktreichen Perioden,
verschiedenen emotionalen Zust&aumlnden oder Klimaperioden entsprechen,
m&uumlssen wir selbst entscheiden.

In diesem Artikel haben wir eine kleine &uumlbersicht &uumlber
Informationstheorie und Hidden Markov-Models erhalten. Wir haben
gelernt, diese Methoden auf echte Datens&aumltze anzuwenden, um
unterliegende Makromuster in Daten und ihren zugeh&oumlrigen Systemen zu
erkennen.

### Bibliographie

**DeDeo, S. (2016):** Conflict and Computation on Wikipedia: A
Finite-State Machine Analysis of Editor Interactions. Future Internet
8(3), 31; doi:10.3390/fi8030031.

------------------------------------------------------------------------


