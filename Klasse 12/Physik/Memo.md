---
author: karlz
tags:
  - Physik
  - FGN
---

# Schwingungen

## Hooksches Gesetz

(Lb. S. 48)

Die wirkenden Kraft ist direkt proportional zur Auslenkung der Feder ist: $F=Ds$
- $D$ Federkonstante
- $s$ Auslenkung

**Beispiel**
$D=10 \frac{N}{m}$
Man benötigt eine Kraft von $10 N$, um die um $1 m$ zu dehnen.

### Scherung

(Lb. S: 49)

![Scherung](Working%20Materials/Schwingungen/Scherung.png)

$F\sim \delta$

### Torsion

![Torsion](Working%20Materials/Schwingungen/Torsion.png)

$F\sim \varphi$

## Größe einer Schwingung

![](Working%20Materials/Schwingungen/Schwingungen.png)

$\hat{y}$ Amplitude (Maximale Auslenkung)
$y$ Elongation (Auslenkung)
$f$ Frequenz in $1Hz=1s^{-1}$
$T$ Periode $T=\frac{1}{f}$

## Harmonische Schwingung

Schwingungen, die durch eine Sinus- oder Kosinusfunktion beschrieben werden kann.

## Zeigerdiagramm

![](Working%20Materials/Schwingungen/Zeigerdiagramm.png)

Eine gleichförmige Kreisbewegung kann man gedanklich in zwei harmonische Schwingungen gleicher Frequenz und Amplitude zerlegen, die senkrecht zueinander verlaufen. Umgekehrt kann man sich auch jede harmonische Schwingung als Projektion einer Kreisbewegung denken. Deshalb wird zur Veranschaulichung von harmonischen Schwingungen oft eine Zeigerdiagramm verwendet, in dem ein Zeiger der Länge $A$ mit der Frequenz $f$ um einen festen Punkt rotiert.

## Geschwindigkeit & Beschleunigung bei Schwingungen

Auslenkung
$y(t)=\hat{y}\sin{(\omega t)}$

Geschwindigkeit
$v(t)=\frac{dy}{dt}=\hat{y}\omega\cos{(\omega t)}=\hat{v}\cos{(\omega t)}$ mit $\hat{v}=\hat{y}\omega$

Beschleunigung
$a(t)=\frac{dv}{dt}=-\hat{y}\omega^{2}\sin{(\omega t)}=-\hat{a}\sin{(\omega t)}$ mit $\hat{a}=\hat{y}\omega^{2}$

### Rückstellkraft

$y(t)=\hat{y}\sin{(\omega t)}$
$a(t)=-\hat{y}\omega^{2}\sin{(\omega t)}=-\omega\hat{y}\sin{(\omega t)}=-\omega^{2}y(t)$

$a(t)\sim y(t)\to F_{r}(t)\sim a(t)\sim y(t)$

**Beispiel Federschwinger**
$F_{r}(t)=-Dy(t)$

### Eigenfrequenz Federschwinger

$w_{0}=\sqrt{\frac{D}{m}}$
$f_{0}=\frac{1}{2\pi} \sqrt{\frac{D}{m}}$
$T_{0}=2\pi \sqrt{\frac{m}{D}}$

### Periodendauer Fadenpendel

$w_{0}=\sqrt{\frac{g}{l}}$
$f_{0}=\frac{1}{2\pi} \sqrt{\frac{g}{l}}$
$T_{0}=2\pi \sqrt{\frac{l}{g}}$

## Energieerhaltung einer harmonischen Schwingung

|                | $E_{\text{kin}}$   | $E_{{pot}}$         |
| -------------- | ------------------ | ------------------- |
| Federschwinger | $\frac{m}{2}v^{2}$ | $\frac{1}{2}Dx^{2}$ |
| Fadenpendel    | $\frac{m}{2}v^{2}$ | $mgh$               |

$E_{ges}=E_{pot}+E_{kin}=\frac{1}{2}Dx(t)^{2}+ \frac{1}{2}mv(t)^{2}=\frac{1}{2}D(\hat{x}\cos{\omega t})^{2}+ \frac{1}{2}m (-\hat{x}\omega \sin{\omega t})^{2}$
$\frac{1}{2}D\hat{x}\cos^{2}{\omega t}+ \frac{1}{2}m \hat{v}^{2}\sin{\omega t}=E_{ges}\cos^{2}{\omega t}+E_{ges}\sin^{2}{\omega t}=E_{ges}(\cos^{2}{\omega t}+\sin^{2}{\omega t})=E_{ges}$

