# Bohrsches Atommodell

## Postulate

1. Es existieren stabile Bahnen, auf denen die Elektronen kreisen, ohne Strahlung auszusenden.
2. Es sind nur Bahnen erlaubt, für die gilt: $m\cdot v\cdot r=n \frac{h}{2\pi}$
3. Die Emissionen oder Absorption von Photonen erfolgt genau dann, wenn ein Elektron von einer erlaubten Bahn auf eine andere erlaubte Bahn wechselt.
4. Jeder erlaubten Elektronenbahn entspricht eine bestimmte Energie der Elektronen. Wechselt ein Elektron die Bahn, so ist die Energie emittierten bzw. absorbierten Photons gleich der Energiedifferenz der Bahnenergien.

## Energieniveaus

$E_{\text{ges}}=-\frac{e^{4}m}{8\epsilon_{0}^{2}h^{2}}\cdot\frac{1}{n^{2}}$

Lyman Serie $E_{n\to1}$
Balmer Serie $E_{n\to2}$
Paschen Serie $E_{n\to3}$

## Serienformel für Wasserstoff

Geht ein Elektron von der $m$-ten auf die $n$-te Bahn (Zustand) über mit $m>n$, dann wird ein Photon mit der Energie $E_{\text{ph}}=E_{m}-E_{n}$ ausgestrahlt.

$R_{H}=\frac{e^{4}m}{8\epsilon_{0}^{2}h^{3}}=3.2898\cdot10^{15}Hz$
$E_\text{ph}=h\cdot f=h\cdot R_{H}(\frac{1}{n^{2}}- \frac{1}{m^{2}})$
$f=\frac{E_{\text{ph}}}{h}=R_{H}(\frac{1}{n^{2}}- \frac{1}{m^{2}})$

## Möglichkeiten und Grenzen

| Möglichkeiten 👍                                                                                | Grenzen 👎                                                                                                                  |
| ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Ermöglicht eine Abschätzung des Atomradius                                                      | Widerspruch von diskreten Bahnen (Kreisbahnen) zur Quantentheorie (Quantenteilchen bewegen sich nicht auf konkreten Bahnen) |
| Spektrallinien für Wasserstoff können berechnet werden                                          | Modell versagt bei Vorhersagen für Atome mit mehr als einem Elektron (nur Wasserstoffatom beschreibbar)                     |
| Führt quantentheoretische Erkenntnisse in die Atomtheorie ein (Emission & Absorption von Licht) | Postulate erscheinen willkürlich (Elektronen senden keine Strahlen aus)                                                     |

# Quantenmeschanische Atommodell

## Heisenbergsche Unbestimmtheitsrelation

Ort und Impuls $\Delta x\cdot\Delta p_{x}\ge \frac{h}{4\pi}$

Energie und Zeit $\Delta E\cdot\Delta t\ge \frac{h}{4\pi}$

## Unendlich hoher Potenzialtopf

![](../Working%20Materials/Atommodell/Potenzialtopf.png)

$V_{n}(x)=|\Psi_{n}|^{2}$
$E_{n}=\frac{h^{2}}{8mL^{2}}n^{2}\quad\text{mit}\;n=1,2,3,\dots$

## Schrödinger Gleichung

$$i \frac{h}{2\pi} \frac{\partial \Psi}{\partial t}=\hat{H}\Psi$$

## Orbitale

![](../Working%20Materials/Atommodell/Orbitale.png)

Zustände werden über "stehende Wellen" definiert → Lösungen der Schrödinger Gleichung

Einer vorgegebenen Hauptquantenzahl $n$ kann man $2n^{2}$ verschiedene Kombinationen aus $n,l,m$ und $s$ zuordnen → Anzahl Elektronen pro Schale

# Frank-Hertz Experiment

Durch die Beschleunigungsspannung $U_{B}$ werden die Elektronen von der Kathode bis zur Anode beschleunigt. Ab einer gewissen Spannung $U_{B}$ stoßen die Elektronen unelastisch mit den $Hg$-Atomen zusammen. Dadurch werden von den $Hg$-Atomen von dem Grundzustand in den nächst höheren Energiezustand gehoben. Wenn diese wieder in den Grundzustand zurückfallen, werden Photonen ausgesendet (Gas leuchtet).
Freie Elektronen, die durch unelastische Stöße mit dem $Hg$-Atomen Energie abgeben haben, besitzen nicht genug kinetische Energie, um die Gegenspannung zu überwinden. Dadurch kommen weniger Elektronen an der Anode an und die Stromstärke sinkt.

# Lumineszenz und Floreszenz

## Lumineszenz

- Bei Bestrahlung mit weißem Licht wird ein Atom von Photonen unterschiedlichster Frequenz bzw. Energie getroffen
- Das Atom kann ein Photon nur dann absorbieren wenn dessen Energie genau der Differenz zwischen zwei Atomaren Energieniveaus $E_{1}$ und $E_{2}$ entspricht
- $E_{\text{ph}}=h\cdot f=E_{2}-E_{1}$
- Das Photon der Resonanzabsorption wird für eine gewisse Zeit gespeichert
- Beim Übergang in ein niedrigeres Energieniveau wird das Photon wieder ausgesendet
- Das emittierte Photon hat eine niedrigere Frequenz als das absorbierte Photon, da ein Teil der Energie im Atom zurückbleibt

## Floreszenz

- Bestrahlung mit Licht
- Emittiertes Licht hat selbe Frequenz wie absorbiertes Licht
- Nur wenig Energie bleibt im Atom zurück
- Im Absorptionsspektrum entsteht eine Lücke, da kaum Energie im Atom zurückbleibt

# Laser

Spontane Emission: Emission eines Photons erfolgt spontan nach einer nicht genau bestimmten Zeit.

Stimulierte/Induzierte Emission: Emission eines Photons wird durch ein Photon mit gleicher Wellenlänge ausgelöst.

![](../Working%20Materials/Atommodell/Stimulierte%20Emission.jpg)

**Wirkungsweise**
- Energiequelle bringt Atome des aktiven Mediums (= Lasermedium) in einem angeregten Zustand (Pumpen)
- Durch spontane Emission werden Photonen ausgesendet
- Diese Photonen lösen durch stimulierte weitere Photonen aus
- An den Spiegeln werden die Photonen reflektiert und verstärken somit die induziert Emission
- Ein Teil der Photonen verlässt das aktive Medium als Laserstrahlung durch den halbdurchlässigen Spiegel