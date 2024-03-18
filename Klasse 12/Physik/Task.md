---
author: karlz
tags: 
- Physik
- FGN
---

# Schwingungen

## 2023-08-30

Amplitude: Maximaler Auslenkungswinkel $\hat{\alpha}$

$T=3s$
$f=\frac{1}{3}s^{-1}=\frac{1}{3}Hz$

Amplitude: Maximale Auslenkung der Stimmbänder $\hat{y}$

$T=\frac{1}{20}s$
$f=20Hz$

- - -

$y_{max}=U=325V$
$f=50Hz$

$y(t)=y_{max}*\sin{(2\pi*f*t)}=325V*\sin{(2\pi*50Hz*t)}$

## 2023-09-04

$R=6357km$
$\omega=\sqrt{\frac{g}{R}}$
$y(t)=R\cos{(\omega t)}$

$y(t)=6357km\cos{\bigg(\sqrt{\frac{9.81\frac{km}{s^{2}}}{1.24 \cdot10^{-3}s^{-1}}}\cdot t\bigg)}$

$v(t)=-R \omega\sin{(\omega t)}=-7.88 \frac{km}{s}\sin{(1.24 \cdot10^{-3}s^{-1}t)}$
$a(t)=-R \omega^{2}\cos{(\omega t)}=-9.77 \frac{m}{s^{2}} \cos{(1.24\cdot10^{-3}s^{-1}t)}$

$a(t)=-R \omega^{2}\cos{(\omega t)}=-g \cos{(\omega t)}$
$y(t)=R\cos{\omega t}$

$R \omega^{2}=g$
$\omega=\sqrt{\frac{g}{R}}$

$a(t)\sim y(t)$
$a(t)\sim-\omega^{2}y(t)$

## 2023-09-06

$f_{0}=\frac{1}{2\pi}\sqrt{\frac{D}{m}}$

$\lim\limits_{D\to\infty}f_{0}=\infty$
$\lim\limits_{D\to0}f_{0}=0$

$\lim\limits_{m\to\infty}f_{0}=0$
$\lim\limits_{m\to0}f_{0}=\infty$

Begründung
Es gilt $F=D \cdot y(t)=m \cdot a$. Da bei gleicher Kraft die Masse steigt, ist relativ gesehen die Federkonstante kleiner, und umgekehrt.

## 2023-09-11

|     | 1   | 6   | 7   |
| --- | --- | --- | --- |
| B   | 119 | 30  | 11  |
| A   | 122 | 31  | 17  |

B: Absolut/Reibungskraft = konst.
A: Relativ/Reibungskraft ~ Geschwindigkeit

- - -

$m=2kg$
$D=400 \frac{N}{m}$
$x=0.03m$

$T=2\pi\sqrt{\frac{D}{m}}=0.444s$
$E_{ges}=\frac{1}{2}Dx^{2}=0.18J$

- - -

$E_1=0.99E_0$
$E_2=0.99*0.99E_1$

$\frac{E_{1}}{E_{2}}=0.99=\frac{\frac{1}{2}D\hat{y}_{1}^{2}}{\frac{1}{2}D\hat{y}_{0}^{2}}\to \frac{\hat{y}_{1}}{\hat{y}_{0}}=\sqrt{0.99}$
$\hat{y}(t)=\hat{y}_{0}e^{-\delta t}\quad\text{ mit }\delta=\frac{b}{2m}$
$\hat{y}_{1}=\hat{y}(t=T)=\hat{y}_{0}^{-\delta T}$
$\frac{\hat{y}_{1}}{\hat{y}_{2}}=\frac{\hat{y}_{0}e^{-\delta T}}{\hat{y}_{0}}=\sqrt{0.99}\to e^{-\delta T}=\sqrt{0.99}$
$e^{-\delta T}=\sqrt{0.99}$
$-\delta T=\ln{\sqrt{0.99}}=\ln{0.99^{\frac{1}{2}}}=\frac{1}{2}\ln{0.99}$
$\delta=\frac{-\ln{0.99}}{2T}$
$\frac{b}{2m}=\frac{-\ln{0.99}}{2T}$
$b=\frac{-m\ln{0.99}}{T}=\frac{-2kg\ln0.99}{0.444s}=0.045 \frac{kg}{s}$

## 2023-09-18

Wenn sich die Eigenfrequenz verkleinert, dann vergrößert such die Periodendauer ($f=\frac{1}{t}$ bzw. $T=\frac{1}{f}$). Eine größere Kapazität vergrößert die Dauer der Entlade- und Ausladevorgangs des Kondensators und somit die Periodendauer. Daraus folgt eine kleinere Frequenz.
Eine größere Induktivität vergrößert die Dauer für den "Aufbau" eines elektrischen Stroms im Schwingkreis. Somit wird auch hier die Periodendauer größer. Daraus folgt eine kleinere Frequenz.

- - -

$L=10L_{0}$
$C=10C_{0}$
$f_{0}=\frac{1}{2\pi \cdot\sqrt{10L_{0} \cdot 10C_{0}}}=\frac{1}{10} \frac{1}{2\pi} \sqrt{\frac{1}{C_{0}L_{0}}}$

- - -

$C=100pF$
$f_{0}=2.8 Mhz$

$f_{0}=\frac{1}{2\pi \sqrt{L \cdot C}}$
$\sqrt{L \cdot C}=\frac{1}{f_{0}2\pi}$
$L \cdot C=(\frac{1}{f_{0}2\pi})^{2}$
$L=\frac{(\frac{1}{f_{0}2\pi})^{2}}{C}=3.2309 \cdot10^{-5}H$