## Gedämpfte Schwingung

$\delta=\frac{b}{2m}$
$\omega=\sqrt{\omega_{0}^{2}-\delta^{2}}$

### Reibungskraft = konst.

$W_{R}=\Delta E=F_{R}(\hat{y}_{1}+\hat{y}_{2})$
$\Delta E=\frac{1}{2} D \hat{y}^{2}_{1}- \frac{1}{2}D\hat{y}^{2}_{2}$

$F_{R}(\hat{y}_{1}+\hat{y}_{2})=\frac{1}{2}D(\hat{y}^{2}_{1}-\hat{y}^{2}_{2})$
$F_{R}(\hat{y}_{1}+ \hat{y}_{2})=\frac{1}{2}D(\hat{y}_{1}+\hat{y}_{2})(\hat{y}_{1}-\hat{y}_{2})$
$F_{R}=\frac{1}{2}D(\hat{y}_{1}-\hat{y}_{2})$
$\frac{2F_{R}}{D}=(\hat{y}_{1}-\hat{y}_{2})$
$\hat{y}_{2}=\hat{y}_{1}-\frac{2F_{R}}{D}$

Amplitude nimmt linear  über die Zeit ab.
$\hat{y}_{n+1}=\hat{y}_{n}- \frac{2F_{R}}{D}$

### Reibungskraft ~ Geschwindigkeit

Ansatz
$\vec{F_{s}}=-D\hat{y}$
$\vec{F_{R}}=-b\vec{v}$
$\vec{F_{ges}}=\vec{F_{s}}+\vec{F_{R}}$

$m\vec{a}=-D\vec{y}-b\vec{v}$
$m \frac{d^{2}\vec{y}}{dt}=-D\vec{y}-b \frac{d\vec{y}}{dt}$

Lösung
$y(t)=\hat{y}e^{-st}\cos{\omega t}\quad \text{ mit } \delta=\frac{b}{2m}$
$\omega=\sqrt{\frac{D}{m}-\delta^{2}}$
$f=\frac{1}{2\pi}\sqrt{\frac{D}{m}-\delta^{2}}$

$\hat{y}(t)=\hat{y}e^{-st}$
$y(t)=\hat{y}(t)\cos{(\omega t)}$

### Starke Dämpfung

(Aperiodischer Grenzfall: $\omega_{0}=\delta$)

(Kriechfall: $\omega_{0}<\delta$)

## Resonanz

> Anregung und schwingendes System befinden sich in Resonanz, wenn die Erregerfrequenz und die Eigenfrequenz des Systems gleich sind.

![](Working%20Materials/Schwingungen/Resonanz.gif)

### Erzwungene Schwingung


> Je mehr  sich die Eregerfreqenz einer Eigenfrequenz des Systems nähert, desto mehr Energie pro Periode wird vom Erreger auf dem Oszillator übertragen Im Resonanzfall ist die Energieübertragung maximal.

Erregerfrequenz $f$
Eigenfrequenz $f_{0}$

$f<f_{0}\quad\Delta\varphi\approx0$

![](Working%20Materials/Schwingungen/Erzwungen%200.png)

$f=f_{0}\quad\Delta\varphi=\frac{\pi}{2}$

![](Working%20Materials/Schwingungen/Erzwungen%20pi2.png)

$f>f_{0}\quad\Delta\varphi=\pi$

![](Working%20Materials/Schwingungen/Erzwungen%20pi.png)

### Elektrischer Schwingkreis

**Skizze** ohne Dämpfung

![](Working%20Materials/Schwingungen/Elektrischer%20Schwingkreis%20ohne%20Dämpfung.png)

**Skizze** mit Dämpfung

![](Working%20Materials/Schwingungen/Elektrischer%20Schingkreis%20mit%20Dämpfung.png)

### Vergleich elektrischer Schwingkreis mit Federschwinger

