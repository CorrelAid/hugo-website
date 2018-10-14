---
 title: "Komplexit�t in nicht-linearen und chaotischen Systemen"
 date: NA
 image: /images/blog/sfi-2.jpg
 summary: ""
 author: "Ramona"
---


> Was sind nicht-liniäre dynamische Systeme?\
> Was ist der Unterschied zwischen analytischen und numerischen
> Methoden?\
> Wie kann ich meinen Datensatz mit nicht-liniären Methoden
> analysieren?\

Nach zwei Wochen Summerschool in Santa Fe nehme ich meine Umgebung
ausschließlich als Ansammlung von Systemen war. Ob Luftmoleküle,
Menschen oder die Sterne am Himmel, Systemkomponenten sind in ständiger
Interaktion untereinander und mit ihrer Umgebung. Hierbei entstehen
Makromuster wie zum Beispiel das Wetter, Freundschaften oder
Sonnensysteme/Schwerkraft. Viele dieser Systeme sind im ständigen Wandel
und Dynamik, ein Zweig der Mathematik, analysiert wie sich diese Systeme
zeitlich verändern.

Als Datenanalysten haben wir meist keinen vollständigen Zugang zum
System. Im günstigsten Fall kennen wir die Parameter, die das System
beeinflussen und können aus der Literatur Zusammenhänge zwischen ihnen
herstellen. Wir erstellen ein System aus Differentialgleichungen,
welches die Veränderungen in jenen Parametern ausdrückt und diese
zueinander in Beziehung setzt. Zum Beispiel, beschreibt das SIR-Modell
aus der Epidemiologie wie sich die Anzahlen von anfälligen
(susceptibles), infizierten (infected) und genesenden (recovered)
Personen zeitlich zu einander verhalten.

\
$$\frac{\delta S}{\delta t} = \frac{\beta IS}{N}$$\
$$\frac{\delta I}{\delta t} = \frac{\beta IS}{N} - \gamma I$$\
$$\frac{\delta R}{\delta t} = \gamma I$$\
Im schlechtesten Fall, kennen wir die Parameter und deren Zusammenhänge
nicht. Wir erhalten jediglich einen kleinen Ausschnitt in Form von
Messdaten und müssern daraus ableiten, welche Prozesse im System von
statten gehen.

In beiden Fällen ist es wichtig zunächst die Dynamik des Systems näher
zu karakterisieren. Dadurch können wir die richtige Analysemethode
wählen und feststellen inwiefern Vorhersagen über die Zukunft des
Systems möglich sind. Wir unterscheiden zwischen liniären und
nicht-liniären Systemen, wobei letztere noch die Unterkategorie
chaotische Systeme enthalten (siehe Abbildung 1).

![](/images/blog/sfi-circles.jpg){.img-responsive}*Abbildung
1: Systemkategorien*\
\
### Liniäre dynamische Systeme

In liniäre dynamische Systemen gibt es keine Interaktionen zwischen
Systemkomponenten. Durch diese Unabhängigkeit erhalten wir eine kostante
Wachstumsrate im System. Beispiel hierfür ist eine Bakterienkolonie.
Durch asexuelle Reproducktion (jedes Bakterium teilt sich in zwei) sind
die Bakterien unabhängig voneinander und die Kolonie wächst
exponentiell. Die entsprechende Diffenrentialgleichung lautet:

\
$$\frac{\delta y(t)}{\delta t} = ky(t)$$\
y: Koloniegröße, k: Wachstumsrate, t: Zeit.

Diese hat eine analytische Lösung. Das heißt, wir können eine Funktion
y(t) finden, die die Koloniegröße für alle ts beschreibt. Nämlich
$y(t) = e^{kt}$.

Falls wir jediglich Zeitreihendaten des Systems haben (also keine
Differentialgleichung), müssen wir anhand der Daten ableiten, ob unser
System liniär oder nicht-liniär ist. Hierzu gibt es verschiedene Test,
wie zum Beispiel Akaike Information Criterion or Bayesian Information
Criterion (mehr dazu im nächsten Artikel). Um das Systemverhalten für
die Zukunft vorherzusagen (wie groß ist die Bakterienkolonie zum
Zeitpunkt x), können wir liniäre Zeitreihenmethoden verwenden, wie zum
Beispiel ANOVA und ANCOVA, sowie ihre multivariaten Versionen MANOVA und
MANCOVA.

### Nicht-liniären dynamische Systeme