- - -

Kondensator einmalig mittels  einer Gleichspannungsquelle aufladen.

Wechselspannungsquelle direkt an Schwingkreis schließen.

![](Working%20Materials/Schwingungen/Wechselspannungsquelle.png)

Durch Induktion über eine zweite Spule.
![](Working%20Materials/Schwingungen/Induktion%20über%20Spule.png)

- - -

$U_{C}=\hat{U}\cos{(\omega t)}$

$Q=CU$
$I=\frac{dQ}{dt}=C \frac{dU}{dt}=-C\hat{U}\omega\sin{\omega t}$

$\omega^{2}=\frac{1}{LC}$

$E_{el}=\frac{1}{2}CU^{2}=\frac{1}{2}C\hat{U}^{2}\cos^{2}{(\omega t)}$
$E_{mag}=\frac{1}{2}LI^{2}=\frac{1}{2}LC^{2}\omega^{2}\hat{U}^{2}\sin^{2}{(\omega t)}=\frac{1}{2}C\hat{U}^{2}\sin^{2}{(\omega t)}$

$E_{ges}=E_{mag}+E_{el}=\frac{1}{2}C\hat{U}^{2}\sin^{2}{(\omega t)}+\frac{1}{2}C\hat{U}^{2}\cos^{2}{(\omega t)}=\frac{1}{2}C\hat{U}^{2}(\sin^{2}{(\omega t)}+\cos^{2}{(\omega t)})=\frac{1}{2}C\hat{U}^{2}$
## 2023-09-20

![](Working%20Materials/Schwingungen/Induktiver%20Widerstand.png)

---

$L=0.2H$
$C=100\mu F=10\cdot10^{-4}F$

$X_{C}=\frac{1}{C\omega}$
$f=\frac{1}{T}=\frac{\omega}{2\pi}$
$10\cdot10^{-4}F \cdot2\pi f=\frac{1}{10\cdot10^{-4}F\cdot2\pi f}$
$f=35.589Hz$

## 2023-09-25

$y(t)=5cm \cdot\sin{(\omega t)}$ mit $\omega=\frac{2\pi}{T}$
$T=2s$
$\lambda=2 \frac{m}{s}$

Amplitude $\hat{y}=5cm$
Periodendauer $T=2s$
Frequenz $f=\frac{1}{T}=\frac{1}{2s}$
Wellenlänge $\lambda=\frac{c}{f}=4m$

$y(t,x)=\hat{y}\sin{( \frac{2\pi t}{2s}- \frac{2\pi x}{4\frac{m}{s}})}=\hat{y}\sin{(\pi (\frac{t}{s}- \frac{x}{2\frac{m}{s}}))}$

$f=\frac{1}{T}=\frac{1}{0.75m}$
$\lambda=0.8s$

$y(t)=4cm\sin{(2\pi(\frac{t}{0.8s}-\frac{x}{0.75m}))}$

# Wellen

## 2023-10-23

Die Flasche ist eine Röhre mit einem festen Ende (Wasserspiegel) und einem losem Ende (Flaschenöffnung). So entstehen durch das Anpusten stehende Wellen.

Mit steigendem Wasserspiegle verringert sich die Länge der Röhre. Nach der Bedingung: $$\lambda = \frac{4L}{2n-1}$$
Nimmt die Wellenlänge mit kleiner werdender Länge $L$ ab. Da die Schallgeschwindigkeit konstant bleibt, gilt: $f=\frac{1}{\lambda}$
Somit steigt die Frequenz beziehungsweise Tonhöhe für geringere Längen $L$.

---

$L=2.4m$
$f_{n}=\frac{c}{\lambda}=c\frac{2n-1}{4L}$
$f_{1}=0.104 \cdot 343 Hz$
$f_{2}=0.3125 \cdot 343 Hz$
$f_{3}=0.521 \cdot 343 Hz$

$f_{n}=\frac{c}{\lambda}=\frac{c n}{2L}$
$f_{1}=0.208 \cdot 343 Hz$
$f_{2}=0.42 \cdot 343 Hz$
$f_{3}=0.625 \cdot 343 Hz$

---

$L=45cm=0.45m$
$f=\frac{c}{\lambda}=\frac{343 \frac{m}{s}}{2\cdot0.45}=381 Hz$

## 2023-10-25

$\Delta y=0.1 \frac{\mu s}{cmm}$
$\Delta t=40ns$
$\Delta x\text{ in cm}$

$\Delta x=\frac{\Delta t}{\Delta y}=\frac{40ns}{0.1 \frac{\mu s}{cm}}=\frac{0.04\mu s}{0.1 \frac{\mu s}{cm}}=0.4cm$

$d=6mm$
$d=c\cdot t$
$t=b\cdot\Delta y=6mm\cdot0.1 \frac{\mu s}{cm}=0.6cm\cdot0.1 \frac{\mu s}{cm}=0.06\mu s$
$d=\frac{1}{2}\cdot3\cdot10^{8} \frac{m}{s}\cdot0.06\mu s=\frac{1}{2}\cdot3\cdot10^{8} \frac{m}{s}\cdot0.06\cdot10^{-6}s\approx9m$

---

| Eintritt | Ausdritt | Verhältnis |
| -------- | -------- | ---------- |
| 10       | 8        | 1.248      |
| 20       | 15       | 1.321      |
| 30       | 20       | 1.462      |
| 40       | 25       | 1.521      |
| 50       | 30       | 1.532      |
| 60       | 36       | 1.473      |

