---
author: karlz
tags:
- Mathe
- LSGM
---

## Problem

- $n$ nummerierte Objekte werden im Kreis angeordnet.
- Jedes $k$-te Objekt wird entfernt (beginnend mit Objekt $k$)
- Nach jeder Runde wird der Kreis neu geschlossen
- Bei gegebenen $n,k\in\mathbb{N} (n\ge k)$ soll das letzte Objekt der Josephus-Permutation bestimmt werden

### Josephus-Permutation

Die Reihenfolg der entfernten Objekte wird als Josephus-Permutationbezeichnet.

**Beispiel**
$n=13,k=3$
$JP=[3,6,9,12,2,7,11,4,10,5,1,8,13]$

**Aufgabe**
Bestimme die Josephus-Permutation für $n=10,k=4$
$JP=[4,8,2,7,3,10,9,1,6,5]$

#### Permutation für $k=2$

$f:\mathbb{N}\to\mathbb{N}$, wobei $f(n)$ das letzte Objekt der Josephus-Permutation für n

**Aufgabe**
Bestimme für $f(n)\forall n\in[1,\dots8]$

| n    | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| f(n) | 1   | 1   | 3   | 1   | 3   | 5   | 7   | 1   |

**Satz**
Im ersten Durchlauf werden alle Objekte mit gerader Zahl eliminiert.

**Beweis**
Nach der ersten Runde sind nach die Objektnummern $1,3,\dots2n-3,2n-1$ im Kreis. Die 3 eröffnet nun die nächste Runde, $\forall j\in[1,3,\dots,2n-3,2n-1]$ sei $i=\frac{j+1}{2}\in\mathbb{N}$, d. h. $1\to1,3\to2,5\to3,\dots,2n-1\to n$. Nun startet man das Problem für n. Das letzte Objekt der Josephus-Permutation bleibt dabei offensichtlich gleich. Es gilt also umgekehrt $jP2i-1$.
$f(2n)=2f(n)-1$

**Hinweis**
Die Rekursionen
1. $f(1)=1$
2. $f(2n)=2f(n)-1$
3. $f(2n+1)=2f(n)+1$

beschreiben $f(n)$ vollständig.

**Aufgabe**
$f(11)=2f(5)+1=2(2f(2)+1)+1=2(2(2f(1)-1)+1)+1=2*3+1$

**Beweis**
$f(2^n)=1\forall n\in\mathbb{N}$
$IA: n_0\to f(2^{n_0})$
$IV: f(2^n)=1\forall n\in\mathbb{N}$
$IB: f(2^{n+1})=1$
$IS: f(2^{n+1})=f(2*2^n)=2f(2^n)-1$

Induktionsvorraussetzung: $2-1=1$