In nicht-liniären Systemen wird das Systemverhalten hingegen von
Interaktionen zwischen den Systemkomponenten geprägt. Beispiel hierfür
ist ein Gewicht an einer Feder, welches ohne Reibung auf und ab schwingt
(harmonischer Oszillator). Das Makroverhalten des Systems wird durch die
Interaktion zweier Variablen beschrieben: Position und Geschwindigkeit.
Das System aus Differentialgleichungen lautet:

\
$$\frac{\delta p}{\delta t} = v(t)$$\
$$\frac{\delta v}{\delta t} = - p(t)$$\
p: Position, v: Geschwindigkeit, t: Zeit

Für dieses System existiert jedoch keine analytische Lösung. Das heißt,
wir können keine Funktionen p(t) und v(t) finden, die jeweils Position
und Geschwindigkeit des Gewichts zu jedem Zeitpunkt t in der Zukunft
beschreiben. Aber zum Glück gibt es numerische Methoden. Diese
verlangen, dass wir zwischen unserer Ausgangspostion zum Zeitpunkt t=0
und unserem Berechnungsziel, der Position zum Zeitpunkt t = n alle
Positionswerte für alle t's nacheinander berechnen müssen (\*Seufz\*).
Es gibt verschiedene Methoden, um Differentialgleichungen zu lösen. Eine
davon ist das explizite Euler Verfahren (forward Euler). Hierzu stellen
wir uns vor, dass alle Positionen abhängig von der Zeit auf einem Pfad
im Positions-Zeit Koordinatensystem liegen (siehe Abbildung 2). Die
Steigung dieses Pfades wird durch $\frac{\delta p}{\delta t}$
beschrieben. Um von unserem jetzigen Zustand zum nächsten zu gelangen,
müssen wir demnach Folgendes berechnen:

\
$$\left\lbrack \begin{array}{l}
{p(t + \Delta t)} \\
{v(t + \Delta t)} \\
\end{array} \right\rbrack = \left\lbrack \begin{array}{l}
{p(t)} \\
{v(t)} \\
\end{array} \right\rbrack + s(t) \ast \Delta t$$\
$$s(t):Steigung = \left\lbrack \begin{array}{l}
\frac{\Delta p(t)}{\Delta t} \\
\frac{\Delta v(t)}{\Delta t} \\
\end{array} \right\rbrack$$\
Die Steigung ist die erste Ableitung der alten Position und das
Zeitinterval $\Delta t$ ist frei wählbar. **Aber Vorsicht:** Numerische
Methoden sind keine perfekten Lösungen. Da sie Zeit diskretisieren, sind
die Berechnungen nie zu 100% exakt. Je kleiner $\Delta t$ desto genauer
werden die Berechnungen, jedoch ist hierfür mehr rechenarbeit nötig.

![](/images/blog/sfi-euler.jpg){.img-responsive}*Abbildung
2: Explizites Euler Verfahren zur numerischen Lösung von
Differenzialgleichungen*\
\
Wir können nun das Verhalten des Systems auf zwei verschiedene weisen
darstellen. Zum einen als Position über die Zeit (siehe Abbildung 3),
zum anderen in einem Phasendiagramm, wo wir die Systemvariablen
(Position und Geschwindigkeit) gegeneinander plotten (siehe Abbildung
4). Letztere Darstellung hat den Vorteil, dass wir den Attraktor des
Systems identifizieren können, welcher das Langzeitverhalten des Systems
characterisiert. In unserem Fall schwingt das Gewicht die ganze Zeit mit
derselben Amplitude nach oben und nach unten. Das System hat daher einen
periodischer Attraktor, welcher im Phasendiagram durch einen Grezzyklus
(limit cycle) zu sehen ist.

Falls unser System durch Reibung beeinfluss werden würde, würde die
Amplitude der Schwingung mit der Zeit abnehmen. Das Gewicht würde
irgendwann zum Stillstand kommen. In diesem Fall wäre der Attraktor
unseres Systems ein (fixed point) und wir sähen eine Spirale im
Phasendiagram (siehe Abbildung 5).

![](/images/blog/sfi-periodic.jpg){.img-responsive}*Abbildung
3: Systemzustand über Zeit hinweg*\
\
![](/images/blog/sfi-limit-cycle.jpg){.img-responsive}*Abbildung
4: Phasendiagram mit Grenzzyklus*\
\
![](/images/blog/sfi-fixed-point.jpg){.img-responsive}*Abbildung
5: Phasendiagram mit Fixpunkt*\
\
### Chaotische dynamische Systeme

Jedoch weisen die wenigsten Systeme diese Regelmäßigkeiten auf. Echte
Datensätze aus der Natur sehen meist anders aus (siehe Abbildung 6)

