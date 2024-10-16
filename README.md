# VP Ticket Tagging

**VP Ticket Tagging** ist ein Odoo 17 Modul, das automatisch Tags zu Kundendienst-Tickets basierend auf dem Betreff und Inhalt eingehender E-Mails hinzufügt. Schlagwörter und zugehörige Tags können von Benutzern der Rolle "VP Ticket Tagging" verwaltet werden.

## Features

- Automatische Tag-Zuweisung basierend auf vordefinierten Schlagwörtern im E-Mail-Betreff und -Inhalt.
- Verwaltung von Schlagwörtern und Tags im Kundendienstmodul (Helpdesk).
- Benutzerrollen-basierter Zugriff auf die Verwaltung von Schlagwörtern (nur Benutzer der Gruppe **"VP Ticket Tagging"**).

## Voraussetzungen

- Odoo 16, 17
- Module: `mail`, `helpdesk`

## Installation

1. Kopiere den Modulordner `vp_ticket_tagging` in das Odoo-Addons-Verzeichnis.

2. Melde dich im Odoo-Backend an und gehe zu Apps, aktualisiere die App-Liste. Suche nach VP Ticket Tagging und installiere das Modul.

## Berechtigungen

Die Verwaltung der Regeln kann nur von Benutzern der Gruppe **VP Tagging Manager** durchgeführt werden.
- Zugriffsrechte für das Modul sind über die Odoo-Benutzerverwaltung zuweisbar.

## Verwendung
**Automatisches Tagging**

1. Jedes Mal, wenn ein Kunde eine E-Mail sendet, die in ein Ticket umgewandelt wird, überprüft das Modul den Betreff und den Inhalt der E-Mail auf vordefinierte Suchbegriffe.

2. Wenn ein Suchbegriff gefunden wird, wird automatisch das entsprechende Tag dem Ticket hinzugefügt.

**Verwaltung der Suchbegriffen**

1. Benutzer mit der Rolle **VP Ticket Tagging Manager** können im Menü Kundendienst > Tag-Schlagwörter Tags und Schlagwörter hinzufügen, bearbeiten oder löschen.

2. Suchbegriffe, Tags und Kundendienstteams verwalten: Benutzer mit der Rolle **VP Ticket Tagging Manager** können nun im Kundendienst-Modul unter dem Menüpunkt **Automatisches Ticket Tagging** Suchbegriffe entsprechenden Tags und Kundendienstteams zuordnen.

2. Suchbegriffe müssen als Komma-getrennte Liste eingegeben werden. Zum Beispiel:

```csv
Telefon;Timio;Jabber
```

Diese Suchbegriffe lösen das Tagging für alle E-Mails aus, die eines dieser Wörter im Betreff oder im Text enthalten und dem entsprechenden Kundendienstteam zugeordnet ssind.

## Sicherheit

Nur Benutzer mit der Rolle **VP Ticket Tagging Manager** haben Zugriff auf die Verwaltung von Schlagwörtern und Tags.

## Technische Details

Die automatische Tag-Zuweisung erfolgt über das Erweitern der Odoo-Klasse ***`mail.thread`***. Die Funktion ***```message_new```*** wird überschrieben, um den Inhalt der eingehenden E-Mails zu analysieren.

Schlagwörter und zugehörige Tags werden in einem eigenen Modell (***```ticket.tagging```***) gespeichert.

## Autor
BKK VerbundPlus, Christian Bopp 2024

## Lizenz
Dieses Modul ist unter der LGPL-3-Lizenz lizenziert. Weitere Informationen findest Du in der LICENSE-Datei.

