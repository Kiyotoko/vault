## Vorbetrachtung

Kräfteansatz
$F_G=m*g=m*9.81\frac{m}{s}$
$F_H=F_G*\sin{\alpha}$
$F_N=F_G*\cos{\alpha}$
$F_R=F_N*\mu$

$F_Z=F_G-F_R-F_H$
$F_Z=m_1*g-m_2*\cos{\alpha}*g*\mu-m_2*\sin{\alpha}*g$
$F_Z=\Big(m_1-(\cos{\alpha}\mu+\sin{\alpha})*m_2\Big)*g$

Reibungskoeffizient auf eine Seite bringen
$a*m_2=F_Z$
$a*m_2=\Big(m_1-(\cos{\alpha}\mu+\sin{\alpha})*m_2\Big)g$
$a*m_2=m_1g-\cos{\alpha}\mu m_2g-\sin{\alpha}m_2g$
$a*m_2+\sin{\alpha}m_2g-m_1g=-\cos{\alpha}\mu m_2g$
$\frac{a*m_2+\sin{\alpha}m_2g-m_1g}{-\cos{\alpha} m_2g}=\mu$

Beschleunigung berechnen und einsetzen
$s=\frac{a}{2}t^2$
$a=\frac{2s}{t^2}$

$\mu=\frac{a*m_2+\sin{\alpha}m_2g-m_1g}{-\cos{\alpha} m_2g}$
$\mu=\frac{\frac{2s}{t^2}*m_2+\sin{\alpha}m_2g-m_1g}{-\cos{\alpha} m_2g}$

## Messergebnisse
|     | Zeit | Weg   | Masse 1 | Masse 2 | Winkel | Reibungskoeffizient |
| --- | ---- | ----- | ------- | ------- | ------ | ------------------- |
| 1   | 0.76 | 0.385 | 0.03    | 0.04    | 10     | 0.60                |
| 2   | 0.58 | 38.5  | 0.03    | 0.05    | 10     | 0.33                |
| 3   | 0.35 | 38.5  | 0.03    | 0.07    | 10     | -0.91               |

## Auswertung

$\mu=\frac{1}{3}(\mu_1+\mu_2+\mu_3)=0.0067$

## Fehlerbetrachtung

Mittelwert Zeit
$t=\frac{1}{3}(t_{1}+t_{2}+t_{3})=0.5633$

Mittelwert Reibungskoeffizient
$\mu=\frac{1}{3}(\mu_{1}+\mu_{2}+\mu_{3})=0.0067$

$SE=1\text{digit}=0.01s$
$FG=10\%$

$\frac{\Delta s}{s}=\frac{0.001m}{0.385m}=0.0130$
$\frac{\Delta t}{t}=\frac{0.01s}{0.5633s}=0.0178$
$\Delta \alpha_{\cos}=|\cos{\Big(10°+\frac{1°}{2}\Big)}-\cos{\Big(10°-\frac{1°}{2}\Big)}|=0.0031$
$\Delta \alpha_{\sin}=|\sin{\Big(10°+\frac{1°}{2}\Big)}-\sin{\Big(10°-\frac{1°}{2}\Big)}|=0.0172$
$\Omega=FG+\frac{\Delta s}{s}+2 \frac{\Delta t}{t}+\Delta\alpha_{\cos}+\Delta\alpha_{\sin}=0.1689$

Systematische Fehler
$u=0.0067*\Omega=0.0011$
$a=0.001$
$g=u+a=0.0021$

Angabe des Fehlers
$M=0.0067\pm0.0021$
$R=\frac{0.0021}{0.0067}=0.3134\%$