| Schwingkreis                                 | Federschwinger                                    |
| -------------------------------------------- | ------------------------------------------------- |
| Kondensator wird geladen (maximale Spannung) | Wird gespannt (maximale Auslenkung)               |
| Wird mit Spule verbunden (Schalter umlegen)  | Massestück wird losgelassen                       |
| Spannung nimmt ab; Stromstärke wird größer   | Auslenkung nimmt ab, Geschwindigkeit wird größer  |
| Spannung ist null; Stromstärke maximal       | Auslenkung ist null; Geschwindigkeit maximal      |
| Spannung nimmt zu; Stromstärke wird kleiner  | Auslenkung nimmt zu; Geschwindigkeit wird kleiner |
| Spannung maximal; Stromstärke ist null       | Auslenkung maximal; Geschwindigkeit ist null      |

- Energie Schwingkreis
	- $E_{el}=\frac{1}{2}CU^{2}$
	- $E_{mag}=\frac{1}{2}LI^{2}$

- Energie Federschwinger
	- $E_{pot}=\frac{2}{2}Dy^{2}$
	- $E_{kin}=\frac{1}{2}mv^{2}$

### Ohne Dämpfung


$U_{L}=-L \frac{dI}{dt}=-L \frac{d}{dt}(\frac{dQ}{dt})=-L \frac{d^{2}Q}{dt^{2}}$

$U_{L}=U_{C}$
$-L \frac{d^{2}Q}{dt^{2}}=\frac{Q}{C}$

$-\frac{d^{2}Q}{dt^{2}}=\frac{1}{LC}Q$

$w_{0}=\sqrt{\frac{1}{LC}}$
$f_{0}=\frac{1}{2\pi}\sqrt{\frac{1}{LC}}$

### Mit Dämpfung

$U_{l}=U_{R}+U_{C}$
$U=R \cdot I=R \frac{dQ}{dt}$
$-L \frac{d^{2}Q}{dt}=R \frac{dQ}{dt}+ \frac{Q}{C}$
$\omega=\sqrt{\omega_{0}^{2}-\delta^{2}}\quad\text{ mit }\delta= \frac{R}{2L}$

### Rückkopplungsschaltung nach Meißner

**Rückkopplung**: Periodische Zufuhr von Energie in einem schwingenden System.+

**Schaltplan**
![](Working%20Materials/Schwingungen/Rückkopplungsschaltung.png)

Mit dem Regelbaren Widerstand wird der Arbeitspunkt des Transistors eingestellt. Durch den Schwingkreis wird über die Spule $L_{S}$ eine Wechselspannung in $L_{R}$ induziert. Dadurch liegt auch ein Wechselstrom $I_B$ an der Basis an. Wenn $I_{B}$ maximal ist, schaltet der Transistor in Durchlassrichtung und der Kondensator im Schwingkreis wird wieder auf die maximale Spannung geladen.

**Anwendungen Schwingkreise**: Radio, Fernsehtechnik, Funktechnik

### Wechselstromkreis

**Effektivwert**

$U(t)=R \cdot i(t)$

Wechselstrom: $P=u(t)\cdot i(t)=R \cdot i(t)^{2}$

Gleichstrom: $P=UI=RI^{2}$

Welcher Gleichstrom wäre nötig, um die gleiche Leistung zu bekommen, wie im Mittel bei dem Wechselstrom?

Herleitung

$RI_{eff}^{2}=R \frac{1}{T}\displaystyle\int_{0}^{T}{\hat{I}\sin^{2}{(\omega t)}}dt=R \frac{1}{T} \frac{\hat{I}}{2}T$
$I_{eff}^{2}=\frac{\hat{I}^{2}}{2}$

$I_{eff}=\frac{\hat{I}}{\sqrt{2}}$
$U_{eff}=\frac{\hat{U}}{\sqrt{2}}$

### Zeigerdiagramme

**Widerstand**

#### Kondensator im Wechselstromkreis

**Kondensator**

Der Strom eilt der Spannung um $\frac{\pi}{2}$ voraus.
Kapazitiver Widerstand: 
$U=\hat{U}\sin{\omega t}$
$I=\frac{dQ}{dt}=C \frac{dU}{dt}$
$I=C \frac{dU}{dt}=C\hat{U}\omega\cos{(\omega t)}=\hat{I}\cos{(\omega t)}$
$U=X_{C}\cdot I\to X_{C}=\frac{U}{I}=\frac{\hat{U}}{C\hat{U}\omega}=\frac{1}{C\omega}$

