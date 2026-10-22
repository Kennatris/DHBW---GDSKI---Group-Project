# GDSKI: CNN-Gruppenprojekt: Projektleitfaden

[Einstieg](../README.md) · [Agentenregeln](../AGENTS.md) · Inventarstand 22.10.2026.

## Zweck und vorhandener Stand

Studienprojekt zu einem Convolutional Neural Network mit vorhandenem Python-Einstieg und Bildbeispielen.

Geprüfter Branch: `main`; Ausgangscommit `87685978e06de6baf7d5082790ae19d3716ab260`. Die folgende Struktur stammt aus dem vorhandenen Git-Baum, nicht aus einer behaupteten erfolgreichen Installation.

## Aufbau und Einstieg

Noch kein belastbarer ausführbarer Einstieg im geprüften Defaultbranch vorhanden.

Weitere vorhandene Hauptbereiche: `0.png`, `1.png`, `README.md`, `test.py`, `test_img_1.png`.

## Einrichtung und Prüfungen

Zuerst die vorhandenen Projekt-/Paketdateien und Agentenregeln lesen. Verfügbare Toolchain und Versionen vor Installation feststellen. Nur vorhandene Manifeste/Lockfiles verwenden; keine Abhängigkeiten aus dem Projektnamen erfinden.

```bash
python3 .github/scripts/check-project-docs.py
```

Das Dokumentationsgate arbeitet ohne Anwendungsausführung oder externe APIs. Weitere aufgeführte Befehle sind aus dem Projekt abgeleitete nächste Prüfungen; ihr erfolgreicher Lauf auf der Zielumgebung wird durch diesen Leitfaden nicht behauptet. Bei geräte-, GUI-, Broker- oder Datenbankabhängigen Prüfungen gelten die folgenden Grenzen.

## Daten, Betrieb und Sicherheit

Bildrechte und Datensatzherkunft erhalten, Trainings-/Testdaten trennen und Ergebnisse nicht erfinden. Das Skript test.py ist anhand des Namens noch kein nebenwirkungsfreier automatisierter Test.

Konfigurationen, Datenquellen, erzeugte Artefakte und ihre Aufbewahrung dokumentieren. Produktiv-/Nutzerdaten haben eine getrennte Sicherung und einen geprüften Rückweg. Keine Cloudübertragung, Kosten, Releases oder Deployments als Nebenwirkung eines Dokumentationstests.

## Änderungen und Abnahme

[Beitragsablauf](../CONTRIBUTING.md) beschreibt Branch, PR und Tests; [Sicherheitsmeldungen](../SECURITY.md) beschreibt den vertraulichen Meldeweg. Änderungen an Schnittstellen, Datenformaten oder Betrieb aktualisieren die Dokumentation im selben Change. Kleine nachvollziehbare Änderungen und ein datenkompatibler Rückweg gehören bei relevanten Eingriffen zur Abnahme.

## Lizenz und Herkunft

Im geprüften Baum wurde keine eigenständige Lizenzdatei nachgewiesen. Vor externer Wiederverwendung Rechte und Lizenz mit den Rechteinhabern klären; dieser Change wählt keine neue Lizenz.

## Offene Nachweise

- Eine reproduzierbare Python-/R-/Datenumgebung ist nicht vollständig durch ein gemeinsames Lockfile belegt. Notebookausführung, Datenrechte und Ergebnisreproduktion bleiben eigene Abnahmen.
- Branchschutz aktuell nicht als aktiv gemeldet; konkrete Regeln, Secret Scanning, Push Protection und Code Scanning wurden mit diesem Dokumentationschange nicht als vollständig eingerichtet nachgewiesen.
