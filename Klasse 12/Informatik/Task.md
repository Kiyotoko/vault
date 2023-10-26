---
author: karlz
tags:
  - Informatik
  - FGB
---


## 2023-09-07

```py
Kunden(Nummer, Name, Vorname, Strasse, PLZ, Ort, Geburtsdatum, Telephon, Datum, Führerscheinerwerb)
PKW(Kennzeichen, Modell, Erstzulassung, kmStand, Modellname)
Werkstatt(Name, Strasse, PLZ, Ort, Telephon, Kontaktperson)
Modell(Name, Hersteller, Leistung, Laenge, Breite, Hubraum, Herstellername)
Hersteller(Name, Strasse, PLZ, Ort, Telephon, Kontaktperson)

Ausleihe(fortlaufendeNummer, Kundennummer, Kennzeichen, Ausleihdatum, Rueck- gabedatum) Reparatur(Vorgangsnummer, Werkstatt, Kennzeichen, Datum, Dauer, Art)
```

## 2023-10-26

```SQL
CREATE TABLE AG (Name VARCHAR, Beginn TIME, Tag VARCHAR, AGLeiter VARCHAR, Zimmer VARCHAR)
```

```SQL
INSERT INTO AG (Name, Beginn, Tag, AGLeiter) VALUES ("Fußball", 15:00, "Mo", "Komischke", "Sportplatz")
```

```SQL
UPDATE AG SET AGLeiter="Stenzel" WHERE AGLeiter="Pophal"
```

---

```SQL
SELECT Vorname FROM Tabelle1, Tabelle2 WHERE Tabelle1.Vorname=Tablle2.Vorname

> Vorname
> ---------
> Tina
> Franziska
```

```SQL
SELECT DISTINCT Wohnort FROM Tabelle2

> Wohnort
> -------
> Leipzig
> Dresden
```

```SQL
SELECT * FROM Tabelle1 WHERE Vorname LIKE "T%"

> Vorname | Geschlecht | Geburtsdatum
> --------+------------+-------------
> Tina    | w          | 28:03:05
```

```SQL
SELECT Geburtsdatum, Wohnort FROM Tabelle1, Tabelle2 WHERE Vorname.Tabelle1 = Vorname.Tabelle2

> Geburtsdatum | Wohnort
> -------------+--------
> 02:03:05     | Leipzig
> 05:09:97     | Dresden
```