#### Spule im Wechselstromkreis

![](Working%20Materials/Schwingungen/Spule%20Im%20Wechselstromkreis.png)

$U=-L \frac{dI}{dt}$
$I=\hat{I}\sin{(\omega t)}$

$U=-L \frac{d}{dt}\big(\hat{I}\sin{(\omega t)}\big)=-L \omega \hat{I}\cos{(\omega t)}$

**induktiver Widerstand**

$X_{L}=\frac{\hat{U}}{\hat{I}}=\frac{L\omega\hat{I}}{\hat{I}}=L \omega$

### Reihenschaltung von Spule, Kondensator & Widerstand

(Siebkette, Siebkreis, Bandpass)

**Zeigerdiagramm**

![](Working%20Materials/Schwingungen/Reihenkondensator.png)

$U_{R}$ ist Phasenverschoben zur Stromstärke
$U_C$ ist der Stromstärke hinterher
$U_L$ ist der Stromstärke voraus

$\hat{U}_{ges}=Z \cdot\hat{I}$
$Z=\frac{\hat{U}_{ges}}{\hat{I}}=\frac{\sqrt{\hat{U}_{R}^{2}+(\hat{U}_{L}+\hat{U}_{C})^{2}}}{\hat{I}}=\frac{\sqrt{R^{2}\hat{I}^{2}+((\omega L)+ \frac{1}{\omega C} \hat{I})^{2}}}{\hat{I}}=\frac{\sqrt{\hat{I}^{2}+(R^{2}+ (\omega L-\frac{1}{\omega C} \hat{I}))^{2}}}{\hat{I}}=\sqrt{R^{2}+(\omega L- \frac{1}{\omega C})^{2}}$

Allgemein:
$Z=\sqrt{R^2+X^{2}}$
$\text{Imdepedanz}=\sqrt{\text{ohmscher Widerstand}^{2}+\text{Reaktanz}^{2}}$

### Frequenzabhängigkeit der Impedanz

$\lim\limits_{\omega\to0}Z=\lim\limits_{\omega\to0}\sqrt{R^{2+(\omega L- \frac{1}{\omega C})^{2}}}=\infty\to I=0$
$\lim\limits_{\omega\to\infty}Z=\lim\limits_{\omega\to\infty}\sqrt{R^{2}+(\omega L- \frac{1}{\omega C})^{2}}=\infty\to I=0$

$Z$ ist minimal für: $\omega L- \frac{1}{\omega C}=0\to I=I_{\text{max}}$

### Hochpass und Tiefpass

### Leistung im Wechselstromkreis

$P_{S}=U \cdot I=\sqrt{P_{W}^{2}+P_{B}^{2}}$
$P_{W}=U \cdot I \cdot\cos{\varphi}$
$P_{B}=U \cdot I \cdot\sin{\varphi}$

# Wellen

> Eine mechanische Welle ist die Ausbreitung einer Störung (mechanischer Schwingung) im Raum. Es erfolgt ein Energietransport, aber kein Stofftransport.

Wird die Welle durch eine harmonische Schwingung angeregt, spricht  man von einer harmonischen Welle.

## Wellentypen

### Transversalwelle

- Schwingungsrichtung steht quer zur Ausbreitungsrichtung
- Bsp.: Seilwelle

### Longitudinalwelle

- Schwingungsrichtung und Ausbreitungsrichtung sind parallel
- Bsp.: Schallwelle

### Kreiswelle

- Überlagerung von Longitudinal und Transversalwelle => Kreiswelle
- Bsp.: Wasserwelle

## Beschreibung mechanischer Wellen

$y(t)$-Diagramm Schwingung eines Wellenteilchens an einem bestimmten Ort X.

## Ausbreitungsgeschwindigkeit

$\lambda=c \cdot T$
$c=\lambda \cdot \frac{1}{T}=\lambda \cdot f$

## Wellenfunktion

$y(x,t)=\hat{y}\sin{(2\pi[ \frac{t}{T}- \frac{x}{\lambda}])}$

Minus bei Ausbreitung in positiver x-Richtung.

