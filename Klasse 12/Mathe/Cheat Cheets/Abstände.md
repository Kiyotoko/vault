# Hessische Normalenform

$$\vec{n}\circ[\vec{x}-\vec{q}]=0\equiv \frac{ax+by+cz-d}{\sqrt{a^{2}+b^{2}+c^{2}}}=0$$

## Von Koordinatenform

$E: ax+by+cz=d$

Den Faktor $d$ auf die andere Seite ziehen und durch der Normalen der Ebene teilen.
$E: \frac{ax+by+cz-d}{\sqrt{a^{2}+b^{2}+c^{2}}}=0$

## Von Parameterform

$E: \vec{A}=s\cdot\vec{B}+t\cdot\vec{C}$

Das Kreuzprodukt der Richtungsvektoren ergibt die Normale der Ebene.
$\vec{q}=\vec{A}$
$\vec{n}=\vec{B}\times\vec{C}$
$E:\vec{n}\circ[\vec{x}-\vec{q}]=0$

# Abstände

## Abstand Punkt Ebene

$E:ax+bx+cx=d$
$P(p_{1}|p_{2}|p_{3})$

Hessische Normalenform
$d=\frac{ax+bx+cx-d}{\sqrt{a^{2}+b^{2}+c^{2}}}=\frac{ap_{1}+bp_{2}+cp_{3}-d}{\sqrt{a^{2}+b^{2}+c^{2}}}$

## Abstand Gerade Ebene

- Wenn die Gerade durch die Ebene geht, ist der Abstand 0
- Ansonsten muss die Gerade parallel zur Ebene sein
- Beliebigen Punkt auf der Gerade auswählen, dann fortfahren wie Abstand Punkt Ebene

## Abstand Punkt Gerade

- Zwei beliebige Punkte auf Gerade wählen
- Minimum bei der Länge des Vektors bestimmen

$g:\vec{A}+t\cdot\vec{B}$
$P(p_{1}|p_{2}|p_{3})\equiv\vec{P}$

$g_{t=0}\mapsto\vec{Q}_{0}=\vec{A}$
$g_{t=1}\mapsto\vec{Q}_{1}=\vec{A}+\vec{B}$

$d=\frac{|(\vec{P}-\vec{Q}_{0})\times(\vec{P}-\vec{Q}_{1})|}{|\vec{Q}_{0}-\vec{Q}_{1}|}$

## Abstand paralleler Geraden

- Beliebigen Punkt auf Gerade auswählen, dann fortfahren wie Abstand Punkt Gerade

## Abstand windschiefer Geraden

- Aufstellen einer Hilfseben, die $g_{1}$ enthält und parallel zu $g_{2}$ verläuft
- Beliebigen Punkt auf $g_{2}$ wählen
- Fortfahren wie bei Abstand Punkt Ebene

$g_{1}:\vec{x}=\vec{A}+s\cdot\vec{B}$
$g_{2}:\vec{x}=\vec{C}+t\cdot\vec{D}$

Ebene aufstellen
$E:\vec{x}=\vec{A}+s\cdot\vec{B}+t\cdot\vec{D}$

$\vec{q}=\vec{A}$
$\vec{n}=\vec{B}\times\vec{D}$

$E:\vec{n}\circ\big[\vec{x}-\vec{q}\big]\mapsto ax+by+cz=d\quad\text{mit}\;\vec{x}=\vec{C}$

Abstand berechnen
$d=\frac{ax+by+cz-d}{\sqrt{a^{2}+b^{2}+c^{2}}}=\frac{a\vec{C}_{x}+b\vec{C}_{y}+c\vec{C}_{z}-d}{\sqrt{a^{2}+b^{2}+c^{2}}}$