$\frac{\sin{\alpha}}{\sin{\beta}}=1.432$

$\frac{\sin{\alpha}}{\sin{\beta}}=\frac{c_{0}}{c_{s}}=\frac{c_{0}}{\frac{\sin{\alpha}}{\sin{\beta}}}=3\cdot10^{8} \frac{\frac{m}{s}}{1.52}\approx=1.97\cdot10^{8} \frac{m}{s}$

## 2023-11-06

$c=3\cdot10^{8} \frac{m}{s}$
$x=384000000m$
$s=v\cdot t$
$t=\frac{s}{v}=\frac{384\cdot10^{6}m}{3\cdot10^{8} \frac{m}{s}}=1.28s$

---

$\varphi=0.02^{\circ}$
$x=384000000m$

$\tan{\frac{\varphi}{2}}=\frac{\frac{d}{2}}{x}$
$d=\tan{\frac{\varphi}{2}}\cdot 2x$

---

$a=3m=3000mm$
$b=0.5mm$
$s_{n}=4mm$
$n=1$

$\frac{s_{n}}{a}\approx \frac{n\cdot\lambda}{b}\quad(n\in\mathbb{N})$
$\lambda=\frac{s_{n}\cdot b}{n\cdot a}=6.67\cdot10^{-4}mm$

---

$n_\text{rot}=1.51$
$n_\text{blau}=1.52$
$\alpha=45^{\circ}$
$a=2m$

Für Rot
$\frac{\sin{\alpha_{1}}}{\sin{\beta_{1}}}=\frac{n_{1}}{n_{2}}$
$\beta_{1}=\arcsin{(\frac{n_{\text{Licht}}}{n_\text{Glas}}\cdot\sin{\alpha_{1}}})=27.92^{\circ}$
$60^{\circ}+2\cdot90^{\circ}+\delta=360^{\circ}$
$\delta=120^{\circ}$
$\alpha_{2}=180^{\circ}-\beta_{1}-\delta=32.08$
$\beta_{2}=\arcsin{(\frac{n_\text{Glas}}{n_{\text{Licht}}}\cdot\sin{\beta_{1}}})=53.82^{\circ}$

Für Blau
$\beta_{1}=27.723^{\circ}$
$\alpha_{2}=32.2767^{\circ}$
$\beta_{2}=54.2617^{\circ}$

$\tan{\frac{\beta_{b}-\beta_{r}}{2}}=\frac{\frac{b}{2}}{a}$
$2\cdot a\cdot\tan{\frac{\beta_{b}-\beta_{r}}{2}}$
$a=3.2m$

## 2023-11-08

$n_{G}=1.53$
$\lambda=550nm$
$n_{V}=1.35$

$n_{L}<n_{V}<n_{G}$

$2d=\frac{\lambda}{2n_{V}}\quad\text{für }k=0$
$d=\frac{\lambda}{4n_{V}}=101.85nm$

## 2023-11-20

Ein Polarisatiosfilter schwächt die Intensität des unpolariesierten Lichtes der Glühlampe um die Hälfte ab und polarisiert es.
- Unpolarisiertes Licht wird zu polarisierten Licht
- Anteil des Lichts, welches parallel zur Transmissionsrichtung des Filters orientiert ist, wird durchgelassen
- Orientierung senkrecht zum Filter wird vollständig absorbiert
- Orientierung schräg zum Filter ($0^{\circ}<\vartheta<90^{\circ}$) wird teilwiese transmittiert (paralleler Anteil)
- Lichtstärke/Intensität wird um die Hälfte reduziert

# Quantenphysik

## 2023-11-29

$\lambda=400nm\cdot800nm$
$t=\mu s$
$n=10^{12}$

$P=\frac{E}{t}=\frac{n\cdot g\cdot f}{t}=\frac{n\cdot h\cdot c}{t\cdot\lambda}=\frac{10^{12}\cdot 6.626\cdot10^{-34}Js\cdot 3\cdot10^{8} \frac{m}{s}}{10^{-6}s\cdot600\cdot10^{-9}m}=0.33W$

---

$P=1.7\cdot10^{-18}W$
$\lambda=550nm$

$P=\frac{n\cdot h\cdot c}{t\cdot\lambda}$
$\frac{n}{t}=\frac{P\cdot\lambda}{h\cdot c}=\frac{4.7037}{s}\approx5\text{ Photonen pro Sekunde}$

---

Es wird Licht gleicher Frequenz, aber höherer Intensität verwendet. Sagen sie vorher, was dadurch bewirkt wird!

Eine höhere Intensität bedeutet eine größere Anzahl an Photonen. Dadurch werden auch mehr Elektronen ausgelöst. 

Es wird Licht höherer Frequenz, aber gleicher Intensität verwendet.

Eine höhere Frequenz bedeutet, dass die Photonen eine größere Energie. Da die Ablösearbeit gleich bleibt, besitzen die Elektronen eine größere kinetische Energie.

---

Argumentieren Sie, weshalb das Wellenmodell beim Photoeffekt ungeeignet ist.

## 2023-12-04

$m_\text{Elektron}=m_\text{Photon}$

$m_{\text{Elektron}}=9.1\cdot10^{-31}kg$
$m_\text{Photon}=\frac{h\dot f}{c^{2}}=\frac{h}{\lambda\cdot c}$
$\lambda=\frac{h}{c\cdot m}=\frac{6.626\cdot10^{-34}Js}{3\cdot10^{8}\cdot9.1\cdot10^{-31}kg}=2.43\cdot10^{-12}m$

