---
author: karlz
tags:
  - Mathe
  - FGB
---

# Vektoren

## 2023-09-19

$2\cdot1+1\cdot1-3\cdot1=0$

Die Vektoren sind orthogonal zueinander.

---

$4\cdot5-2\cdot7-1\cdot5=1$
$1\ne0$

Die Vektoren sind orthogonal zueinander.

---

$A(5|1|-3)$
$B(6|-3|2)$
$\vec{AB}=\begin{pmatrix}1\\-4\\5\end{pmatrix}$
$\vec{c}=\begin{pmatrix}3\\7\\ k\end{pmatrix}$
$1\cdot3-4\cdot7+5\cdot k=0$
$-\frac{1\cdot3-4\cdot7}{5}=k$
$k=5$

---

$A(11|-1|-4)$
$B(6|-4|-3)$
$C(4|0|-1)$
$D(9|3|-2)$

$\vec{AB}=\begin{pmatrix}6-11 \\ -4+1 \\ -3+4\end{pmatrix}=\begin{pmatrix}-5 \\ -3 \\ 1\end{pmatrix}$
$\vec{AD}=\begin{pmatrix}9-11 \\ 3+1 \\ -2+4\end{pmatrix}=\begin{pmatrix}-2\\4 \\ 2\end{pmatrix}$

$\vec{AB}\circ\vec{AD}=5\cdot2-3\cdot4+1\cdot2=0$

Das Viereck ist rechtwinklig.

---

$A(-1|2|0)$
$B(-1|0|0)$

$g:\vec{x}=\begin{pmatrix}-1 \\ 0 \\ 1\end{pmatrix}+k\begin{pmatrix}1 \\ 1 \\ -1\end{pmatrix}$

Punkt auf $g$, von dem aus man die Strecke $\overline{AB}$ unter einem Winkel von $90^{\circ}$ sieht.

$P(-1+k|k|1-k)$
$\overrightarrow{PA}\circ\overrightarrow{PB}=0$
$\begin{pmatrix}-k \\ 2-k \\ -1+k\end{pmatrix}\circ\begin{pmatrix}-k \\ -k \\ -1+k\end{pmatrix}=k^{2}-2k+k^{2}+1-2k+k^{2}=0$
$3k^{2}-4k+1=0$
$k - \frac{4}{3}k+ \frac{1}{3}=0$
$k_{1,2}=\frac{2}{3}\pm \sqrt{\frac{4}{9}- \frac{3}{9}}$
$k_{1}=\frac{2}{3}+ \frac{1}{3}=1$
$k_{2}=\frac{2}{3}- \frac{1}{3}= \frac{1}{3}$

$\begin{pmatrix}-1\\0\\1\end{pmatrix}+1\begin{pmatrix}1 \\ 1 \\ -1\end{pmatrix}=\begin{pmatrix}0 \\ 1 \\ 0\end{pmatrix}$
$P_{1}(0|1|0)$

$\begin{pmatrix}-1\\0\\1\end{pmatrix}+ \frac{1}{3}\begin{pmatrix}1\\1\\-1\end{pmatrix}=\begin{pmatrix}- \frac{2}{3} \\ \frac{1}{3} \\ \frac{2}{3} \\ \end{pmatrix}$
$P_{2}(- \frac{2}{3}| \frac{1}{3}| \frac{2}{3})$

---

$E: 2x+4y-z=5$
$\vec{n}=\begin{pmatrix}2 \\ 4 \\ -1\end{pmatrix}$
$g:\vec{x}=\begin{pmatrix}1 \\ 2 \\ 3\end{pmatrix}+k\begin{pmatrix}1 \\ 1 \\ 3\end{pmatrix}$
$\arcsin(\frac{\vec{g}\circ\vec{n}}{|\vec{g|\cdot|\vec{n}}|})=11.4^{\circ}$

## 2023-09-28

$\begin{pmatrix}3 \\ -1 \\ 2\end{pmatrix}\times\begin{pmatrix}4 \\ 2 \\ -3\end{pmatrix}=\begin{pmatrix}-1 \\ 17 \\ 10\end{pmatrix}$

## 2023-10-17

$\vec{DE}=\begin{pmatrix}0 \\ 30 \\ 0\end{pmatrix}$
$|\vec{DE}|=30$
$\vec{DF}=\begin{pmatrix}-25 \\ 5 \\ 0\end{pmatrix}$
$|\vec{DF}|=5\cdot\sqrt{26}$
$\vec{EF}=\begin{pmatrix}-25 \\ -25 \\ 0\end{pmatrix}$
$|\vec{EF}|=25\cdot\sqrt{2}$

$\cos{d}=\frac{\vec{DE}\circ\vec{DF}}{|\vec{DE}|\cdot|\vec{DF|}}=\frac{5\cdot30}{30\cdot5\cdot\sqrt{26}}=\frac{1}{\sqrt{26}}$
$\arccos{1/\sqrt{26}}$
$\cos{e}=\frac{\vec{DE}\circ\vec{EF}}{|\vec{DE}|\cdot|\vec{EF|}}=\frac{-25\cdot30}{30\cdot25\cdot\sqrt{2}}=\frac{-1}{\sqrt{2}}$
$\cos{f}=\frac{\vec{DF}\circ\vec{EF}}{|\vec{DF}|\cdot|\vec{EF}|}=\frac{25^{2}-25\cdot5}{25\cdot\sqrt{26}\cdot5\cdot\sqrt{2}}=\frac{4}{\sqrt{26}\cdot\sqrt{2}}=2/\sqrt{13}$