Herleitung
$y(t)=\hat{y}\sin{(\omega t)}$
$y(t)=\hat{y}\sin{(\omega[t_{1}-\Delta t])}$
$y(t)=\hat{y}\sin{(2\pi f[t_{1}-\Delta t])}$
$y(t)=\hat{y}\sin{(2\pi[t_{1} \cdot f-\Delta t \cdot f])}$
$y(t)=\hat{y}\sin{(2\pi[\frac{t_{1}}{T}- \frac{\delta x}{\lambda}])}$

$y(t,x)=\hat{y}\sin{(2\pi[\frac{t}{T}- \frac{x}{\lambda}])}$

## Huygensches Prinzip

Jeder Punkt einer Wellenfront ist Ausgangspunkt einer kugelförmigen Elementarwelle. Diese Elementarwelle besitz die gleiche Ausbreitungsgeschwindigkeit wie die ursprüngliche Welle. Die Elementarwellen überlagern sich und die Einhüllende aller Elementarwellen bildet die neue Wellenfront.

![](Working%20Materials/Schwingungen/Huygensches%20Prinzip.jpeg)

### Reflexion

Jeder Punkt einer Wellenfront ist Ausgangspunkt einer kugelförmigen Elementarwelle. Die Überlagerung vieler Elementarwellen bildet die neue Wellenfront (einhüllende Wellenfront).
Läuft die Wellenfront von links schräg aur ein Hindernis, so trifft zunächst ein Teil dieser Wellenfront in einem Punkt $P_{1}$ auf die Grenzfläche von Hindernissen. Danach treffen weitere Teile der Wellenfront auf die Grenzfläche in den Punkten $P_{2},P_{3},\dots$ (von links nach rechts). Alle diese Punkte sind Ursprungspunkte von Elementarwellen, deren Wellenfronten die Wellenfront der reflektierten Welle bilden.

- Reflexion bei festem Ende: Es kommt bei der Reflexion zu einem Phasensprung vom Betrag $\pi$ (reflektierte Welle ist um $\frac{x}{2}$ verschoben).
- Reflexion be losem Ende: Reflexion erfolgt ohne Phasensprung.

#### Herleitung Reflexionsgesetz

Da die Wellengeschwindigkeit gleich bleibt, gilt $\bar{AD}=c \cdot t$, $\bar{CB}=c \cdot t$
Beide Dreiecke haben die Seite $\bar{AC}$.
Die beiden Dreiecke sind kongruent zueinander.
Somit gilt $\alpha=\beta$ im Dreieck.

$\frac{\sin{\alpha}}{\cos{\alpha}}=\frac{c_{1}}{c_{2}}$

## Stehende Wellen

Bei der Überlagerung zweier Wellen mit gleicher Frequenz und gleicher Amplitude entsteht ein stabiles Interferenzmuster. Dieses Muster sieht wie eine Welle aus, die sich nicht fortbewegt un wird als stehende Welle bezeichnet. Es bilden sich Orte mit keiner Auslenkung (Knoten) und Orte mit maximaler Auslenkung (Bäuche). Abstand zwischen zwei Bäuche beziehungsweise zwei Knoten beträgt $\frac{\lambda}{2}$ der ursprünglichen Welle.

## Licht als Welle

### Fermatsches Prinzip

Das Licht breitet sich auf den zeitlich kürzesten Weg aus.

### Brechungsindex

$n=\frac{c_{0}}{c_{s}}$
- $c_{0}$ - Vakuum
- $c_{s}$ - Stoff

### Methoden zur Messung der Lichtgeschwindigkeit

#### Bestimmung Lichtgeschwindigkeit im Vakuum

(Siehe Seite 244)

##### Nach Romer (17 Jahrhundert):

##### Nach Fizeau (1848)

$f=12.6Hz$
$d=8633m$
$n=720$

$c=\frac{\Delta s}{\Delta t}$
$\Delta s=2\cdot d$
$T=\frac{1}{f}$
$f_\text{Zahn zu Zahn}=\frac{T}{n}$
$f_\text{Zahn zu Lücke}=\frac{T}{2n}$
$c=\frac{2d}{t_{zl}}=\frac{4dn}{T}=4dnf=4\cdot8633m \cdot720\cdot12.6Hz\approx3.13\cdot10^{8} \frac{m}{s}$

##### Moderne Messungen

(Siehe S. 245)

Laufzeitbestimmmmung mittels Lichtdetektor

