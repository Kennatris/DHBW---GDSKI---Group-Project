# Bildverarbeitung mit Faltung und Maximumfilter

**Python · NumPy · Pillow · Matplotlib · Teamprojekt / 2025**

Wie werden aus einem Bild Zahlen und daraus sichtbare Strukturen? Dieses Projekt liest eine gezeichnete Ziffer als Pixelmatrix ein und verarbeitet sie mit einem 3×3-Filter. Die einzelnen Schritte werden als Graustufenbilder dargestellt.

| Eingabematrix | Nach Faltung und Maximumfilter |
| --- | --- |
| ![Binäre Eingabematrix](docs/media/01-binaermatrix.png) | ![Maximumfilter nach der ersten Faltung](docs/media/03-maximum-1.png) |

[Projekt und Technik](docs/PROJEKT.md) · [Alle fünf Ausgaben](docs/GALERIE.md) · [Quellcode herunterladen](https://github.com/Kennatris/DHBW---GDSKI---Group-Project/archive/refs/heads/main.zip)

## Ablauf

1. Pillow lädt das Bild und liest seine Farbwerte.
2. Aus der RGB-Summe entsteht eine Matrix mit den Werten 0 und 255.
3. NumPy berechnet die Faltung mit einem gedrehten 3×3-Kernel.
4. Ein gleitender Maximumfilter hebt lokale Maximalwerte hervor.
5. Die Filterfolge wird zweimal durchlaufen und mit Matplotlib angezeigt.

![Technikübersicht](docs/media/technik.svg)

## Ausführen

Benötigt werden Python sowie NumPy, Pillow und Matplotlib. `test.py` startet mit dem mitgelieferten Bild `0.png` und öffnet nacheinander fünf Diagramme. Die [Startanleitung](docs/PROJEKT.md#start) beschreibt die Einrichtung in einer eigenen Python-Umgebung.

Die gezeigten Bilder sind gespeicherte Ausgaben des unveränderten Programms.

> **Hinweis:** Dokumentation und Zusammenfassung wurden automatisiert durch einen Agenten erstellt und dienen der Veranschaulichung. Der Programmcode ist unverändert. Alle Angaben und Downloads ohne Gewähr.
