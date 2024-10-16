# Security Policy

## Verantwortliche Personen

Für alle sicherheitsrelevanten Fragen und Berichte im Zusammenhang mit dem Modul **VP Ticket Tagging** wenden Sie sich bitte an:

- **Name des Entwicklers**: BKKVerbundPlus, Christian Bopp <cbopp@bkkvp.de>

## Sicherheitsrichtlinien

Das Modul **VP Ticket Tagging** wurde entwickelt, um sicherzustellen, dass nur berechtigte Benutzer bestimmte Funktionen ausführen können. Es wurden verschiedene Sicherheitsmechanismen implementiert, um den Zugriff auf sensible Daten und Funktionen zu beschränken.

### 1. Benutzerrollen und Berechtigungen

Das Modul verwendet eine eigene Benutzerrolle **VP Ticket Tagging Manager**, die nur berechtigten Benutzern den Zugriff auf die Verwaltung von Schlagwörtern und Tags im Kundendienstmodul ermöglicht. Benutzer ohne diese Rolle haben keinen Zugriff auf die Verwaltung dieser Daten.

**Zugriffssteuerungen:**
- Nur Benutzer der Gruppe **VP Ticket Tagging Manager** haben Leseberechtigungen, Schreibberechtigungen, Erstellungs- und Löschrechte für das Modell `ticket.tagging` (Tag-Schlagwörter).
- Standardmäßig hat nur der Administrator das Recht, die Rolle **VP Ticket Tagging Manager** an Benutzer zu vergeben oder zu entziehen.

### 2. Datenvalidierung und Sicherheit

- **Suchbegriffe**: Die Eingabe der Suchbegriffe erfolgt als Komma-getrennte Liste. Es gibt eine Validierung, die sicherstellt, dass keine unerwünschten Zeichen oder unsicheren Eingaben gemacht werden.
- **Tag-Zuweisung**: Die automatische Tag-Zuweisung erfolgt nur, wenn vordefinierte Stichwörter in den E-Mail-Betreff oder -Text sowie das entsprechende Kundendienstteam übereinstimmen.

### 3. Schutz vor unberechtigtem Zugriff

- Das Modul verwendet Odoo-integrierte Zugriffskontrollen, um sicherzustellen, dass nur berechtigte Benutzer (Benutzer der Gruppe **VP Ticket Tagging Manager**) Zugriff auf sensible Informationen und Funktionen haben.
- Benutzer ohne die erforderlichen Berechtigungen haben keinen Zugriff auf die Verwaltung der Tags oder Schlagwörter.

### 4. Melden von Sicherheitsproblemen

Wenn Sie ein Sicherheitsproblem im Zusammenhang mit dem Modul **VP Ticket Tagging** gefunden haben, melden Sie dies bitte umgehend. Wir behandeln solche Meldungen mit höchster Priorität und arbeiten daran, das Problem so schnell wie möglich zu beheben.

**Berichtsprozess:**
1. Beschreiben Sie das Sicherheitsproblem klar und detailliert.
2. Schicken Sie eine E-Mail an: it@bkkvp.de
3. Falls möglich, fügen Sie Schritte hinzu, um das Problem zu reproduzieren.

## Sicherheitshinweise

**Empfohlene Maßnahmen:**
- Stellen Sie sicher, dass nur berechtigte Administratoren die Benutzerrolle **VP Ticket Tagging** verwalten können.
- Überprüfen Sie regelmäßig, ob alle Benutzer der **VP Ticket Tagging Manager**-Gruppe wirklich berechtigt sind, Zugriff auf die Stichwort- und Tag-Verwaltung zu haben.
- Halten Sie Ihre Odoo-Installation auf dem neuesten Stand, um sicherzustellen, dass bekannte Sicherheitslücken rechtzeitig behoben werden.

## Versionsverlauf

- **Version 17.0.1.0**: Initiale Veröffentlichung des Moduls mit integrierten Sicherheitsfeatures.

---

**Hinweis:** Sicherheit ist eine kontinuierliche Aufgabe. Es wird empfohlen, das Modul regelmäßig zu überprüfen und alle Sicherheitslücken sofort zu melden.