$\Delta t= 67ns$
$\Delta s = 20m$
$c=\frac{\Delta s}{\Delta t}=\frac{20m}{67\cdot10^{-9}s}=2.99\cdot10^{8} \frac{m}{s}$
$c=\frac{1}{\sqrt{\epsilon_{0}\cdot\mu_{0}}}$

#### Bestimmung Lichtgeschwindigkeit für verschiedene Stoffe

Brechungsgesetz

$\frac{\sin{\alpha}}{\sin{\beta}}=\frac{c_{1}}{c_{2}}$

$n_{1}=\frac{c_{0}}{c_{1}}$
$n_{2}=\frac{c_{0}}{c_{2}}$
$n_{2}c_{2}=c_{0}=n_{1}c_{1}\to \frac{c_{1}}{c_{2}}=\frac{n_{2}}{n_{1}}$

Lichtgeschwindigkeit mithilfe von Laserentfernungsmesser

Anzeige des Entfernungsmesser $\cases{s_{0}=24.8cm \\ s_{w}=32.2cm}$

Brechung von $c_{w}$ und $n_{w}$

$c_{0}=\frac{s_{0}}{t_{0}}$
$c_{w}=\frac{s_{0}}{t_{w}}$

Anzeige $s_{w}=c_{0}\cdot t_{w}=c_{0}\cdot \frac{s_{0}}{c_{w}}\to s_{w}=\frac{c_{0}s_{0}}{c_{w}}\to c_{w}=\frac{c_{0}s_{0}}{s_{w}}=3\cdot10^{8} \frac{m}{s}\cdot \frac{25cm}{32cm}$
$s_{w}=\approx2.34\cdot10^{8} \frac{m}{s}$
$n_{w}=\frac{c_{0}}{c_{w}}=\frac{s_{w}}{s_{0}}=\frac{32cm}{25cm}=1.28$

### Reflexion, Brechung und Beugung

#### Nachweis Reflexionsgesetz

Mithilfe einer Winkelscheibe Einfallswinkel $\alpha$ und Reflexionswinkel $\alpha'$ messen.

### Beugung von Licht

*Erläuterung mittels Huygenschen Prinzipes*

Jeder Punkt auf einer Wellenfront ist Ursprung einer kugel-/kreisförmigen Elementarwelle. Diese Elementarwellen breiten sich mit der gleichen Geschwindigkeit aus wie die ursprüngliche Welle. Die einhüllende Überlagerung der Wellenfronten der Elementarwellen bildet die neue Wellenfront.

Nach dem Huygenschen Prinzip ist der Punkt $P$ (Teil der Wellenfront, die auf das Hindernis trifft) Ursprung einer kugelförmigen Elementarwelle, die sich in den geometrischen Schattenraum des Hindernisses ausbreitet.

## Interferenz und Polarisation

### Interferenz am Doppelspalt/Gitter

*Für den Doppelsplat gilt*

$a$ Abstand Doppelspalt zu Schirm
$b$ Abstand Spalte
$s_{n}$ Abstand Maximum $n$-ter Ordnung zu $0$-te Ordnung
$\alpha_{n}$ Winkel zwischen Maxima und 

$\tan{\alpha_{n}}=\frac{s_{n}}{a}$

$\sin{\alpha_{n}}=\frac{n\cdot\lambda}{b}$

Für kleine Winkel $\alpha_{n}$ gilt $\sin{\alpha_{n}}\approx\tan{\alpha_{n}}\quad(a\ge10\cdot s_{n})$
$$\frac{s_{n}}{a}\approx \frac{n\cdot\lambda}{b}\quad(n\in\mathbb{N})$$

*Die Gleichung gelten auch für das Gitter*

Gitterkonstante $G$ gibt an, wie groß der Abstrand zwischen den Öffnungen des Gitters sind $G=\frac{1}{b}$
**Beispiel** $G=\frac{1}{100\frac{1}{mm}}$

Das Licht, das durch einen dritten Spalt auf den Schirm trifft, hat den gleichen Gangunterschied zur Lichtwelle des zweiten Splats, wie die Lichtwelle vom 2. Spalt zum 1. Spalt. Weitere Spaltöffnungen verändern nicht die Lage der Maxima, sondern nur deren Intensität, da mehr Licht beim Gitter hindurchdringt.

Beugung in Abhängigkeit von der Wellenlänge

