---
 title: "Informationstheorie und Markov Modelle"
 date: 2017-07-29T00:00:00+02:00
 image: "509-sfi-update-week-2.jpg"
 summary: "Makromuster in Daten erkennen"
 author: "Ramona"
---


Systeme, so wird allgemein angenommen, durchlaufen verschiedene
Zustandsformen. Gesellschaften wechseln zwischen kooperativen und
konfliktreichen Perioden (z.B. Frieden vs. Bürgerkrieg), manche
Menschen verändern sich mental sehr stark (z.B. Depression), und
Klimaperioden wechseln sich ab. Diese Makromuster lassen sich oftmals
nicht direkt aus den sichtbaren Verhaltensweisen der Systemkomponenten
ableiten. Zum Beispiel kann sich eine Gesellschaft trotz mehrerer
Hauseinbrüche noch stets in einer kooperativen Periode befinden.
Neuronenaktivität von depressiven Menschen kann der von
fröhlichen Menschen gleichen und während einer Warmperiode kann
auch verstärkt Schnee fallen. Je nach Forschungsgebiet werden diese
Makromuster als Phasen, Epochen, Regime oder Zustände bezeichnet.
Gemeint ist immer dasselbe.

In diesem Artikel lernen wir, wie wir mithilfe von Informationstheorie
Grenzen zwischen verschiedenen Makromustern eines Systems erkennen
können. Warum ist das sinnvoll? Sobald wir wissen, wo Grenzen
zwischen Regimen verlaufen, können wir herausfinden, warum sie
entstehen und wie wir sie kontrollieren können. Zuerst stürzen
wir uns in die Theorie und danach befassen wir uns mit der Praxis.

Informationstheorie ist ein Bereich der Wahrscheinlichkeitstheorie und
Statistik, welche beschreibt, wie Systeme Informationen speichern und
bearbeiten. Informationen bezeichnen hier die Unsicherheit des Systems,
sich in einem bestimmten Zustand zu befinden. Wie unsicher bin ich mir,
dass es heute regnet? Diese Unsicherheit wird durch das Konzept Entropie
ausgedrückt. Je größer die Entropie, desto unsicherer sind
wir uns, in welchem Zustand sich das System befindet. Was den
Wetterzustand betrifft, so haben die Tropen eine geringere Entropie als
die gemäßigte Klimazone in Europa. Denn in den Tropen ist das
Wetter immer gleich, aber in Europa ändert es sich mit den
Jahreszeiten. In Europa fällt es uns demnach schwerer anzugeben, wie
das Wetter heute wird, bevor wir aus dem Fenster oder auf unsere
Wetterapp geschaut haben.

Mithilfe von Markov-Modellen können wir beschreiben, wie sich das
System durch den Zustandsraum bewegt. Dies ist ein erfundener Raum, der
alle Zustände umfasst, in denen sich das System befinden kann. Zu
jedem Zeitpunkt wählt das System einen Zustand abhängig von
vorangegangen Zuständen. Mithilfe dieser alten Trajekte im
Zustandsraum können neue Zustände des Systems vorhergesagt
werden, da alte und zukünftige Zustände Information teilen. Die
Zustände im Zustandsraum sind für uns nicht direkt sichtbar und
heißen daher interne oder versteckte Zustände. Wir haben es
hier mit einem Hidden Markov-Modell (HMM) zu tun. Jeder dieser internen
Zustände ist mit einem externen Zustand verbunden. Dies ist der
Systemoutput, den wir messen können. Das heißt, sobald sich das
System in einem internen Zustand befindet, sehen wir das System in dem
zugehörigen externen Zustand (siehe Abbildung 1).


{{< image-subtitle
    image="509_state_space.jpg"
>}}
Abbildung 1: Ein System im Zustandsraum. Zu jedem Zeitpunkt befindet sich das
System in einem anderen internen Zustand.
{{< /image-subtitle >}}


Betrachten wir das Ganze anhand eines Beispiels: Stellen wir uns die
Autorengemeinde einer Wikipedia-Seite als System vor (DeDeo, 2016). Wenn
ein Autor eine Wikipedia-Seite bearbeitet (Text hinzufügen oder
löschen), können andere Autoren diese Aktion entweder
akzeptieren oder umkehren und somit den Artikel zu einer früheren
Form zurückkehren. Dies ist das für uns unmittelbar messbare
Verhalten des Systems: eine Zeitreihe von
Akzeptieren-/Umkehren-Aktionen. Das System hat demnach zwei externe
Zustände. Die Anzahl der internen Zustände kennen wir
zunächst nicht. Die Bewegungen des Systems im internen Zustandsraum
geben uns Aufschluss über Makromuster des Systems. Im
Wikipedia-Beispiel wären das beispielsweise kooperative und
konfliktreiche Perioden (auf die Wahl und Interpretation der
Makrozustände kommen wir später zurück).

Nach dieser Theorieeinheit sind wir nun gewappnet für die Praxis.
Wie finden wir ein passendes HMM, um Makromuster aus unserem Datensatz
zu erkennen? Es gibt viele stand-alone Open-Source-Softwares oder
Packages für Programmiersprachen, die anhand eines Datensatzes das
passende HMM für uns berechnen. Da wir das Rad nicht neu erfinden
möchten, ist es sicherlich sinnvoll diese vorhandene Software zu
nutzen. Allerdings ist es ebenso sinnvoll, mit den zugrundeliegenden
Konzepten und Berechnungen vertraut zu sein.

