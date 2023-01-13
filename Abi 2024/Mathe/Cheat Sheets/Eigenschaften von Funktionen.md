# Nullstellen
~~~ad-important
Funktion $0$ setzen.
$0=f(x)$
~~~
## Vielfachheit von NSt
~~~ad-important
Anzahl der Nullstellen.
~~~
# Schnittpunkt mit der $y$-Achse
~~~ad-important
Bei der Funktion $0$ einsetzen.
$y=f(0)$
~~~
# Definitionsbereich
~~~ad-important
Teilen durch $0$.
$f(x)=\frac{n}{x}$
Wurzeln mit Werten unter $0$.
$f(x)=\sqrt{x}$
Logarithmus mit Werten unter $0$
$f(x)=\log{x}$
Einschränkungen durch die Aufgabenstellung
$i=[\dots]$
~~~
# Asymptoten
## Waagerechte Asymptoten
~~~ad-important
Berechnung über den Grenzwert im Unendlichen.
~~~

~~~ad-example
$f(x)=\frac{2x^2-1}{x-x^2}$
$\lim\limits_{x\to\pm\infty}f(x)=-2$
~~~
## Senkrechte Asymptoten
~~~ad-important
Senkrechte Asymptoten sind Polstellen. Polstellen sind die Definitionslücken gebrochen-rationaler Funktionen. Man ermittelt sie, indem man den Nenner gleich $0$ setzt.
~~~

~~~ad-example
$f(x)=\frac{2x^2-1}{x-1}$
$0=x-1\quad x=1$
~~~
# Symmetrie
## Achsensymmetrie
~~~ad-important
Achsensymmetrie zur $y$-Achse: $f(x)=f(-x)$
~~~
## Punktsymmetrie
~~~ad-important
Punktsymmetrie zu einem Punkt, meist Koordinatenursprung.
$f(x)=-f(-x)$
$-f(x)=f(-x)$
~~~
# Extrempunkte / Extremstellen
~~~ad-important
An Extremstellen gilt: 
- $f'(x)=0$ (notwendig)
- $f''(x)\neq0$ (hinreichend)
~~~

~~~ad-example
$f(x)=x^2-2x+1$
$f'(x)=2x-2$
$f''(x)=2$

$0=2x-2\to x=1$
$0\neq2$
~~~
## Nachweis der Art des Extremus
~~~ad-important
- Minimum: $f''(x_E)>0$
- Maximum: $f''(x_E)<0$
oder
- Minimum: $f'(x)=-\to f'(x)=+$
- Maximum: $f'(x)=+\to f'(x)=-$
~~~

~~~functionplot
---
disableZoom: true
---
f(x)=x^2
f'(x)=2x
~~~

~~~ad-example
$f(x)=x^2$
$f'(x)=2x$
$f''(x)=2$

$0=2x_E\quad x_E=0$

Mimimum, da:
- $f'(-1)=-2$
- $f(1)=2$
~~~
## Absolute Extrema
~~~ad-important
Ist $f$ in einem abgeschlossenen Intervall $[a, b]$ definiert, so ergeben sich die absoluten Extrema, indem man die relativen Extrema bestimmt und mit den Funktionswerten am Rand vergleicht (Randwerte).
~~~
# Wendepunkte / Wendestellen
~~~ad-important
Ist $f$ im Intervall $]a,b[$ differenzierbar und geht der Graph $f$ beim Durchlaufen eines Punktes $W(x_W|y_W)$ von einer Rechtskurve in eine Linkskurve (oder umgekehrt) über, so heißt $W$ ein Wendepunkt und die Stelle $x_W$ eine Wendestelle von $f$.

Die Tangent in $W$ heißt Wendetangente. Ein Wendepunkt mit horizontaler Tangente heißt Sattelpunkt (Terassenpunkt).
~~~

~~~ad-help
An Wendepunkten gilt:
- $f''(x)=0$ (notwendig)
- $f'''(x)\neq0$ (hinreichend)
~~~