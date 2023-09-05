---
author: karlz
tags: 
- Informatik
- FGB
---

# Datenmodellierung und Datenbanken

## Modellierung in der Informatik

Ein Modell ist eine vereinfachte Beschreibung eines realen oder geplanten Systems

### Datenmodellierung

Bei der Datenmodellierung werden Daten in Beziehung gesetzt

### Datenflussmodellierung

Bei der Datenflussmodellierung werden komlpexe Systeme in überschaubare Teilsysteme zerlegt und der Informationsfluss zwischen den Teilen untersucht. Dabei helfen nomierte Diagramme , die aus folgenden Elemente bestehen:
- Zylinder: beständiges Datenobjekt
- Ellipse: informationsverarbeitender Prozess
- Rechteck: Datenquelle/Datensenke

## Modelle in der Informatik

### Hierarchisches Datenbankmodell

![](Working%20Materials/Datenmodellierung%20und%20Datenbanken/Hierarchisches%20Datenbankmodell.png)

Das hierarchische Datenbankmodell bildet die reale Welt durch eine hierarchische Baumstruktur ab. Jeder Satz (engl. Record) hat also genau einen übergeordneten Vorgänger, mit Ausnahme genau eines Satzes, nämlich der Wurzel der so entstehenden Baumstruktur. 

### Entity-Relationship-Modell

![](Working%20Materials/Datenmodellierung%20und%20Datenbanken/ER-Modell.png)

Das Entity-Relationship-Modell – kurz ER-Modell oder ERM (mit der sinngemäßen Bedeutung „Modell zur Darstellung von Dingen / Gegenständen / Objekten und deren Beziehungen“) – dient dazu, im Rahmen der semantischen Datenmodellierung den in einem gegebenen Kontext (z. B. einem Projekt zur Erstellung eines Informationssystems) relevanten Ausschnitt der realen Welt zu bestimmen und darzustellen. Das ER-Modell besteht im Wesentlichen aus einer Grafik (ER-Diagramm, Abk. ERD) sowie einer Beschreibung der darin verwendeten Elemente. 

- **Entität** Objekt der realen Welt bzw. der Vorstellung
- **Entitätstypen** Entitäten mit gleichen Eigenschaften
- **Attribute** Eigenschaften der Entitäten
- **Beziehungen** Von Entitätstypen
- Kardinalität
- Primärschlüssel
- Fremdschlüssel

## Datenbanksysteme

**Definition**
Ein **Datenbanksystem** ist eine systematische und strukturierte Zusammenfassung von Daten eines Problembereiches (**Datenbasis**) einschließlich der zur Eingabe, Verwaltung, Auswertung und Ausgabe erforderlichen Software (Datenbankmanagmentsystem, DBMS)

Nach der Modellierung der verwalteten Daten unterscheidet man folgende Datenbankkarten:
- relationale Datenbanken
- hierarchische Datenbanken
- Netzwerk-Datenbanken