Im ersten Schritt ermitteln wir mithilfe des
Akaike-Informationskriteriums die beste Anzahl der internen Zustände
und deren übergangswahrscheinlichkeiten (mit welcher
Wahrscheinlichkeit p wechselt das System vom Zustand x in den Zustand
y). Somit erhalten wir das optimale HMM. Das
Akaike-Informationskriterium (AIK) vergleicht verschiedene HMM, d.h.
Wahrscheinlichkeitsverteilungen der internen Zustände. Für jeden
internen Zustand im Zustandsraum stellen wir die Frage wie
wahrscheinlich es ist, dass sich das System in einem dieser Zustände
befindet. Das Modell, das relativ gesehen den geringsten
Informationsverlust hat, um das echte System darzustellen, wird
ausgewählt. Abbildungen 2 und 3 zeigen jeweils Beispiele einer
Wahrscheinlichkeitsverteilung und einer übergangsmatrix.


{{< image-subtitle
    image="509_trannsition_matrix.jpg"
>}}
Abbildung 2: Beispiel einer Übergangsmatrix.
{{< /image-subtitle >}}

{{< image-subtitle
    image="509_probability_distribution.jpg"
>}}
Abbildung 3: Eine Häufigkeitsverteilung (links) kann anhand des
Datensatzes ermittelt werden. Daraus ergibt sich eine
Wahrscheinlichkeitsverteilung (rechts).
{{< /image-subtitle >}}

Um das AIK zu berechnen, generieren wir zunächst eine Anzahl von
Test-HMMs. Für jedes dieser HMMs berechnen wir die Maximum
Likelihood &Lcirc des Modells:

{{< image 
    image="509_L_max.png"
>}}
L MAX
{{< /image >}}

{{< image 
    image="509_explanation_L_max.png"
>}}
L MAX Explanation
{{< /image >}}

Danach berechnen wir das AIC:

{{< image 
    image="509_AIC.png"
>}}
AIC
{{< /image >}}

{{< image 
    image="509_explanation_AIC.png"
>}}
AIC Explanation
{{< /image >}}


Von allen Test-HMM wählen wir jenes als optimale Lösung, welches
das AIC minimiert.

Im zweiten Schritt berechnen wir die Viterbi-Pfadrekonstruktion, um die
zeitliche Abfolge der internen Zustände des Systems zu finden.
Abhängig vom optimalen HMM und unserem Datensatz ermittelt die
Viterbi-Pfadrekonstruktion den wahrscheinlichsten Pfad des Systems im
internen Zustandsraum. Somit wissen wir, in welchem Zustand sich das
System zu jedem Zeitpunkt mit der größten Wahrscheinlichkeit
befindet.

Die Berechnungen für die Viterbi-Pfadrekonstruktion beruhen auf
einem Annäherungswert, dessen Genauigkeit von der Anzahl der
verwendeten Eigenvektoren der übergangsmatrix abhängt. Die
übergangsmatrix erhalten wir durch das AIK. Die Anzahl ihrer
Eigenvektoren ist gleich der Anzahl ihrer Reihen oder Spalten (die
übergangsmatrix ist quadratisch), d.h. gleich der Anzahl der
internen Zustände des HMM.

{{< image 
    image="509_Viterbi.png"
>}}
Viterbi
{{< /image >}}

{{< image 
    image="509_explanation_Viterbi.png"
>}}
Viterbi Explanation
{{< /image >}}

Im dritten und letzten Schritt verwenden wir die Struktur der
Eigenvektoren der übergangsmatrix, um Makromuster zu erkennen. Der
zweite Eigenvektor der übergangsmatrix beschreibt die Störungen
(Perturbationen), die am längsten brauchen, um abzuebben. Das
heißt, das System balanciert sich letztendlich in einem
Gleichgewichtszustand. Dieser Gleichgewichtszustand ist eines der
unterliegenden Makromuster nach denen wir suchen. Abhängig vom Plus-
oder Minuszeichnen der Eigenvektorkomponenten teilen wir das System in
zwei Teilräume. Nehmen wir beispielsweise an, dass unser optimales
HMM fünf interne Zustände hat und der zweite Eigenvektor der
zugehörigen übergangsmatrix \[-2, -5, 6, -4, 5\] lautet. Dann
wissen wir, dass die internen Zustände 1, 2 und 4 zum ersten
Teilraum zugeordnet werden können und die Zustände 3 und 5 zum
zweiten. Falls wir unser System in mehr als zwei Teilräume aufteilen
möchten, müssen wir die Zeichenanalyse mit höhergradigen
Eigenvektoren durchführen. Auf diese Weise werden unsere zwei
Teilräume hierarchisch zerlegt und Substrukturen in den zwei
Teilräumen werden sichtbar. Mit dieser Methode können wir alle
internen Zustände Teilräumen zuordnen.

Es ist wichtig zu wissen, dass menschliches Denkvermögen
unerlässlich ist, um die Bedeutung dieser Teilräume zu
interpretieren. Der Computer liefert uns nur die Struktur der
Teilräume. Ob sie nun kooperativen und konfliktreichen Perioden,
verschiedenen emotionalen Zuständen oder Klimaperioden entsprechen,
müssen wir selbst entscheiden.

In diesem Artikel haben wir eine kleine übersicht über
Informationstheorie und Hidden Markov-Models erhalten. Wir haben
gelernt, diese Methoden auf echte Datensätze anzuwenden, um
unterliegende Makromuster in Daten und ihren zugehörigen Systemen zu
erkennen.

### Bibliographie

**DeDeo, S. (2016):** Conflict and Computation on Wikipedia: A
Finite-State Machine Analysis of Editor Interactions. Future Internet
8(3), 31; doi:10.3390/fi8030031.

------------------------------------------------------------------------


