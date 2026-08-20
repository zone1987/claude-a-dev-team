# Shopware Publisher – Draft-Management für Erlebniswelten

**Quelle**: https://docs.shopware.com/de/shopware-6-de/erweiterungen/ShopwarePublisher  
**Plan**: Shopware Evolve (oder höher)

## Überblick

Der **Shopware Publisher** ermöglicht kollaboratives Content-Management:
Mehrere Versionen (Drafts) einer Erlebniswelt erstellen, ohne die **aktive Live-Version** zu verändern.

Ideal für:
- Saisonale Kampagnen vorbereiten
- Content-Reviews vor Veröffentlichung
- Team-Kollaboration an Landing-Pages

---

## Installation

1. **Erweiterungen > Meine Erweiterungen** öffnen
2. Im **Shopware Account Tab** einloggen (Lizenzverifizierung)
3. Publisher installieren + aktivieren (**Apps Tab**)

---

## Kernfunktionen

### 1. Draft-Erstellung

**Normales Speichern** (ohne Publisher): Direkt in Live-Version  
**Mit Publisher**: Dropdown-Pfeil neben dem Speicher-Button → "Als neuen Entwurf speichern"

Optionen beim Speichern:
| Option | Beschreibung |
|---|---|
| Direkt speichern | Sofort in die Live-Version übernehmen |
| Als neuen Entwurf speichern | Neue Draft-Version erstellen (Live unverändert) |

### 2. Drafts verwalten

In der **Erlebniswelten-Übersicht** (Content > Erlebniswelten):
- Neben jeder Erlebniswelt: Anzahl der Drafts und Live-Version sichtbar
- Anzahl der kürzlich gemachten Änderungen anderer Nutzer

### 3. Aktivitäts-Feed (Activity Tracking)

Ein integrierter Feed zeigt:
- Welcher Benutzer hat Änderungen gemacht
- Was wurde geändert
- Wann wurde geändert

Gilt sowohl für Live-Version als auch für Drafts.

### 4. Preview (Vorschau)

Drafts können in der **Storefront-Vorschau** angezeigt werden, bevor sie veröffentlicht werden:
- Erlebniswelt öffnen → Draft auswählen → "Vorschau" klicken
- Zeigt genau, wie der Draft im Frontend aussehen würde

---

## Workflow-Beispiel: Saisonale Kampagne

```
1. Aktuelle Startseite (Live)  
   └── Draft: "Weihnachten 2024" (wird parallel erstellt)
       ├── Bearbeitung durch Content-Team
       ├── Review durch Marketing-Lead
       ├── Vorschau prüfen
       └── Am 1. Dezember: Draft → Live publizieren
```

---

## Benutzerrechte für den Publisher

Unterschiedliche Benutzerrollen können unterschiedliche Publisher-Berechtigungen haben:

| Berechtigung | Beschreibung |
|---|---|
| Drafts erstellen | Neuen Entwurf anlegen |
| Drafts bearbeiten | Vorhandenen Entwurf ändern |
| Drafts publizieren | Entwurf zur Live-Version machen |
| Drafts löschen | Entwürfe entfernen |

Benutzerrechte: **Einstellungen > System > Benutzer & Rechte > Rollen**

---

## Unterschied zu Standard-Erlebniswelten-Speicherung

| Aspekt | Ohne Publisher | Mit Publisher |
|---|---|---|
| Speichern = Live | Ja, sofort | Nein – erst nach Publish |
| Mehrere Versionen | Nein | Ja (unbegrenzt viele Drafts) |
| Vorschau | Ja (aber Live) | Ja (Drafts vorschaubar) |
| Änderungshistorie | Nein | Ja (Activity Feed) |
| Rollback | Eingeschränkt | Ja (Draft aktivieren) |
