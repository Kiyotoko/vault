# Der binomische Satz von Fermat

$(a+b)^2=\sum^n_\limits{i=0}\binom{n}{i}a^{i}b^{n-i}$

## Grundwissen

### Binomische Formeln

1. $(a+b)^2=a^2+2ab+b^2$
2. $(a-b)^2=a^2-2ab+b^2$
3. $(a+b)(a-b)=a^2-b^2$

### Binomialkoeffizienten

$\binom{n}{k}$ sprich: $n$ über $k$
$\binom{n}{k}$ Anzahl der Möglichkeiten aus einer $n$-elementigen Mengen einer Teilmenge aus $k$ Elementen auszuwählen, entspricht $\frac{n!}{k!(n-k)!}$.

# Der kleine Satz von Fermat

Für jede Primzahl $p$ und jede natürliche Zahl a gilt: $a^p=a\mod p$

**Beweis**
Über Kombinatorik.
$p|a^p-a$

$\frac{a^p-a}{p}$ Möglichkeiten, das alle Farben verschieden rotierbar sind.
$a$ Möglichkeiten, das alle die selbe Farbe haben.
$\frac{a^p-a}{p}+a\in\mathbb{N}$, ist Teil der Menge der natürlichen Zahlen, weil es Kombinatorik ist. Da $a$ eine natürliche Zahl ist, muss $\frac{a^p-a}{p}$ auch eine natürliche Zahl sein und somit durch $p$ teilbar sein.

**Beweis**
Über vollständige Induktion.

$IA: a=1$ für $a^p=a\mod p$
$IV: p|a^p-a$
$IB: p|(a+1)^p-(a+1)$
$IS: 0=0\mod p$
$\sum^{p-1}_\limits{i=1}\frac{p!}{i!(p-i)!}*a^i=0\mod p$
$\sum^{p-1}_\limits{i=1}\binom{p}{i}*a^i=0\mod p$
$p|(a+1)^p-a^p-1$
$p|(a+1)^p-a^p-1+a-a$
$p|(a+1)^p-a-1-(a^p-a)$
$p|(a+1)^p-a-1$