Näherungsformel $\frac{s_{n}}{a}=\frac{n\cdot\lambda}{b}\to s_{n}=\frac{n\cdot\lambda\cdot a}{b}$

Je größer die Wellenlänge, desto größer der Abstand der Maxima. Rotes Licht wird stärker gebeugt als blaues Licht.

**Einfluss $a$** Je größer $a$, desto größer der Abstand der Maxima
**Einfluss $b$** Je größer $b$, desto kleiner der Abstand der Maxima

### Kohärentes Licht

Interferenzmuster kommen nur bei kohärentem Licht zustande. Das heißt, dass die Wellenzüge ausreichend lang sind, um zu interferieren und die gleuche Frequenz besitzen.

### Interferenz an dünnen Schichten

An dünnen Schichten tritt bei Reflexion konstruktive Interferenz (Verstärkung) auf, wenn der Gangunterschied zwischen den an Vorder- und Rückseite reflektierten Wellen ein ganzzahliges Vielfaches von $\lambda$ beträgt.
1. Lichtstrahlen unterschiedlicher Wellenlänge (Farben) werden unterschiedlich gebrochen (Dispersion) und teilweise reflektiert.
2. Lichtstrahlen werden an der Innenseite der dünnen Schicht reflektiert.
3. Beim Austreten von Lichtstrahlen aus der dünnen Schicht überlagern sich diese Lichtstrahlen, die an der Oberfläche reflektiert werden.

Gangunterschied für Maxima:
$$2d=(2k+1) \frac{\lambda_\text{Medium} }{2}=(2k+1) \frac{\lambda}{2n_{F}}$$

Gangunterschied für Minimum:
$$2d=(k+1) \lambda_\text{Medium}=(k+1) \frac{\lambda}{n_{F}}$$
### Newtonsche Ringe

Beim reflektierten Licht kommen die Interferenzerscheinungen durch das einerseits an der  Rückseite der Linse reflektierte Licht und andererseits dan an der Vorderseite der Glasplatte reflektierte Licht zustande (schwarze Strahlen).

### Interferenzmuster an aufgespannter Seifenschicht

**Dunkler Bereich**
Schichtdichte geht gegen Null
- Phasenverschiebung fast nur durch Phasensprung $\frac{\lambda}{2}$ durch Reflexion
- Destruktive Interferenz

**Gelblicher Bereich**
Schichtdichte nimmt nach unten hin zu
- Licht mit kürzester Wellenlänge, als blaues/violettes Licht interferiert als erstes destruktiv
- Andere Lichtwellenlängen (Farben) werden normal reflektiert
- blaues Licht fehlt im reflektierten Licht
- Gelbfärbung

## Polarisation

Licht natürlicher Lichtquellen (Sonne, Feuer) sowie der meisten künstlichen Lichtquellen (Glühlampen, Leuchtstoffröhre) schwingt in den unterschiedlichen Richtungen. Laserlicht schwingt dagegen nur in eine Richtung (es ist linear polarisiert).

### Faraday-Effekt

Die Polarisationsebene einer linear polarisierten Lichtwelle kann in einem Medium (z.B. Glas) gedreht werden, wenn darin ein Magnetfeld parallel zur Ausbreitungsrichtung der Wellen herrscht. Aus dieser Beobachtung kann man schlussfolgern, dass es sich bei Licht um eine elektromagnetische Welle handelt.

### Gesetz von Malus

$I_{t}=I_{e}\cos^{2}{\vartheta}$

## Brewstersches Gesetz

Stehen reflektierter und gebrochener Lichtstrahl an der Grenzfläche zweier Stoffe senkrecht zueinander, dann ist das reflektierte Licht vollständig linear polarisiert.
$$\frac{n_{2}}{n_{1}}=\tan{\alpha_{p}}$$

Herleitung Brewster-Winkel
$\frac{\sin{\alpha}}{\sin{\beta}}=\frac{n_{2}}{n_{1}}\implies\frac{\sin{dp}}{\sin{90-dp}}=\frac{\sin{dp}}{cos{dp}}=\frac{n_{1}}{n_{2}}\implies\tan{\alpha}=\frac{n_{2}}{n_{1}}$

### Doppelbrechung

Stoffe, bei denen Doppelbrechung auftreten, nennt man optisch anisotrop. Die anderen Stoffe heißen optisch isotrop.