---

| 400    | 450     | 500  | 550     | 600  |
| ------ | ------- | ---- | ------- | ---- |
| 7.5e14 | 6.67e14 | 6e14 | 5.45e14 | 5e14 |
| 1.25   | 0.9     | 0.62 | 0.4     | 0.17 |
34-1
$h=4.27\cdot10^{-15}eVs=6.83\cdot10^{-34}Js$

Schnittpunkt mit y-Achse $W_{A}=1.944eV$
Schnittpunkt mit x-Achse $f_{G}=4.56\cdot10^{14}Hz$

$m_{\text{Elektron}}=9.1\cdot10^{-31}kg$
$E_\text{kin}=\frac{1}{2}mv^{2}=h\cdot f-W_{A}$
$v=\sqrt{\frac{2E_{\text{kin}}}{m}}$

| Ekin \[eV] | 1.25   | 0.9    | 0.62   | 0.4    | 0.17   |
| ---------- | ------ | ------ | ------ | ------ | ------ |
| v \[m/s]   | 663080 | 562642 | 466989 | 375095 | 244532 |

---

$\lambda=[400:800]nm=\approx600nm$
$\Delta t=1\mu s$
$n=10^{12}$

$P=\frac{W_A}{\delta t}=\frac{h\cdot f}{t}=\frac{h\cdot c}{\lambda\cdot t}=\frac{6.6261\dot10^{-34}Js\cdot3\cdot10^{8}}{600nm\cdot1s}$

---

$\lambda=460nm$
$E_{kin}=1.08\cdot10^{-19}$

$E_{kin}=e\cdot U=0.67V$

---

Hohe Intensität
- Viele Photonen
- Es lösen sich viele Elektronen
Halbe Intensität
- Halbe Photonenzahl
- Halb so viele Elektronen lösen sich
- Halb so großer Fotostrom
- Fotospannung bleibt gleich, da kinetische Energie der Elektronen nur abhängig von der Frequenz des Lichts ($E_{kin}(f)=h\cdot f-W_{A}$)

## 2023-12-06

$E_{kin}=e\cdot U$
$E=h\cdot  \frac{c}{\lambda}$
$U=\frac{h\cdot c}{e\cdot\lambda}$

$U_{1}=2.6V$
$U_{2}=2.1V$
$U_{3}=1.3V$

---

$\lambda=\frac{h\cdot c}{e\cdot U}$

$\lambda_{1}=564nm$
$\lambda_{2}=636nm$
$\lambda_{3}=671nm$

---

$\lambda=635nm$
$E=120J$

$E=n\cdot h\cdot \frac{c}{\lambda}$
$n=\frac{E\cdot\lambda}{h\cdot c}=3.8\cdot10^{20}\text{ Photonen}$

---

$v=4.9\cdot10^{5} \frac{m}{s}$
$\lambda=\frac{h}{m\cdot v}=\frac{6.6261\cdot10^{-34}J\cdot s}{9.10939\cdot10^{-31}\cdot4.9\cdot10^{5}}=1.484nm$

---

$U=2kV$

$E=e\cdot U=3.204\cdot10^{-16}eV$

$\lambda=\frac{h}{mv}$
$eU=\frac{m}{2}v^{2}$ 
$v=\sqrt{\frac{2eU}{m}}$

$\lambda=2.74\cdot10^{-11}nm$

---

$U=54V$
$b=4650 \frac{1}{\mu m}$

$E_{kin}=e\cdot U$
$E_{kin}=\frac{m}{2}v^{2}$
$\lambda=\frac{h}{2eUm}=1.67\cdot10^{-10}m$

$\frac{n\cdot\lambda}{b}=\sin{\alpha}$
$\alpha=\arcsin{\frac{n\cdot\lambda}{b}}=50.9458$

---

$\lambda=5.48\cdot 10^{-12}m$

$e=350mm$
$b=2\mu m$

$\frac{n\cdot\lambda}{b}=\frac{s}{e}$
$s=\frac{n\cdot\lambda\cdot e}{b}=9.6\cdot10^{-7}m$
$k=\frac{\Delta s}{s}=105$

## 2023-12-10

Es werden mehr Elektronen herausgelöst, jedoch mit jeweils gleicher Energie.

Es werden gleichviele Elektronen herausgelöst, jedoch mit jeweils mehr Energie.

---

$\lambda=400nm=400\cdot10^{-9}m$
$E_{\text{max}}=1.8eV$

$E_{\text{max}}=h\cdot \frac{c}{\lambda}-W_{A}$
$W_{A}=\frac{h\cdot c}{\lambda}-E_{\text{max}}=2.09\cdot10^{-19}J$

$h\cdot f=W_{A}$
$f=\frac{W_{A}}{h}=3.15\cdot20^{14}Hz$

---

$\lambda=300nm=300\cdot10^{-9}m$
$A=1cm^{2}$
$W_{A}=2 eV=3.2044\cdot10^{-19}J$

$E=h\cdot \frac{c}{\lambda}=6.6261\cdot10^{-19}J$

---

$\lambda=444nm$
$W_{A}=1.9\cdot10^{-19}J$

$h\cdot f=E_{\text{kin}}+W_{A}$
$E_{\text{kin}}=h\cdot f-W_{A}=2.577\cdot10^{-19}J$

$E_{\text{kin}}=\frac{m}{2}v^{2}$
$v=\sqrt{\frac{2E_{\text{kin}}}{m}}=752592 \frac{m}{s}$

---

