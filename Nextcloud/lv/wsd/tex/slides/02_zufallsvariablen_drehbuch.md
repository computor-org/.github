# VO 2 Drehbuch

- Datum: `2026-03-26`
- Grundlage: [VO_Plan.md](/home/ert/Nextcloud/lv/wsd/VO_Plan.md)
- Skriptbasis: [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex)
- Timing-Modell: [README.md](/home/ert/Nextcloud/lv/wsd/tex/slides/README.md)

## Absatz 001

- Text:
  Jetzt ist es so, dass bei simplen Beispielen wie Würfelspielen ganz klar ist, dass man den Ergebnissen einfach Zahlen zuordnen kann. Wir erinnern uns: Wir haben den Ergebnissen des Würfels einfach die natürlichen Zahlen 1, 2, 3, 4, 5, 6 zugeordnet. Das sind natürlich auch reelle Zahlen, und ein Ereignis ist dann eine Menge, die mehrere solcher Ergebnisse enthält. Man könnte auch sagen: ein Wertebereich. Wenn ich zum Beispiel sage, der Würfel habe weniger als drei gezeigt, dann wären 1 und 2 darin enthalten. Allgemein ist es aber nicht immer so einfach. Wenn ich etwa eine Karte ziehe, dann ist das Ergebnis zunächst einmal einfach: Ich habe eine bestimmte Karte gezogen. Das ist noch keine Zahl. Die Ergebnisse beim Kartenziehen bilden also zunächst eine abstraktere Menge.
- Herkunft:
  `diktiert`
- Skriptanker:
  [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex), Übergang von diskreten Ergebnissen zur Zufallsvariable
- Typ:
  `normal`
- Wortzahl:
  `116`
- Berechnete Zeit:
  `0:56`
- Folientyp:
  `Inhaltsfolie`
- Moegliche Visualisierung:
  zunächst keine neue Folie erzwingen; später wahrscheinlich einfache Gegenüberstellung `Würfel` versus `Kartenziehen`

## Absatz 002

- Text:
  Wenn ich damit rechnen will, muss ich diese abstrakte Menge erst einmal wieder auf etwas Reelles abbilden. Genau das nennt man eine Zufallsvariable. Formal ist eine Zufallsvariable deshalb eine Abbildung, die jedem Element, also jedem Ergebnis, Vorsicht: nicht jedem Ereignis, sondern jedem Ergebnis, eine reelle Zahl zuordnet.
- Herkunft:
  `diktiert`
