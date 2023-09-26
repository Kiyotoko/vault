---
author: karlz
tags:
  - Physik
  - FGN
---

## Größe einer Schwingung

$\hat{y}$ Amplitude (Maximale Auslenkung)
$y$ Elongation (Auslenkung)
$f$ Frequenz in $1Hz=1s^{-1}$
$T$ Periode $T=\frac{1}{f}$

## Geschwindigkeit & Beschleunigung bei Schwingungen

Auslenkung
$y(t)=\hat{y}\sin{(\omega t)}$

Geschwindigkeit
$v(t)=\frac{dy}{dt}=\hat{y}\omega\cos{(\omega t)}=\hat{v}\cos{(\omega t)}$ mit $\hat{v}=\hat{y}\omega$

Beschleunigung
$a(t)=\frac{dv}{dt}=-\hat{y}\omega^{2}\sin{(\omega t)}=-\hat{a}\sin{(\omega t)}$ mit $\hat{a}=\hat{y}\omega^{2}$

### Eigenfrequenz Federschwinger

![Eigenfrequenz Federschwinger](../Working%20Materials/Schwingungen/Eigenfrequenz%20Federschwinger.png)

$w_{0}=\sqrt{\frac{D}{m}}$
$f_{0}=\frac{1}{2\pi} \sqrt{\frac{D}{m}}$
$T_{0}=2\pi \sqrt{\frac{m}{D}}$

### Periodendauer Fadenpendel

$w_{0}=\sqrt{\frac{g}{l}}$
$f_{0}=\frac{1}{2\pi} \sqrt{\frac{g}{l}}$
$T_{0}=2\pi \sqrt{\frac{l}{g}}$

## Energieerhaltung einer harmonischen Schwingung

- Energie Schwingkreis
	- $E_{el}=\frac{1}{2}CU^{2}$
	- $E_{mag}=\frac{1}{2}LI^{2}$

- Energie Federschwinger
	- $E_{pot}=\frac{2}{2}Dy^{2}$
	- $E_{kin}=\frac{1}{2}mv^{2}$

- Energie Fadenpendel
	- $E_{pot}=mgh$
	- $E_{kin}=\frac{m}{2}v^{2}$

---

$E_{ges}=E_{pot}+E_{kin}=\frac{1}{2}Dx(t)^{2}+ \frac{1}{2}mv(t)^{2}=\frac{1}{2}D(\hat{x}\cos{\omega t})^{2}+ \frac{1}{2}m (-\hat{x}\omega \sin{\omega t})^{2}$
$\frac{1}{2}D\hat{x}\cos^{2}{\omega t}+ \frac{1}{2}m \hat{v}^{2}\sin{\omega t}=E_{ges}\cos^{2}{\omega t}+E_{ges}\sin^{2}{\omega t}=E_{ges}(\cos^{2}{\omega t}+\sin^{2}{\omega t})=E_{ges}$

---

$U_{C}=\hat{U}\cos{(\omega t)}$
$Q=CU$
$I=\frac{dQ}{dt}=C \frac{dU}{dt}=-C\hat{U}\omega\sin{\omega t}$
$\omega^{2}=\frac{1}{LC}$

$E_{el}=\frac{1}{2}CU^{2}=\frac{1}{2}C\hat{U}^{2}\cos^{2}{(\omega t)}$
$E_{mag}=\frac{1}{2}LI^{2}=\frac{1}{2}LC^{2}\omega^{2}\hat{U}^{2}\sin^{2}{(\omega t)}=\frac{1}{2}C\hat{U}^{2}\sin^{2}{(\omega t)}$

$E_{ges}=E_{mag}+E_{el}=\frac{1}{2}C\hat{U}^{2}\sin^{2}{(\omega t)}+\frac{1}{2}C\hat{U}^{2}\cos^{2}{(\omega t)}=\frac{1}{2}C\hat{U}^{2}(\sin^{2}{(\omega t)}+\cos^{2}{(\omega t)})=\frac{1}{2}C\hat{U}^{2}$
## Widerstände im Wechselstromkreis

$X=X_{L}-X_{C}=\omega\cdot L- \frac{1}{\omega\cdot C}$
$Z=\sqrt{R^{2}+X^{2}}$

### Ohmscher Widerstand

$R=\frac{U}{I}$

### Induktiver Widerstand

$X_{L}=\omega\cdot L$

Phasenverschiebung $\varphi=+ \frac{\pi}{2}$

### Kapazitiver Widerstand

$X_{C}=\frac{1}{\omega\cdot C}$

Phasenverschiebung $\varphi=- \frac{\pi}{2}$

## Hoch- und Tiefpass

![Hochpass](../Working%20Materials/Schwingungen/Hochpass.png)

![Tiefpass](../Working%20Materials/Schwingungen/Tiefpass.png)

## Leistung im Wechselstromkreis

$P_{S}=U \cdot I=\sqrt{P_{W}^{2}+P_{B}^{2}}$
$P_{W}=U \cdot I \cdot\cos{\varphi}$
$P_{B}=U \cdot I \cdot\sin{\varphi}$