### Flüssigkeitskristallanzeigen

(LCD - Liquid Cristal Display)

![](Working%20Materials/Interferenz/Flüssigkeitskristallanzeigen.png)

### Herleitung Brechungsgesetz nach Fermatschen Prinzip

$t(x)=\frac{l_{1}}{c_{1}}+ \frac{l_{2}}{c_{2}}=\frac{\sqrt{a^{2}+x^{2}}}{c_{1}}+\frac{\sqrt{b^{2}+(d-x)^{2}}}{c_{2}}$
$\frac{dt}{dx}=0=\frac{1}{c_{1}}(a^{2}+x^{2})^{\frac{-1}{2}}\cdot x+\frac{1}{c_{1}}(b^{2}+(d-x)^{2})^{\frac{-1}{2}}\cdot(d-x)\cdot(-1)$
$0=\frac{x}{c_{1}\sqrt{a^{2}+x^{2}}}- \frac{d-x}{c_{2}\sqrt{b^{2}+(d-x)^{2}}}$
$0=\frac{x}{c_{1}l_{1}}- \frac{d-x}{c_{2}l_{2}}$

$\sin{\alpha}=\frac{x}{l_{1}}\quad\sin{\beta}=\frac{d-x}{l_{2}}$
$0=\frac{\sin{\alpha}}{c_{1}}- \frac{\sin{\beta}}{c_{2}}$
$\frac{\sin{\alpha}}{c_{1}}=\frac{\sin{\beta}}{c_{2}}$
$\frac{\sin{\alpha}}{\sin{\beta}}=\frac{c_{1}}{c_{2}}$

# Quantenphysik

$E_{\text{ph}}=h\cdot f_{g}$
$E_{\text{ph}}=f\cdot f_{uv}$
$f_{g}<f_{uv}$
$E_{\text{ph, gelb}}<E_{\text{ph, uv}}$

## Fotoeffekt

Als äußeren photoelektrischen Effekt bezeichnet man das Herauslösen von Elektronen aus einer Halbleiter- oder Metalloberfläche durch Bestrahlung.

## Modelle für das Licht

| Modell Lichtstrahlen                                         | Modell Wellen                                          | Modell Teilchen                            |
| ------------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------ |
| Eignet sich zur Beschreibung des Wegs, den Licht zurücklegt. | Eignet sich zu Erklärung von Beugung und Interferenz. | Eignet sich zur Erklärung des Fotoeffekts. |
| Keine Aussage zur Natur des Lichts                           | Licht hat Wellencharakter                              | Licht hat Teilchencharakter                |

## Energie eines Photons

$h$ plankschens Wirkungsquantum mit $6.626\cdot10^{-34}Js$
$f$ Frequenz
$$E_\text{ph}=h\cdot f$$

### Äußere lichtelektrischer Effekt im Photonenmodell

$E_{\text{ph}}=W_{A}+E_{\text{kin}}$

### Energiebilanz

### Gegenfeldmethode

![](Working%20Materials/Quantenphysik/Photoeffekt.png)

![](Working%20Materials/Quantenphysik/Bewegung%20der%20Elektronen.png)

- Regelbare Spannungsquelle ist zwischen Kathode und Anode angeschlossen
- Gegenspannung an der regelbaren Spannungsquelle wird so eingestellt, dass die Stromstärke null ist ($I=0$)
- Mithilfe der Gegenspannung U kann die kinetische Energie der herausgelösten Elektronen bestimmt werden: $E_\text{kin}=e\cdot U$

### Einstein-Gerade

Anstieg der Einstein-Gerade ist das plancksche Wirkungsquantum $h$.

$E_\text{ph}=E_\text{kin}+W_{A}$
$E_{\text{kin}}(f)=W_{A}+h\cdot f\to m+n\cdot x$

### Impuls-Photon

$E=m\cdot c^{2}$
$E=h\cdot f$

$m\cdot c^{2}=h\cdot f$
$mc=h\cdot \frac{f}{c}$
$$p=h\cdot \frac{f}{c}=\frac{h}{\lambda}$$
$$m=\frac{h\cdot g}{c^{2}}$$

## Materiewellen

### De-Broglie-Wellenlänge

### Leuchtdiode

Umkehrung des lichtelektrischen Effekts.