- Skriptanker:
  [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex#L14), Definition der Zufallsvariablen
- Typ:
  `dicht`
- Wortzahl:
  `47`
- Berechnete Zeit:
  `0:26`
- Folientyp:
  `Inhaltsfolie`
- Moegliche Visualisierung:
  formale Definition der Zufallsvariablen mit explizitem Hinweis `Ergebnis`, nicht `Ereignis`

## Absatz 003

- Text:
  Für den Würfel ist das trivial. Da kann ich einfach die identische Abbildung nehmen, also dem Würfelergebnis 1 die reelle Zahl 1 zuordnen und so weiter. Ein zweites Beispiel ist die Indikatorfunktion, die herausschneidet, ob das Ergebnis gerade oder ungerade ist. Sie gibt also immer 1 für gerade Zahlen und 0 für ungerade. Mit solchen Indikatorfunktionen kann man Ereignisse auch wieder als Mengen über eine Zufallsvariable definieren. Das, was wir vorher händisch hinschreiben mussten, nämlich dass die geraden Würfelergebnisse 2, 4 und 6 sind, kann man dann abstrakter schreiben als die Menge aller Ergebnisse, für die die Indikatorfunktion größer als 0.5 ist. Das funktioniert in diesem Fall natürlich, weil die Funktion nur die Werte 0 und 1 annimmt. Ich habe das grafisch noch einmal aufbereitet: Wir sehen die identische Abbildung und daneben, wie die Indikatorfunktion das Ereignis "gerade Zahl" aus dem Ergebnisraum herausschneidet und über das Komplement das Ereignis "ungerade Zahl" übrig bleibt.
- Herkunft:
  `diktiert`
- Skriptanker:
  [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex#L27), Identität und Indikatorfunktion als Beispiele
- Typ:
  `normal`
- Wortzahl:
  `168`
- Berechnete Zeit:
  `1:21`
- Folientyp:
  `Inhaltsfolie`
- Moegliche Visualisierung:
  später die bereits angelegte Grafik zu Identität und Indikatorfunktion verwenden und eventuell um das Herausziehen des Ereignisses ergänzen

## Absatz 004

- Text:
  Auch wenn wir Versuche wiederholen, passt dieses Bild sehr gut. Dann bekommen wir als Ergebnisse die Elemente der Produktmenge, also zum Beispiel bei dreimaligem Münzwurf geordnete Tupel wie Kopf-Kopf-Zahl. Und diesen Ergebnissen können wir dann wieder Zahlen zuordnen. Ein naheliegendes Beispiel ist: Wir ordnen jedem Ergebnis einfach die Anzahl der Köpfe zu. Dann sehen wir sofort, dass dreimal Kopf in gewissem Sinn unwahrscheinlicher ist, weil dieser Wert seltener vorkommt als etwa einmal oder zweimal Kopf.
- Herkunft:
  `diktiert`
- Skriptanker:
  [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex#L40), Beispiel wiederholter Münzwurf und Anzahl der Köpfe als Zufallsvariable
- Typ:
  `normal`
- Wortzahl:
  `77`
- Berechnete Zeit:
  `0:37`
- Folientyp:
  `Inhaltsfolie`
- Moegliche Visualisierung:
  später Tupelraum des dreifachen Münzwurfs mit Zuordnung zur Kopfanzahl

## Absatz 004a

- Text:
  Wenn wir denselben Versuch \(N\)-mal unter gleichen Bedingungen wiederholen, dann ist der Ergebnisraum des Gesamtexperiments der \(N\)-fache Produktraum \(\mathcal G^N=\mathcal G\times\cdots\times\mathcal G\). Ein einzelnes Ergebnis des Gesamtexperiments ist dann ein geordnetes \(N\)-Tupel \((\omega_1,\ldots,\omega_N)\). Genau so modellieren wir eine Stichprobe vom Umfang \(N\).
- Herkunft:
  `generiert`
- Skriptanker:
  [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex), Definition der Stichprobe über den Produktraum
- Typ:
  `dicht`
- Wortzahl:
  `55`
- Berechnete Zeit:
  `0:30`
- Folientyp:
  `Inhaltsfolie`
- Moegliche Visualisierung:
  Produktraumformel mit explizitem \(N\)-Tupel und einer Skizze der \(N\) Wiederholungen

## Absatz 004b

- Text:
  Wenn die Wiederholungen unabhängig sind und jeder Einzelversuch durch dieselben Wahrscheinlichkeiten beschrieben wird, dann faktorisiert die Wahrscheinlichkeit eines solchen Tupels einfach zum Produkt \(\prod_{i=1}^{N}P_{\omega_i}\). Eine Statistik ist dann jede Funktion auf diesem Produktraum. Der Stichprobenmittelwert ist also eine ganz konkrete Statistik auf \(\mathcal G^N\).
- Herkunft:
  `generiert`
- Skriptanker:
  [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex), Produktraumwahrscheinlichkeit und Statistik
- Typ:
  `dicht`
- Wortzahl:
  `56`
- Berechnete Zeit:
  `0:31`
- Folientyp:
  `Inhaltsfolie`
- Moegliche Visualisierung:
  prominente Produktformel für die Wahrscheinlichkeit und direkte Brücke zur Statistik

## Absatz 005

- Text:
  Jetzt, wo wir unsere Ergebnisse in Zahlen gegossen haben, können wir anfangen, Mittelwerte zu bilden. Dafür definieren wir den Mittelwert, meistens Erwartungswert genannt, als die gewichtete Summe einer Zufallsvariablen mit der dazugehörigen Wahrscheinlichkeit. Warum wir hier lieber Mittelwert als Erwartungswert sagen, sieht man sofort am fairen Würfel. Wenn wir dort die identische Zufallsvariable nehmen, also einfach die Augenzahl selbst, dann bekommen wir den Wert 3.5. Niemand würde erwarten, dass ein Würfel den Wert 3.5 zeigt. Als Mittelwert ist das aber völlig in Ordnung.
- Herkunft:
  `diktiert`
- Skriptanker:
  [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex#L79), Definition des Mittelwerts und Würfelbeispiel
- Typ:
  `normal`
- Wortzahl:
  `92`
- Berechnete Zeit:
  `0:44`
- Folientyp:
  `Inhaltsfolie`
- Moegliche Visualisierung:
  Definitionsfolie mit direkt anschließendem Würfelbeispiel; das Rechenbeispiel `3.5` soll unmittelbar nach der Definition sichtbar werden

## Absatz 006

- Text:
  Daran sieht man auch eine grundsätzliche Schwäche oder jedenfalls eine wichtige Eigenschaft des Mittelwerts: Er muss nicht selbst ein Wert sein, der tatsächlich jemals erreicht wird. Unsere Notation für den Mittelwert machen wir mit den Spitzenklammern, wie später auch in der Quantenmechanik. Davon unterscheiden wir den Stichprobenmittelwert. Der entsteht, wenn ich einen Versuch oft wiederhole und über die beobachteten Werte mittle.
- Herkunft:
  `diktiert`
- Skriptanker:
  [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex#L92), Bemerkungen zum Mittelwert und Notation
- Typ:
  `normal`
- Wortzahl:
  `63`
- Berechnete Zeit:
  `0:30`
- Folientyp:
  `Inhaltsfolie`
- Moegliche Visualisierung:
  Notationsfolie oder Ergänzung auf derselben Mittelwertfolie; Kontrast zwischen Spitzenklammern und Stichprobenmittelwert mit Überstrich

## Absatz 007

- Text:
  Es gibt dabei einen feinen, aber wichtigen Unterschied: Der wahre Mittelwert ist keine Zufallsvariable, sondern ein fixer Wert der Verteilung. Der Stichprobenmittelwert ist dagegen eine Zufallsvariable auf dem Ergebnisraum der wiederholten Versuche. Genauer nennt man so eine aus der Stichprobe berechnete Zufallsvariable eine Statistik. Der Stichprobenmittelwert ist also eine Statistik und gleichzeitig ein Schätzer für den wahren Mittelwert. Und je öfter ich den Versuch wiederhole, desto näher kommt dieser Stichprobenmittelwert typischerweise an den wahren Mittelwert heran.
- Herkunft:
  `diktiert`
- Skriptanker:
  [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex#L101), Mittelwert versus Stichprobenmittelwert; [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex#L242), Stichprobenmittelwert
- Typ:
  `dicht`
- Wortzahl:
  `93`
- Berechnete Zeit:
  `0:51`
- Folientyp:
  `Inhaltsfolie`
- Moegliche Visualisierung:
  knappe Gegenüberstellung `Mittelwert` versus `Stichprobenmittelwert`; später anschließender Übergang zum Gesetz der großen Zahlen

## Absatz 007a

- Text:
  Formal schreibt man den Stichprobenmittelwert auf dem Produktraum als \(\overline X(\omega_1,\ldots,\omega_N)=\frac1N\sum_{i=1}^{N}X(\omega_i)\). Wenn die Stichprobe dann wirklich beobachtet ist, schreiben wir meist kürzer \(\overline x=\frac1N\sum_{i=1}^{N}x_i\).
- Herkunft:
  `generiert`
- Skriptanker:
  [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex), präzise Definition des Stichprobenmittelwerts als Statistik
- Typ:
  `dicht`
- Wortzahl:
  `36`
- Berechnete Zeit:
  `0:22`
- Folientyp:
  `Inhaltsfolie`
- Moegliche Visualisierung:
  Formel prominent, erst auf \(\mathcal G^N\), dann die verkürzte Schreibweise mit \(x_i\)

## Absatz 008

- Text:
  Für Funktionen von Zufallsvariablen verwenden wir eine abgekürzte Notation. Und der Mittelwert ist eine lineare Operation, das heißt: Ich kann konstante Faktoren herausziehen und Summen im Mittel auseinanderziehen. Einfach gesagt: Wenn überall doppelt so viel herauskommt, dann ist es im Mittel auch doppelt so viel.
- Herkunft:
  `diktiert`
- Skriptanker:
  [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex#L107), Funktionen und Linearität des Mittelwerts
- Typ:
  `normal`
- Wortzahl:
  `53`
- Berechnete Zeit:
  `0:25`
- Folientyp:
  `Inhaltsfolie`
- Moegliche Visualisierung:
  kurze Formelzeile zur Linearität plus ein sehr knappes Alltagsbeispiel

## Absatz 009

- Text:
  Das Rechenbeispiel mit dem Würfel sollten wir gleich direkt nach der Definition bringen, damit sofort klar ist, warum wir lieber Mittelwert sagen. Und ich hätte an der Stelle auch gern eine kurze schwarze Folie oder einen kurzen Moment, in dem die Studierenden das selbst ausrechnen und dann jemand antworten darf.
- Herkunft:
  `diktiert`
- Skriptanker:
  didaktische Anweisung für die spätere Folienableitung zu [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex#L148)
- Typ:
  `uebergang`
- Wortzahl:
  `46`
- Berechnete Zeit:
  `0:22`
- Folientyp:
  `Schwarze Folie`
- Moegliche Visualisierung:
  kurze schwarze Denkpause direkt nach der Definition und vor dem aufgedeckten Würfel-Rechenbeispiel

## Absatz 010

- Text:
  Wo der Mittelwert ist, ist natürlich die Varianz nicht weit. Auf dem Weg dorthin führen wir gleich ein allgemeineres Konzept ein mit dem Namen Moment. Ein Moment einer Zufallsvariablen ist der Mittelwert einer Potenz dieser Variablen. Also: das erste Moment ist der Mittelwert selbst, also der Mittelwert von \(x^1\), das zweite Moment ist der Mittelwert von \(x^2\), dann das dritte Moment und so weiter.
- Herkunft:
  `diktiert`
- Skriptanker:
  [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex#L163), Definition der Momente
- Typ:
  `normal`
- Wortzahl:
  `69`
- Berechnete Zeit:
  `0:33`
- Folientyp:
  `Inhaltsfolie`
- Moegliche Visualisierung:
  kompakte Momentenfolie mit `m_i = \langle X^i \rangle` und den Spezialfällen `m_1`, `m_2`, `m_3`

## Absatz 011

- Text:
  Damit man daraus die Varianz bekommt, geht man dann zu den zentralen Momenten über. Bei zentralen Momenten wird vorher der Mittelwert abgezogen, bevor die Potenz gebildet wird. Im Speziellen kann man damit die Varianz als zweites zentrales Moment definieren, also als den Mittelwert von \((x-\langle x\rangle)^2\). Dazu gibt es auch einen kleinen Satz, den man sofort durch simples Rechnen beweisen kann. Der heißt Verschiebungssatz. Er sagt, dass diese Varianz gleich dem zweiten nichtzentralen Moment minus dem Quadrat des Mittelwerts ist. Das kennen Sie vielleicht aus der Experimentalphysik: Bei Trägheitsmomenten gibt es eine ganz analoge Formel, und dort heißt das der Steinersche Satz.
- Herkunft:
  `diktiert`
- Skriptanker:
  [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex#L182), zentrale Momente; [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex#L194), Varianz und Verschiebungssatz
- Typ:
  `dicht`
- Wortzahl:
  `123`
- Berechnete Zeit:
  `1:00`
- Folientyp:
  `Inhaltsfolie`
- Moegliche Visualisierung:
  Definition des zentralen Moments, Varianzformel und daneben der kurze Hinweis `Verschiebungssatz`; die Steiner-Analogie eher als kleiner Randhinweis

## Absatz 012

- Text:
  Die Standardabweichung ist dann die Wurzel aus der Varianz. Sie hat die besondere Bedeutung der Streuung der Werte um den Mittelwert, weil die Varianz selbst nicht dieselbe Dimension wie die Werte hat, sondern quadriert ist. Dann würde ich Sie an dieser Stelle gleich bitten, auch für den fairen Würfelwurf nach dem Mittelwert jetzt die Varianz und dann die Standardabweichung auszurechnen.
- Herkunft:
  `diktiert`
- Skriptanker:
  [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex#L215), Standardabweichung
- Typ:
  `normal`
- Wortzahl:
  `74`
- Berechnete Zeit:
  `0:36`
- Folientyp:
  `Schwarze Folie`
- Moegliche Visualisierung:
  schwarze Denkpause; Auflösung erst auf der nächsten Folie

## Absatz 013

- Text:
  Und noch einmal zur Erinnerung: Auch diese Momente sind alles intrinsische Eigenschaften unserer Ergebnismenge und der darauf definierten Wahrscheinlichkeiten. Sie sind also keine Zufallsvariablen. Sehr wohl eine Zufallsvariable ist dagegen der Stichprobenmittelwert, den wir statistisch für endliche Stichproben definieren, weil wir ja nicht unendlich oft probieren können. Je öfter wir probieren, desto näher wird sich dieser Stichprobenmittelwert an den wahren Mittelwert annähern.
- Herkunft:
  `diktiert`
- Skriptanker:
  [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex#L103), Mittelwert keine Zufallsvariable; [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex#L242), Stichprobenmittelwert
- Typ:
  `normal`
- Wortzahl:
  `79`
- Berechnete Zeit:
  `0:38`
- Folientyp:
  `Inhaltsfolie`
- Moegliche Visualisierung:
  knapper Rückbezug `Momente = Kennzahlen der Verteilung` versus `Stichprobenmittelwert = Statistik`

## Absatz 014

- Text:
  Das Maß dafür, wie ungenau dieser Stichprobenmittelwert noch ist, ist der Standardfehler. Der Standardfehler ist die Standardabweichung dividiert durch die Wurzel der Anzahl der Versuche. Diese Wurzelabhängigkeit wird uns später auch noch oft begleiten, zum Beispiel bei Monte-Carlo-Methoden. Wir lassen das jetzt zunächst als Definition stehen und lernen später Genaueres dazu. Wichtig ist hier die Intuition: Auch wenn die einzelnen Ergebnisse mit der Standardabweichung streuen, streut der Mittelwert über viele Wiederholungen immer weniger, je öfter ich den Versuch wiederhole. Das hat mit dem Gesetz der großen Zahlen zu tun.
- Herkunft:
  `diktiert`
- Skriptanker:
  [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex#L242), Stichprobenmittelwert und Standardfehler
- Typ:
  `dicht`
- Wortzahl:
  `102`
- Berechnete Zeit:
  `0:49`
- Folientyp:
  `Inhaltsfolie`
- Moegliche Visualisierung:
  später Abbildung in Folien und Skript nachziehen: Streuung der Einzelwerte versus engere Streuung des Stichprobenmittelwerts bei wachsendem `N`

## Absatz 015

- Text:
  Die letzte Formel, die wir in diesem Unterabschnitt gleich erwähnen, ist die Stichprobenvarianz. Anders als der Stichprobenmittelwert wird sie durch \(N-1\) und nicht durch \(N\) dividiert. Wenn man das nicht tut, bekommt das Ergebnis eine Verzerrung, auf Englisch einen Bias. Der Grund ist, dass man ja den Mittelwert auch nur schätzt. Die Varianz wird also nicht um den wahren Mittelwert herum bestimmt, sondern schon um einen geschätzten Wert. Dadurch unterschätzt man die Streuung systematisch, vor allem bei kleinen Stichproben. In der Praxis ist es deshalb wichtig, immer die richtige Formel oder Funktion mit den richtigen Einstellungen zu verwenden, wenn man aus Daten eine Varianz schätzt.
- Herkunft:
  `diktiert`
- Skriptanker:
  [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex#L252), Stichprobenvarianz
- Typ:
  `dicht`
- Wortzahl:
  `112`
- Berechnete Zeit:
  `0:54`
- Folientyp:
  `Inhaltsfolie`
- Moegliche Visualisierung:
  Stichprobenvarianz mit `N-1` klar hervorheben; kleiner Warnhinweis `Bias bei falscher Normierung`

## Absatz 016

- Text:
  Bevor wir hier Schluss machen, lohnt sich noch ein reines Bild zur Intuition. Hier sehen Sie zwei verschiedene diskrete Verteilungen mit demselben Mittelwert 3.5. Der Schwerpunkt liegt also an derselben Stelle. Aber oben sitzt die Wahrscheinlichkeitsmasse dicht beim Schwerpunkt, unten weit außen. Genau das meint Varianz: nicht die Lage des Schwerpunkts, sondern wie weit die Werte typischerweise von ihm entfernt sind. Der Mittelwert allein beschreibt also noch nicht die ganze Verteilung.
- Herkunft:
  `Codex-Platzhalter, nicht vom Dozenten diktiert`
- Skriptanker:
  [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex#L194), Varianz als Streuung um den Mittelwert
- Typ:
  `normal`
- Wortzahl:
  `73`
- Berechnete Zeit:
  `0:35`
- Folientyp:
  `Inhaltsfolie`
- Moegliche Visualisierung:
  zwei diskrete Verteilungen auf derselben Zahlengeraden, gleicher Mittelwert und deutlich verschiedene Streuung

## Absatz 017

- Text:
  Dasselbe gibt es auf der Ebene der Daten. Hier haben zwei konkrete Stichproben denselben Stichprobenmittelwert 3.5. Wenn ich nur auf den Mittelwert schaue, sehen sie gleich aus. Aber die zweite Stichprobe ist viel weiter auseinandergezogen. Deshalb ist dort die Stichprobenvarianz größer. So trennt man die Rollen sauber: Der Stichprobenmittelwert beschreibt die Lage der beobachteten Daten, die Stichprobenvarianz ihre Streuung um diesen geschätzten Mittelpunkt.
- Herkunft:
  `Codex-Platzhalter, nicht vom Dozenten diktiert`
- Skriptanker:
  [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex#L242), Stichprobenmittelwert; [ws_definitions.tex](/home/ert/Nextcloud/lv/wsd/tex/skriptum/TexFiles/ws_definitions.tex#L252), Stichprobenvarianz
- Typ:
  `normal`
- Wortzahl:
  `66`
- Berechnete Zeit:
  `0:32`
- Folientyp:
  `Inhaltsfolie`
- Moegliche Visualisierung:
  zwei kleine Stichproben auf derselben Zahlengeraden mit gleichem Stichprobenmittelwert und unterschiedlicher Stichprobenvarianz

## Folienzuordnung

- `Titelfolie`:
- `Rückblick auf VO 1: Grundbegriffe`:
- `Von Ergebnissen zu Zahlen`: Absatz `001`
- `Zufallsvariable`: Absatz `002`
- `Beispiel 1: Identische Abbildung`: Absatz `003`
- `Beispiel 2: Indikatorfunktion`: Absatz `003`
- `Ereignisse über eine Zufallsvariable definieren`: Absatz `003`
- `Rückblick: Stichprobe im Produktraum`: Absatz `004a`, `004b`
- `Beispiel: Dreimal Münzwurf`: Absatz `004`
- `Funktionen von Zufallsvariablen`: Absatz `008`
- `Mittelwert einer diskreten Zufallsvariablen`: Absatz `005`
- `Leere Folie`: Absatz `009`
- `Fairer Würfel: Was ist der Mittelwert?`: Absatz `005`
- `Mittelwert versus Stichprobenmittelwert`: Absatz `006`, `007`, `007a`
- `Linearität des Mittelwerts`: Absatz `008`
- `Momente`: Absatz `010`
- `Zentrale Momente und Varianz`: Absatz `011`
- `Leere Folie`: Absatz `012`
- `Fairer Würfel: Varianz und Standardabweichung`: Absatz `012`
- `Kennzahl der Verteilung oder Statistik?`: Absatz `013`
- `Standardfehler des Stichprobenmittelwerts`: Absatz `014`
- `Stichprobenvarianz`: Absatz `015`
- `Bild: Gleicher Mittelwert, andere Varianz`: Absatz `016`
- `Bild: Gleicher Stichprobenmittelwert, andere Stichprobenvarianz`: Absatz `017`
- `Bis Hierher`:

## Sprechernotizen

### 01. Titelfolie

Jetzt kommen wir zum zweiten Abschnitt des Einführungsteils. Bisher haben wir über Ereignisse und Wahrscheinlichkeiten gesprochen. Jetzt gießen wir Ergebnisse in Zahlen und kommen damit zu Zufallsvariablen, Mittelwert und Stichprobe.


### 02. Rückblick auf VO 1: Grundbegriffe

Bevor wir weitergehen, wiederholen wir ganz kurz die Grundbegriffe aus der letzten Einheit. Ein Versuch ist etwa einmal würfeln. Ein Ergebnis ist dann ein einzelner Ausgang wie die Zahl 3. Der Ergebnisraum ist die Menge aller möglichen Ergebnisse, beim Würfel also einfach die Zahlen 1 bis 6. Ein Ereignis ist eine Teilmenge davon, zum Beispiel die geraden Augenzahlen. Und ein Elementarereignis ist ein Ereignis mit genau einem Ergebnis, also zum Beispiel nur die 3.

### 03. Von Ergebnissen zu Zahlen

Jetzt ist es so, dass bei simplen Beispielen wie Würfelspielen ganz klar ist, dass man den Ergebnissen einfach Zahlen zuordnen kann. Wir erinnern uns: Wir haben den Ergebnissen des Würfels einfach die natürlichen Zahlen 1, 2, 3, 4, 5, 6 zugeordnet. Das sind natürlich auch reelle Zahlen, und ein Ereignis ist dann eine Menge, die mehrere solcher Ergebnisse enthält. Man könnte auch sagen: ein Wertebereich. Wenn ich zum Beispiel sage, der Würfel habe weniger als drei gezeigt, dann wären 1 und 2 darin enthalten. Allgemein ist es aber nicht immer so einfach. Wenn ich etwa eine Karte ziehe, dann ist das Ergebnis zunächst einmal einfach: Ich habe eine bestimmte Karte gezogen. Das ist noch keine Zahl. Die Ergebnisse beim Kartenziehen bilden also zunächst eine abstraktere Menge.

### 04. Zufallsvariable

Wenn ich damit rechnen will, muss ich diese abstrakte Menge erst einmal wieder auf etwas Reelles abbilden. Genau das nennt man eine Zufallsvariable. Formal ist eine Zufallsvariable deshalb eine Abbildung, die jedem Element, also jedem Ergebnis, Vorsicht: nicht jedem Ereignis, sondern jedem Ergebnis, eine reelle Zahl zuordnet.

### 05. Beispiel 1: Identische Abbildung

Für den Würfel ist das erste Beispiel ganz trivial: Ich nehme einfach die identische Abbildung. Dem Ergebnis 1 ordne ich die reelle Zahl 1 zu, dem Ergebnis 2 die Zahl 2 und so weiter. Weil die Ergebnisse hier ohnehin schon Zahlen sind, sieht diese Zufallsvariable genauso aus wie die Identität.

### 06. Beispiel 2: Indikatorfunktion

Ein zweites Beispiel ist die Indikatorfunktion für das Ereignis "gerade Zahl". Die gibt 1 für die Ergebnisse 2, 4 und 6 und 0 für 1, 3 und 5. Damit sieht man schon, dass eine Zufallsvariable nicht die Ergebnisse selbst wiedergeben muss, sondern auch nur eine Ja-Nein-Information codieren kann.

### 07. Ereignisse über eine Zufallsvariable definieren

Und damit kann man jetzt umgekehrt wieder Ereignisse definieren. Das, was wir vorher händisch als die Menge der geraden Augenzahlen hingeschrieben haben, kann ich auch schreiben als die Menge aller Ergebnisse, für die die Indikatorfunktion größer als 0.5 ist. In diesem Sinn schneidet mir die Zufallsvariable ein Ereignis aus dem Ergebnisraum heraus.

### 08. Rückblick: Stichprobe im Produktraum

Zur Erinnerung: Bei der Wiederholung desselben Versuchs ist der Ergebnisraum des Gesamtexperiments der N-fache Produktraum, und eine Stichprobe vom Umfang N ist ein geordnetes N-Tupel von Ergebnissen. Wenn die Wiederholungen unabhängig sind, faktorisiert die Wahrscheinlichkeit eines solchen Tupels einfach zum Produkt der Einzelwahrscheinlichkeiten. Genau auf diesem Produktraum definieren wir dann unsere Statistiken.

### 09. Beispiel: Dreimal Münzwurf

Auch wenn wir Versuche wiederholen, passt dieses Bild sehr gut. Dann bekommen wir als Ergebnisse die Elemente der Produktmenge, also zum Beispiel bei dreimaligem Münzwurf geordnete Tupel wie Kopf-Kopf-Zahl. Und diesen Ergebnissen können wir dann wieder Zahlen zuordnen. Ein naheliegendes Beispiel ist: Wir ordnen jedem Ergebnis einfach die Anzahl der Köpfe zu. Dann sehen wir sofort, dass dreimal Kopf in gewissem Sinn unwahrscheinlicher ist, weil dieser Wert seltener vorkommt als etwa einmal oder zweimal Kopf.

### 10. Funktionen von Zufallsvariablen

Für Funktionen von Zufallsvariablen verwenden wir abgekürzte Notation. Wenn ich also nicht nur die Zufallsvariable selbst, sondern etwa ihr Quadrat oder eine lineare Kombination anschaue, dann schreiben wir den Mittelwert direkt in dieser Form hin. Das braucht man gleich für Momente, Varianz und alle weiteren Größen.

### 11. Mittelwert einer diskreten Zufallsvariablen

Jetzt, wo wir unsere Ergebnisse in Zahlen gegossen haben, können wir anfangen, Mittelwerte zu bilden. Dafür definieren wir den Mittelwert, meistens Erwartungswert genannt, als die gewichtete Summe einer Zufallsvariablen mit der dazugehörigen Wahrscheinlichkeit. Warum wir hier lieber Mittelwert als Erwartungswert sagen, sieht man sofort am fairen Würfel. Wenn wir dort die identische Zufallsvariable nehmen, also einfach die Augenzahl selbst, dann bekommen wir den Wert 3.5. Niemand würde erwarten, dass ein Würfel den Wert 3.5 zeigt. Als Mittelwert ist das aber völlig in Ordnung.

### 12. Leere Folie

Das Rechenbeispiel mit dem Würfel sollten wir gleich direkt nach der Definition bringen, damit sofort klar ist, warum wir lieber Mittelwert sagen. Und ich hätte an der Stelle auch gern eine kurze schwarze Folie oder einen kurzen Moment, in dem die Studierenden das selbst ausrechnen und dann jemand antworten darf.

### 13. Fairer Würfel: Was ist der Mittelwert?

Lassen Sie uns das gleich am fairen Würfel ausrechnen. Wenn wir die identische Zufallsvariable nehmen, dann ist der Mittelwert 3.5. Genau deshalb sage ich hier lieber Mittelwert als Erwartungswert: Kein Mensch erwartet, dass der Würfel jemals 3.5 zeigt, aber als Mittel der Verteilung ist 3.5 völlig sinnvoll.

### 14. Mittelwert versus Stichprobenmittelwert

Davon unterscheiden wir jetzt den Stichprobenmittelwert. Der wahre Mittelwert ist eine feste Eigenschaft der Verteilung und keine Zufallsvariable. Der Stichprobenmittelwert entsteht dagegen aus endlich vielen Beobachtungen; solange die Stichprobe noch nicht beobachtet ist, ist er selbst eine Zufallsvariable. Genauer nennt man so etwas eine Statistik. Er ist also eine Statistik auf dem Produktraum der Stichprobe und dient als Schätzer für den wahren Mittelwert. Formal ist das einfach der Durchschnitt der N beobachteten Werte.

### 15. Linearität des Mittelwerts

Der Mittelwert ist außerdem linear. Ich kann konstante Faktoren herausziehen und Summen auseinanderziehen. Anschaulich: Wenn überall doppelt so viel herauskommt, dann ist es im Mittel auch doppelt so viel. Diese einfache Eigenschaft wird uns später ständig das Rechnen erleichtern.

### 16. Momente

Wo der Mittelwert ist, ist natürlich die Varianz nicht weit. Auf dem Weg dorthin führen wir gleich ein allgemeineres Konzept ein mit dem Namen Moment. Ein Moment einer Zufallsvariablen ist der Mittelwert einer Potenz dieser Variablen. Also: das erste Moment ist der Mittelwert selbst, das zweite Moment ist der Mittelwert des Quadrats, dann das dritte Moment und so weiter.

### 17. Zentrale Momente und Varianz

Damit man daraus die Varianz bekommt, geht man dann zu den zentralen Momenten über. Bei zentralen Momenten wird vorher der Mittelwert abgezogen, bevor die Potenz gebildet wird. Im Speziellen kann man damit die Varianz als zweites zentrales Moment definieren. Dazu gibt es auch einen kleinen Satz, den man sofort durch simples Rechnen beweisen kann: Die Varianz ist gleich dem zweiten nichtzentralen Moment minus dem Quadrat des Mittelwerts. Das kennen Sie vielleicht aus der Experimentalphysik in einer ganz analogen Form als Steiner-Satz.

### 18. Leere Folie

Die Standardabweichung ist dann die Wurzel aus der Varianz. Sie hat die besondere Bedeutung der Streuung der Werte um den Mittelwert, weil die Varianz selbst nicht dieselbe Dimension wie die Werte hat, sondern quadriert ist. Rechnen Sie für den fairen Würfel jetzt nach dem Mittelwert auch die Varianz und dann die Standardabweichung aus.

### 19. Fairer Würfel: Varianz und Standardabweichung

Für den fairen Würfel ist das zweite Moment noch leicht auszurechnen, und daraus bekommt man sofort die Varianz. Die Varianz ist hier ungefähr 2.92 und die Standardabweichung ungefähr 1.71. Die Standardabweichung ist also ein lineares Streuungsmaß in derselben Einheit wie die Würfelaugen.

### 20. Kennzahl der Verteilung oder Statistik?

Und noch einmal zur Erinnerung: Auch diese Momente sind alles intrinsische Eigenschaften unserer Ergebnismenge und der darauf definierten Wahrscheinlichkeiten. Sie sind also keine Zufallsvariablen. Sehr wohl zufällig sind dagegen Größen wie der Stichprobenmittelwert oder später die Stichprobenvarianz, weil sie aus endlich vielen beobachteten Daten berechnet werden.

### 21. Standardfehler des Stichprobenmittelwerts

Das Maß dafür, wie ungenau dieser Stichprobenmittelwert noch ist, ist der Standardfehler. Der Standardfehler ist die Standardabweichung dividiert durch die Wurzel der Anzahl der Versuche. Wichtig ist hier die Intuition: Auch wenn die einzelnen Ergebnisse stark streuen, streut der Mittelwert über viele Wiederholungen immer weniger, je öfter ich den Versuch wiederhole.

### 22. Stichprobenvarianz

Die letzte Formel, die wir in diesem Unterabschnitt gleich erwähnen, ist die Stichprobenvarianz. Anders als der Stichprobenmittelwert wird sie durch N minus 1 und nicht durch N dividiert. Wenn man das nicht tut, bekommt das Ergebnis eine systematische Unterschätzung der Streuung, also einen Bias. In der Praxis ist es deshalb wichtig, bei der Auswertung immer die richtige Formel oder Funktion zu verwenden.

### 23. Bild: Gleicher Mittelwert, andere Varianz

Zum Schluss noch ein Bild für die Intuition. Beide Verteilungen haben denselben Mittelwert 3.5, also denselben Schwerpunkt. Aber oben liegt die Wahrscheinlichkeitsmasse dicht beim Schwerpunkt, unten weit außen. Genau diese Streuung um den Schwerpunkt misst die Varianz.

### 24. Bild: Gleicher Stichprobenmittelwert, andere Stichprobenvarianz

Und dasselbe sieht man auf der Datenebene. Beide Stichproben haben denselben Stichprobenmittelwert 3.5. Wenn ich aber auf die Streuung der beobachteten Werte schaue, ist die zweite Stichprobe viel breiter. Darum ist dort auch die Stichprobenvarianz größer.

### 25. Bis Hierher

Bis hierher haben wir also den Weg von Zufallsvariablen über Mittelwert und Stichprobenmittelwert bis zu Momenten, Varianz, Standardabweichung, Standardfehler und Stichprobenvarianz gelegt. Außerdem haben wir jetzt das zentrale Bild dazu: gleicher Mittelwert heißt noch lange nicht gleiche Streuung.
