# Bildverarbeitung – Projekt und Technik

## Projektidee

Das gemeinsame Studienprojekt von 2025 untersucht grundlegende Schritte der Bildverarbeitung. Eine gezeichnete Ziffer dient als Eingabe. Bilddaten werden in eine numerische Matrix überführt und durch Faltung und einen Maximumfilter weiterverarbeitet.

## Verarbeitung

| Funktion | Aufgabe |
| --- | --- |
| `load_image` | Bild mit Pillow öffnen |
| `get_stuff_from_image` | RGB-Werte in eine Binärmatrix umwandeln |
| `make_matrix` | Kernel drehen und auf Bildregionen anwenden |
| `max_matrix` | Größten Wert eines gleitenden Fensters bestimmen |
| `plot_image` | Matrix mit Matplotlib als Graustufenbild anzeigen |

Die RGB-Kanäle eines Pixels werden addiert. Eine Summe ab 255 ergibt den Matrixwert 0, eine kleinere Summe den Wert 255. Der Alphakanal geht nicht in die Berechnung ein.

Der eingestellte Kernel lautet:

```text
-1   2  -1
-1   2  -1
-1   2  -1
```

`make_matrix` dreht den Kernel um 180 Grad. Das Fenster rückt jeweils um seine eigene Breite und Höhe weiter. Der anschließende Maximumfilter verwendet überlappende 3×3-Fenster mit einer Schrittweite von einem Element.

Bei der mitgelieferten 1000×1000-Eingabe entstehen zunächst 333×333 und danach 331×331 Elemente. Für die zweite Faltung bleibt die Größe des Eingabebildes die Referenz. Ihre Ergebnismatrix hat daher erneut 333×333 Elemente, bevor der Maximumfilter sie auf 331×331 reduziert. Die [Galerie](GALERIE.md) zeigt die vollständige Folge.

## Aufbau

![Technikübersicht](media/technik.svg)

`test.py` enthält die Verarbeitung und den Programmstart. Im Projekt liegen die PNG-Eingabebilder `0.png`, `1.png` und `test_img_1.png`. NumPy übernimmt die Matrixoperationen, Pillow das Einlesen und Matplotlib die Darstellung.

## Start

Eine eigene Python-Umgebung hält die Projektbibliotheken zusammen. Im Projektordner:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install numpy pillow matplotlib
.venv\Scripts\python.exe test.py
```

Unter Linux:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install numpy pillow matplotlib
.venv/bin/python test.py
```

Die gezeigten Ausgaben verwenden NumPy 2.3.5, Pillow 13.0.0 und Matplotlib 3.11.2. Jedes Diagrammfenster schließen, um zum nächsten Verarbeitungsschritt zu wechseln. Das Eingabebild wird im Arbeitsverzeichnis gesucht.

## Bilder

Die fünf Diagramme wurden direkt aus dem unveränderten Programm gespeichert. Die Darstellung verwendet dessen Graustufen-Farbskala und Beschriftungen.

[Zur Übersicht](../README.md) · [Galerie](GALERIE.md). Alle Angaben und Downloads ohne Gewähr.