![](/images/blog/sfi-chaotic.jpg){.img-responsive}*Abbildung
6: Nicht liniäre oder chaotische Zeitreihe*\
\
Ein solches Systemverhalten weist auf Chaos hin, was wir im Folgenden
testen werden.

Deterministisches Chaos sieht zwar willkürlich aus, entsteht aber in
Systemen ohne Zufalsskomponente. Das heißt jeder Zustand kann exakt
durch einen anderen vorangegangenen Zustand im System beschrieben
werden. Zum Beispiel, ist das heutige Wetter vom gestrigen Wetter
abhängig, weil die gestrige Position, Geschwindigkeit und Interaktion
der Luftmoleküle deren heutigen Zustand beeinflusst. Darüber hinaus sind
chaotische Systeme abhängig vom Ausgangszustand des Systems. Dies
beschreibt den berühmten Butterfly Effect: Der Flügelschal eines
Schmetterlings in Japan verursacht Monate später einen Hurricane in der
Karibik. Wären die Anfangsbdingungen anders gewesen (kein
Schmetterling), hätte das große Auswirkungen auf das System haben können
(z.B. kein Hurricane).

Das bekannteste chaotische System aus der Literatur ist das Lorentz
System, welches durch drei Differentialgleichungen beschrieben wird.

\
$$\frac{\delta x}{\delta t} = \omega(y - x)$$\
$$\frac{\delta y}{\delta t} = x(\rho - z) - y$$\
$$\frac{\delta z}{\delta t} = xy - \beta z$$\
Attraktoren in chaotischen Systemen heißen seltsame Attraktoren (siehe
Titel Grafik).

Wie im Abschnitt über non-liniäre Systeme beschrieben, können wir die
Lösungen dieser Differentialgleichungen numerisch berechnen und dadurch
das Phasendiagramm ermitteln. Doch Vorsicht: Unsere Computer arbeiten
mit einer endlichen Präzision, das heißt kleine und große Zahlen können
nicht bis ins unendliche dargestellt werden. Nach einer bestimmten
Kommastelle rundet der Computer einfach auf und die numerische Lösung
ist ein bisschen ungenauer als die echte Lösung. Diese kleine
Veränderung kann große Ausmaße auf das System zu einem späteren
Zeitpunkt haben. Die numerische Lösungen kann somit sehr stark von der
echten Lösung abweichen. Es empfihelt sich daher das System mehrmals zu
lösen und einen Mittelwert zu berechnen.

Ein chaotisches System hat mindestens drei Parameter und mindestens
einen positiven Lyapunov Exponenten. Der Lyapunov Exponent λ misst wie
stark sich die Trajekte eines Systems im Phasendiagramm mit der Zeit
voneinander entfernen. Ein positiver Lyapunov exponent impliziert, dass
die Trajekte sich stets mehr voneinander entfernen und daher kleine
Unterschiede in Anfangswerten große Ausmaß auf das System haben. Jedes
System hat einen Lyapunov Exponenten für jede Dimension, d.h. für jeden
Parameter des Systems. Unser harmonischer Osxillator hat zum Beispiel
zwei Lyapunov Exponenten, da das System durch die Parmeter Position und
Geschwindigkeit beschrieben werden kann. Unabhängig von der Dynamik des
Systems lassen sich mithilfe des Lyapunov Exponenten Aussagen über die
Stabilität des Systems treffen. Wenn die Summe aller Lyapunox Exponenten
kleiner als Null ist, ist das System attraktiv (Grenzzyklus oder
Fixpunkt, oder seltsamer Attraktor). Falls alle Lyapunov Exponenten
kleiner als Null sind, liegt ein Fixpunkt vor.

Software für nicht-liniäre Zeitreihenanalyse Lyapunov Exponenten,
Attraktors, deren Stabilität und weitere topographische Eigenschaften
von nicht-liniären System lassen sich analytisch bestimmen, sofern das
System durch Differentialgleichungen beschrieben werden kann (vgl.
Eigenwerte der Jacobian Matrix). Da dies oftmals jedoch nicht der Fall
ist, möchte ich euch hier die Software TISEAN vorstellen, ein
open-source tool, welches viele der nicht-liniären Analysen ausführt
(Hegger, Kantz & Schreiber). TISEAN akzeptiert Datensätze in allen
möglichen Formaten und hat eine kompakte Dokumentation aller Funktionen
(Hegger, Kantz & Schreiber). Da Wrapper für andere Programmiersprachen
noch nicht großflächig implementiert sind, ist es am einfachsten die
TISEAN Funktionen vom Terminal auszuführen und die Ergebnisse als
Dateiabzuspeichern. Letztere können dann mit der Programmiersprache
eurer Wahl visualisiert und weiter bearbeitet werden. Mehrere kurze
TISEAN Tutorials sind auf der Website zu finden. Um ein tieferes
konzeptionelles Verständnis der angewandten Methoden und nicht-liniären
Zeitanalysemethoden zu erhalten, empfehle ich das Buch "Nonlinear Time
Series Analysis" (Kantz & Schreiber, 2004) und für Eilige den
wissenschaftlichen Artikel "Nonlinear time-series analysis revisited"
(Bradley & Kantz, 2015).