Gegenfeldmethode
- Zwischen Anode und Kathode wird eine Gegenspannung so eingestellt, dass die Stromstärke null beträgt.
- Die Energie der Gegenspannung $E_\text{kin}=e\cdot U$ entspricht der Energie der Elektronen $E_\text{kin}=\frac{m}{2}v^{2}$, worin man nach $v$ umstellen kann

---

$\lambda=[400:800]nm\approx600nm=6\cdot10^{-7}m$
$\Delta s=1\mu s=10^{-6}s$
$n=1T \text{ Photonon}=10^{12}\text{ Photonen}$
$P=\frac{n\cdot E}{t}=\frac{n\cdot h\cdot c}{t\cdot\lambda}=0.33W$

## 2023-12-11

$\Delta x=10^{-10}m$

$\Delta p=5.27\cdot10^{-25} kg\frac{m}{s}$
$\Delta v=578840 \frac{m}{s}$

---

Elektronen können kein eindeutiger Impuls zugeordnet werden, da sie als Quantenobjekte nicht eindeutig bestimmt werden können.
Bei einer Unschärfe $\Delta p=0$ wäre $\Delta p\cdot \Delta x\ge \frac{h}{4\pi}$ wäre somit immer falsch. Wenn $\Delta p\to0$, dann müsste $\Delta x\to \infty$ und somit $L\to\infty$, was nicht der Fall sein kann.

$\Delta x\approx0.3L$

$\Delta x\cdot\Delta p\ge \frac{h}{4\pi}$
$\Delta p\ge \frac{h}{4pi\Delta x}=6.76\cdot10^{-26}kg \frac{m}{s}$

## 2023-12-18

Energieniveaus sinken mit zunehmendem n.

---

Der Radius ist einhundertfach so groß wie $a_{0}$, da $\frac{10^{2}}{1}$.

Da $v=\frac{nh}{2\pi mr}$ gilt, ist bei $n=10$ die Geschwindigkeit ein zehntel von $n=1$: $\frac{v_{10}}{v_{1}}=\frac{\frac{10h}{2\pi m100r}}{ \frac{1h}{2\pi m1r}}=\frac{10}{100}=\frac{1}{10}$

---

$F=G \frac{m_{1}\cdot m_{2}}{r^{2}}=6.673\cdot10^{-11} \frac{m^{3}}{kg\cdot s^{2}} 9.10939\cdot10^{-31}kg\cdot \frac{1.67493\cdot10^{-27}kg+1.67262\cdot10^{-27}kg}{(0.053nm)^{2}}=1.086\cdot10^{-36}N$


## 2024-01-03

Die Stromstärke sinkt nach dem Auftreffen der Elektronen mit den Helium-Atomen. Beim Erhöhen der Spannung erhöht sich auch die Energie der Elektronen. Wenn die Elektronen auf die Atome mit genug Energie aufstoßen, erreicht das Atom einen höheren Energiezustand und das Elektron verliert an Energie.
Bei Helium werden höhere Energiezustände im Abstand von etwa 22 V im Gegensatz zu 4.9 V vom Quecksilber erreicht erreicht.

---

Abstand Maximum zu Maximum:
$\Delta U=22.5V$

$E_{\text{kin}}=e\cdot \Delta U=3.60495\cdot10^{-18}J$

---


Die Ergebnisse des Experimentes zeigen, dass gleiche Mengen an Energie (feste Abstände) für das Anheben des Energieniveaus benötigt wird. Es gibt feste Energieniveaus. Dies stützt das dritte Postulat.

## 2024-01-08

Bei der Fluoreszenz wird ein Photon in einem Atom absorbiert. Die Energie wird in dem Atom durch das Erreichen eines höheres Energieniveau gespeichert. Wenn das Atom die Energie emittiert, wird ein Photon wieder ausgesendet, wobei ein Teil der Energie im Atom zurückbleibt. Da dass Photon mit weniger Energie emittiert wurde, als es absorbiert wurde, hat es auch eine kleinere Frequenz nach $E=h\cdot f$.

---

Nach der Absorption wird zwar ein Photon gleicher Frequenz wieder emittiert, aber die Aussendung der Photonen erfolgt ungerichtet in den gesamten Raum. Somit wird weniger Licht an dieser Stelle in die ursprüngliche Strahlungsrichtung ausgesendet. Dadurch ergibt sich eine Verdunklung im Spektrum.

---

|          | Elektronen                                                                                           | Photonen                                                                              |
| -------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Anregung | erfolgt durch Zusammenstöße zwischen freien Elektronen und den Atomen/Molekülen                      | Photonen werden absorbiert und sind danach auch nicht mehr existent                   |
| Energie  | Energie des Elektrons muss mindestens der Energiedifferenz zwischen dem Energienivieaus entsprechen. | Energie des Photons muss der Energiedifferenz zwischen den Energieniveaus entsprechen |

---

$t=100fs=100\cdot10^{-15}s$
$W=10TW=10\cdot10^{12}W$

---

$p=m\cdot v=\frac{E}{c}=\frac{10\cdot10^{12}W\cdot100\cdot10^{-15}s}{3\cdot10^{8} \frac{m}{s}}=3.33\cdot10^{8}N\cdot s$

$v=\frac{p}{1g}=3.33\cdot10^{-6} \frac{m}{s}$

# Thermodynamik

## 2024-01-10

Lb. S. 283 Nr. 1

Das Material nimmt Wärme von der Umgebung auf. Diese wird genutzt, um das Material zu schmelzen. Dadurch findet keine Temperaturerhöhung statt.

