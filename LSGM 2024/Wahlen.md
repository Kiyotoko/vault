## Wahlsysteme

**Definition**
$A=\{a_{0},a_{1},\dots,a_{x}\}$ Kandidaten
$N=\{1,\dots,N\}$ Wahlberechtigte
Jeder hat Reihenfolge $R$ under Kandidaten, z.B. $R_{1}: a_{1}>a_{2}>a_{k}$ am besten

Wahlsystem Funktion: $\{(R_{1},R_{2},\dots,R_{i}),\dots\}\to A$

**Beispiel**
1. Meiste erste Stimmen gewinnt (UK)
	- Tie-Break: $a_{1}>a_{2}>\dots>a_{k}$
2. Bordacount:

| Listenplatz | Punkte |
| ----------- | ------ |
| 1           | k-1    |
| 2           | k-2    |
| ...         | ...    |
| k           | 0      |

3. Integrierte Stichwahl/Ranked Choice (Australien)
	- wenigsten Erststimmen raus
	- 
1. Stichwahl zwischen Top 2 (Fra)
2. Eliminierung: meiste letzte Stimmen raus
	- dann neu abstimmen

---

**Beispiel**
$k=5\quad N=100$

| Personen | Reihenfolge |
| -------- | ----------- |
| 31       | A>B>D>E>B   |
| 20       | B>D>C>E>A   |
| 19       | D>C>E>B>A   |
| 16       | E>C>B>A>D   |
| 14       | C>E>D>B>A   |

Beim ersten System: A Gewinnt
Beim dritten System: C fliegt raus, D fliegt raus, B fliegt raus, A fliegt raus, E gewinnt
Beim vierten System: B gewinnt