Um den Lyapunox Exponenten zu berechnen, speichern wir unseren
ausgewähleten Datensatz im TISEAN bin Ordner ab und navigieren
anschließend in der Commandline zu jenem Ordner. Dann tippen wir
folgendes ein:

    lyap\_k.exe  Datensatz.dat -o

Wir können auch noch Parameterwerte angeben. Hierfür schreiben wir vor
-o den Namen des Parameter und direkt dahinter den mitgegebenen Wert.
Zum Beispiel, -c1, um anzugeben, dass die erste Spalte unseres
Datensatzes eingelesen werden soll. Es empfiehlt sich mit den Parametern
etwas zu experimentieren. Als Output erhalten wir eine Datei mit
mehreren Ergebnisdatenreihen. Die Anzahl dieser Ergebnisreihen hängt von
den Dimensionen ab, die TISEAN in unseren Daten erkannt hat. Das heißt,
wir füttern TISEAN mit einer Zeitreihe, von deren ursprüngliche System
wir nicht wissen wie viele Parameter dieses beeinflussen. TISEAN schätzt
die Anzahl der Parameter von der das System abhängt. Wir plotten alle
Ergebnisdatenreihen und schauen, ob die Grafik im ersten Teil einer
liniäre Funtion gleicht. Falls ja, fitten wir eine Linie zu diesem Teil
des Plots. Falls nicht, eignet sich diese Analysemethode
höchstwahrscheinlich nicht für den ausgewählten Datensatz. Er sollte
nochmals auf Nichtliniarität geprüft werden. Die Steigungen der Linien
sind unsere Lyapunov Exponenten. Der liniäre Fit sollte auf jeden Fall
von Hand erfolgen. Auch wenn es verführerisch klingen mag: Schreibt bloß
KEIN Script, dass den Bereich bestimmt, in dem der liniäre Fit erfolgen
soll! Nicht-liniäre Systemen verlangen eine genaue Analyse eines
Menschen. Wir müssen die Ergebnisse selbst interpretieren, nicht der
Computer.

Eine Warnung zum Schluss: TISEAN eignet sich ausschließlich zur
topographischen Analyse eines Systems. Für den Fall, dass ihr
nicht-liniäre Zeitreihen als Vorhersagetool nutzen wollt, sollten andere
Methoden verwendet werden, wie zum Beispiel delay-encoordinate embedding
in Kombination mit Lorentz Methods of Analogues (Garland, James &
Bradley, 2016).

\
liniär
nicht liniär, nicht chaotisch
chaotisch
kleine Ursache → kleine Konsequenz
kleine Ursache → mögliche Konsequenz
kleine Ursache → mögliche große Konsequenz
Attraktor ist immer ein Fixpunkt
verschiedene Attraktoren möglich
immer seltsamer Attraktor
immer analytische Lösung möglich
analytische Lösung, manchmal Lösung
analytische Lösung nie möglich
1 - n Dimensionen
1 - n Dimensionen
immer mindestens 3 Dimensionen
"the whole is the sum of its parts"
"the whole is more than the sum of its parts"
"the whole is more than the sum of its parts"
keine sensitive Abhangigkeit von den Anfangsbedingungen
sensitive Abhängigkeit von den Anfangsbedingungen
sensitive Abhängigkeit von den Anfangsbedingungen
*Tabelle 1: Zusammenfassung dynamische Systeme*\
\
### Literatur

**R. Hegger, H. Kantz & T. Schreiber:** [TISEAN
website](https://www.pks.mpg.de/~tisean/Tisean_3.0.1/index.html)

**R. Hegger, H. Kantz & T. Schreiber:** [TISEAN
Funktionen](https://www.mpipks-dresden.mpg.de/~tisean/TISEAN_2.1/docs/contents.html)

**H. Kantz & T. Schreiber (2004):** Nonlinear Time Series Analysis.
Cambridge University Press.

**E. Bradley & H. Kantz (2015):** Nonlinear time-series analysis
revisited. Chaos 25.

**J. Garland, R.G. James, E. Bradley (2016):** Leveraging information
storage to select forecast-optimal parameter for delay-coordinate
reconstructions. Physical Review E, 93.

------------------------------------------------------------------------