---

$P=1.7kW$
$q_{v}=2260 \frac{kJ}{kg}$

$Q_{v}=q_{v}\cdot m$
$P=q_{v}\cdot \frac{m}{t}$
$\frac{m}{t}= \frac{P}{q_{v}}=\frac{1.7kW}{2260 \frac{kJ}{kg}}=\frac{1.7kg}{2260}=752\cdot10^{-6} \frac{kg}{s}=0.752 \frac{g}{s}$

---

Verdunsten: Übergang von flüssig zu gasförmig unterhalb der Siedetemperatur.

Das Wasser dring durch die poröse Wand nach Außen und verdunstet. Dazu ist Wärme notwendig, die der Umgebung und dem Wasser im Gefäß entzogen wird (Verdunstungswärme). Somit sinkt die Temperatur und es kommt zu Abkühlung.

---

Lb. S. 283 Nr. 4

Durch einen Unterdruck wird der Siedepunkt und somit die Änderung des Aggregatzustandes nach unten Verlagert. Durch die Änderung wird jedoch mehr Energie benötigt, um höhere Temperaturen zu erreichen, weshalb es nicht sinnvoll ist.

---

Offenes System: Turbine oder Mensch, tauscht Energie bzw. Wärme und Materie aus.
Geschlossenes System: Kühlschrank oder Wasserkocher, tauscht Energie bzw. Wärme aus.
Abgeschlossenes System: Thermoskanne, tauscht weder Energie bzw. Wärme noch Materie aus.

## 2024-01-17

$\approx3bar$

---

$V=\frac{nRT}{p}$

## 2024-01-22

$m=1kg$
$q_{s}=334 \frac{kJ}{kg}$
$q_{v}=2260 \frac{kJ}{kg}$
$c=4.186 \frac{kJ}{kg\cdot K}$

$Q_{s}=q_{s}\cdot m=334 \frac{kJ}{kg}\cdot1kg=334kJ$
$Q_{0\to100}=m\cdot c\cdot 100K=419kJ$
$Q_{v}=q_{v}\cdot m=2260 \frac{kJ}{kg}=2260kJ$

---

$\varrho=1 \frac{g}{cm^{3}}$
$V=1000L=1000kg$
$c_\ce{H2O}=4.19 \frac{kJ}{kg\cdot K}$

$Q=m\cdot c\cdot\Delta T=m\cdot c(90^{\circ}-20^{\circ})=1000kg\cdot 4.19 \frac{kJ}{kg\cdot K}\cdot70K=293300kJ$

---

$c_{v}=1.01 \frac{kJ}{kg\cdot K}$
$V=\frac{Q}{\varrho\cdot c\cdot \Delta T}=\frac{293300kJ}{1.29 \frac{kg}{m^{3}}\cdot1.01 \frac{kJ}{kg\cdot K}\cdot 4K}=56278m^{3}$

---

$m_{A}=\frac{1}{2}L$
$T_{A,1}=25^{\circ}C$
$T_{A,2}=10^{\circ}C$
$m_{E}=10g$
$T_{E}=-18^{\circ}C$

$c_{\text{Eis}}=2.09 \frac{kJ}{kg\cdot K}$
$c_{\text{Wasser}}=4.19 \frac{kJ}{kg\cdot K}$
$q_{s}=334 \frac{kJ}{kg}$

$Q_{-10\to0}=0.01g\cdot c\cdot 10K=0.01g\cdot2.09 \frac{kJ}{kg\cdot K}\cdot10K$
$Q_{s}=q_{s}\cdot 0.01g=0.01g\cdot 334 \frac{kJ}{kg}$
$Q_{0\to10}=m\cdot c\cdot10K=0.01g\cdot 4.19 \frac{kJ}{kg\cdot K}\cdot10K$
$Q_{25\to10}=m\cdot c\cdot 15K=0.5kg\cdot 4.19 \frac{kJ}{kg\cdot K}\cdot15K=31.4kJ$

$n\cdot Q_{auf}=Q_{ab}$
$n=\frac{Q_{ab}}{Q_{auf}}=\frac{0.5kg\cdot 4.19 \frac{kJ}{kg\cdot K}\cdot15K}{0.01kg\cdot(2.09\frac{kJ}{kg\cdot K}\cdot10k+334 \frac{kJ}{kg})+4.19 \frac{kJ}{kg\cdot K}\cdot10K}=7.9\approx8$

## 2024-01-29

$p=0.1\pu{MPa}$
$T_{0}=293\pu{K}\;(20\pu{^\circ C})$
$T_{1}=100 ^{\circ} C$

$W=p \Delta V=p(V_{1}-V_{0})$
$\frac{V_{0}}{T_{0}}=\frac{V_{1}}{T_{1}}\to V_{1}=V_{0} \frac{T_{1}}{T_{0}}$

$W=p(V_{0} \frac{T_{1}}{T_{0}}- V_{0})=pV_{0}(\frac{T_{1}}{T_{0}}-1)=100000Pa\cdot1\pu{cm3}(\frac{273K}{293K}-1)\approx27300J$

---

