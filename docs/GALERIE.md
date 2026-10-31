# Bildverarbeitung – Galerie

Die fünf Ansichten zeigen die vollständige Verarbeitung des mitgelieferten Bildes `0.png`. Sie sind direkt gespeicherte Matplotlib-Ausgaben des Programms.

## Binärmatrix

Das Eingabebild wird in Werte von 0 und 255 überführt.

![Binärmatrix](media/01-binaermatrix.png)

## Erste Faltung

Der 3×3-Kernel betont Strukturen der gezeichneten Ziffer.

![Erste Faltung](media/02-faltung-1.png)

## Erster Maximumfilter

Überlappende Fenster wählen jeweils den größten Wert.

![Erster Maximumfilter](media/03-maximum-1.png)

## Zweite Faltung

Die Verarbeitung setzt mit der bereits gefilterten Matrix fort.

![Zweite Faltung](media/04-faltung-2.png)

## Zweiter Maximumfilter

Die letzte Ansicht schließt die zweite Filterfolge ab.

![Zweiter Maximumfilter](media/05-maximum-2.png)

[Projekt und Technik](PROJEKT.md) · [Zur Übersicht](../README.md). Alle Angaben und Downloads ohne Gewähr.
