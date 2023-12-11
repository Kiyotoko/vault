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