$p_{2}=200000\pu{Pa}$
$c_{V}=718\pu{J // kg K}$
$V=\text{konst.}\to\mathrm{d}V=0\to W=0$

$Q=mc_{V}(T_{2}-T_{1})$

$\frac{p_{2}}{T_{2}}=\frac{p_{1}}{T_{1}}\to T_{2}=T_{1} \frac{p_{2}}{p_{1}}$
$Q=mc_{V}(T_{1} \frac{p_{2}}{p_{1}}-T_{1})=mc_{V}T_{1}(\frac{p_{2}}{p_{1}}-1)$

$m=\varrho V=1.29 \pu{kg // m3}1\pu{m3}=1.29\pu{kg}$

$Q=1.29kg 718\pu{J // kgK} 293K(\frac{0.2}{0.1}-1)\approx271.4 kJ$ 

---

$p_{a}=101300\pu{Pa}$
$R_{0}=283\pu{K}$
$Q=126\pu{J}$
$T_{1}=333\pu{K}\;(60\pu{^\circ C})$

$P_\text{ges}=P_{a}+P_\text{Kolben}=P_{a}+ \frac{F_{g}}{A}=101300\pu{Pa}+ \frac{0.5\pu{kg}\cdot9.81\pu{m //s2}}{40\cdot 10^{-4}\pu{m2}}\approx102526\pu{Pa}$

---

isobarer Prozess ($p=\text{konst.}$)
$\frac{V_{1}}{V_{2}}=\frac{T_{1}}{T_{2}}\quad\text{mit}\;\begin{matrix}V_{1}=A\cdot h_{1} \\ V_{2}=A\cdot h_{2}\end{matrix}$
$V_{2}=\frac{T_{2}}{T_{1}}V_{1}$
$h_{2}=\frac{T_{2}}{T_{1}}h_{1}=\frac{333\pu{K}}{283\pu{K}}49.6\pu{cm}\approx58.4\pu{cm}$

---

Lb. S. 295

**Ansatz**

$Q_{p}=Q_{v}+W$

$Q_{v}$ Erwärmung
$W$ Arbeit für Änderung Volumen

$Q_{p}=mc_{v}\Delta T + p(V_{2}-V_{1})$
$m=\frac{Q_{p}-pV_{2}-V_{1}}{c_{v}\Delta T}$
$m=\frac{126\pu{J}-102526\pu{Pa}\cdot0.004\pu{m2}(0.584\pu{m}-0.496\pu{m})}{718\pu{J // kg K}\cdot50\pu{K}}=2.50\pu{g}$

---

$\ce{O2}:32\pu{g //mol} (21\%)$
$\ce{N2}:28\pu{g //mol} (78\%)$
$\ce{Ar}:40\pu{g//mol} (1\%)$

$n\approx 0.0864\pu{mol}$

$\frac{m}{n}=0.21\cdot32\pu{g//mol}+ 0.78\cdot28\pu{g//mol}+ 0.01\cdot40\pu{g//mol}\approx28.96\pu{g//mol}$
$m=28.9\pu{g//mol}6\cdot0.0864\pu{mol}\approx 2.5\pu{g}$

## 2024-02-07

$T_{1}=40+273K$
$T_{2}=120+273K$

$\eta=1 - \frac{T_{1}}{T_{2}}=0.204$

---

$2\cdot0.204=1-\frac{T_{1}}{T_{2}}$
$2\cdot0.204-1=-\frac{T_{1}}{T_{2}}$
$T_{2}=-\frac{T_{1}}{2\cdot0.204-1}=527.935K$
## 2024-02-26

$n=0.1\pu{mol}$
$\frac{V_{2}}{V_{1}}=4$
$T_{2}=1200\pu{K}$

Isobare Zustandsänderung
$\frac{V_{1}}{T_{1}}=\frac{V_{2}}{T_{2}}$
$T_{1}=\frac{V_{1}}{V_{2}}T_{2}=\frac{1}{4}\cdot1200\pu{K}=300K$

---

$\begin{split}W_{3,1}&=\int p\;\mathrm{d}V=-\int \frac{nRT_{2}}{V}\;\mathrm{d}V \\ &=-nRT_2[\ln{V}]^{V_{2}}_{V_{1}}=-nRT_{2}(\ln{V_{1}-\ln{V_{2}}})\\ &=-nRT_{2}\ln{\frac{V_{2}}{V_{1}}}=-0.1\pu{mol}\cdot8.314 \pu{J //mol K}1200K\cdot\ln{4}=-1383J\end{split}$

---

$V_{1}=500\pu{m3}$
$p_{1}=1.1\cdot10^{5}\pu{Pa}$
$W_{1,2}=20\pu{kW h}$
$T=298K$

Isotherm
$p_{1}\cdot V_{1}=p_{2}\cdot V_{2}$

$W=-nRT\ln{\frac{V_{2}}{V_{1}}}$
$W=-nRT\ln{\frac{p_{1}}{p_{2}}}$
$\ln{\frac{p_{1}}{p_{2}}}=-\frac{W}{nRT}$
$\frac{p_{1}}{p_{2}}=e^{- \frac{W}{nRT}}$

Da $p_{1}V_{1}=nRT$
$p_2=p_{1}e^{\frac{W}{nRT}}=p_{1}e^{\frac{W}{nRT}}=p_{1}e^{\frac{W}{p_{1}V_{1}}}=1.1\cdot10^{5}\cdot e^\frac{20000\cdot3600}{500}=4.07\cdot10^{5}\pu{Pa}$

---

$\eta=0.6$
$W=2000J$
$T=900k$

$\eta=1- \frac{T_{N}}{T_{H}}$
$T_{N}=T_{H}(1-\eta)=900\pu{K}(1-0.6)=360\pu{K}$
## 2024-02-28

$P=5.8\pu{kW}$

Pufferwärmespeicher: $T_{N}$

$\eta=\frac{P_{el}}{P_{zu}}=1 - \frac{T_{N}}{T_{H}}$

$P_{zu}=\frac{P_{el}}{1- \frac{T_{N}}{T_{H}}}$

Da $P_{el}$ konstant bleiben soll und der Wirkungsgrad abhängig von der Pufferspeichertemperatur $T_{N}$ ist, muss sich die Wärmeleistung ändern, um die elektrische Leistung konstant zu halten.

## 2024-03-04

$T_{N}=5^{\circ}C=287\pu{K}$
$T_{H}=30=303\pu{K}$

$T_{B,N}=5=378\pu{K}$
$T_{B,H}=25=398\pu{K}$
$\Delta T=25\pu{K}$

$P_{el}=1200W$
$V=3\cdot25\pu{l}=200\pu{kg}$

$Q=m\cdot c_{V}\cdot\Delta T=200\pu{kg}\cdot4.19\pu{kJ//kgK}\cdot20\pu{K}=16.760\pu{kJ}$

$\epsilon_{KM}=\frac{Q_{N}}{W_{el}}=\frac{T_{N}}{T_{H}-T_{N}}$
$Q_{N}=W_{el}\cdot\frac{T_{N}}{T_{H}-T_{N}}$
$P_{N}=P_{el}\cdot \frac{T_N}{T_H-T_{N}}=1.2\pu{kW} \frac{278\pu{K}}{303\pu{K}-278\pu{K}}\approx13.334\pu{kW}$

$t=\frac{Q}{P_{N}}=\frac{6.760\pu{kJ}}{13.334\pu{kW}}\approx1256\pu{s}$

---

$T_{zu}=-10^{\circ}\pu{C}=263\pu{K}$
$T_{ab}=17^{\circ}\pu{C}=290\pu{K}$
$W=37\pu{kJ}$

$\epsilon_{WM}=\frac{T_{ab}}{T_{ab}-T_{zu}}=\frac{290\pu{K}}{290\pu{K}-263\pu{K}}=10.7$

$Q_{H}=Q_{N}+W$
$\epsilon=\frac{Q_{H}}{W}$

$W\cdot\epsilon=Q_{N}+W$

---

Die Temperatur wird sich langfristig erwärmen, da die zugeführte und abgeführte Wärme im selben abgeschlossenen Raum sich austauscht, sich durch den Kühlschrank die Temperatur sich nicht senk, da die Effizienz jedoch nicht 100% ist, durch Abwärme bei der Kühlung die Temperatur sich erhöht.

---

$P=1.5\pu{kW}$
$m=1\pu{kg}$

$c_{S}=334\pu{kJ//kg}$
$Q_{S}=m\cdot q_{S}=1\pu{kg}\cdot334\pu{kJ//kg}=334\pu{kJ}$
$P=\frac{Q_{S}}{t}$
$t=\frac{Q_{S}}{P}=\frac{334\pu{kJ}}{1.5\pu{kW}}=222.7\pu{s}=3.71\pu{min}$

---

$\Delta S=\frac{334\pu{kJ}}{273\pu{K}}=1.22\pu{kJ//K}$

Da die Temperatur beim Schmelzprozess konstant ist (273K), vereinfacht sich das Integral:

$\Delta S=\int_{1}^{2} \frac{\mathrm{d}Q}{T}=\frac{1}{T}\int_{1}^{2}\mathrm{d}Q=\frac{Q}{T}$
<<<<<<< HEAD

---

$W_{2,3}>W_{1,2}$

$W_{1,2}$ Volumenarbeit positiv
$W_{2,3}$ Volumenarbeit negativ
=======
# Kernphysik

## 2024-03-10

$\ce{^{14}_{6}C}$ bedeutet, dass ein Kohlenstoff-Atom mit der Ordnungszahl 6 14 Nukleonen hat.
Ein C-14 Atom kann bei vollständiger Ionisierung 6 Elektronen abgeben.

---

$N_A=6.0221\cdot10^{23} \pu{mol-1}$

$1\pu{kmol}=6.0221\cdot10^{26}$

$m_{A}=14\pu{u}$
$1\pu{u}=1.660539\cdot10^{-27}\pu{kg}$

$n=\frac{m_{ges}}{m_{C}}=\frac{1\pu{kg}}{14\cdot1.66\cdot10^{-27}\pu{kg}}\approx4.3\cdot10^{25}$

## 2024-03-11

$\ce{^{62}_{28}Ni}$
$m_{Kern}=61.912985\pu{u}$

$m_{Nuk}=28m_{P}+34m_{N}=62.498338u$
$\Delta m=m_{Nuk}-m_{Kern}=62.498338u-61.912985\pu{u}=0.585353u$

$E_{B}=\Delta m\cdot c^{2}=0.585353\cdot1.660539\cdot10^{-27}\pu{kg}\cdot(3\cdot10^{8}\pu{m//s})^{2}=8.74801\cdot10^{-10}\pu{J}$
$E_{B}=\frac{8.74801\cdot10^{-10}\pu{J}}{1.6602\cdot10^{-19}\pu{As}}=546\pu{MeV}$

$\overline{E_{B}}=\frac{E_{B}}{A}=8.8\pu{MeV}$

---

$m_{A}=12.01\pu{u}$
$1\pu{u}=1.660539\cdot10^{-27}\pu{kg}$

$\Delta m=0.137\pu{u}$
$E_{B}=128\pu{MeV}$
$\overline{E_{B}}=\frac{E_{B}}{A}=8\pu{MeV}$



## 2024-03-18

Im Diagramm sind verschiedene Materialien dargestellt