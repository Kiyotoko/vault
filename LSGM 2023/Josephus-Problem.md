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
$JP=[4,8,2,7,4,10,6]$

#### k = 2

$f:\mathbb{N}\to\mathbb{N}$, wobei $f(n)$ das letzte Objekt der Josephus-Permutation für n

****