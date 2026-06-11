# Livegang nach der Migration

**Quelle**: https://docs.shopware.com/de/migration-de/Livegang

---

## Überblick

Der Livegang erfolgt in drei Bereichen:
1. Änderungen im **Shopware 6 Zielshop**
2. Änderungen im **Quellshop** (SW5 / SW6 / Magento)
3. Änderungen beim **Hoster** (DNS-Routing)

Danach: Migrationsdaten aufräumen.

---

## 1. Änderungen im Shopware 6 Zielshop

### 1.1 Lizenzierungshost umtragen

**Pfad:** Einstellungen > System > Shopware Account

- Hauptdomain eintragen, unter der der neue Shop erreichbar sein soll
- Zweck: Shopware-Lizenz korrekt der Domain zuordnen

### 1.2 Domain in Verkaufskanälen umtragen

**Pfad:** Administration > Verkaufskanäle

- Jeder Verkaufskanal hat ein URL-Feld
- Neue Hauptdomain eintragen
- Feld: **„URL"**

> ⚠️ Dieser Schritt muss für **jeden Subshop / Verkaufskanal separat** durchgeführt werden!

---

## 2. Änderungen im Quellshop

### Shopware 5
- Shop in einen Unterordner legen
- Unterordner in Einstellungen > Shopeinstellungen > Shops eintragen
- Ziel: Hauptdomain wird für SW6 freigegeben

### Shopware 6
- Domain im Verkaufskanal auf neue (Ausweich-)Domain umtragen
- Hauptdomain wird für Zielshop freigegeben

### Magento
- Magento so konfigurieren, dass es **nicht mehr unter Hauptdomain** erreichbar ist
- Stattdessen neue/andere Domain für Magento einstellen

---

## 3. Änderungen beim Hoster (DNS-Routing)

Die **Shopdomain muss auf das Unterverzeichnis `/public/`** im Shopware-6-Installationsverzeichnis routen.

### Apache-Konfiguration (Beispiel)

```apache
<VirtualHost *:80>
    ServerName "_HOST_NAME_"
    DocumentRoot _SHOPWARE_DIR_/public

    <Directory _SHOPWARE_DIR_>
        Options Indexes FollowSymLinks MultiViews
        AllowOverride All
        Order allow,deny
        allow from all
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/shopware-platform.error.log
    CustomLog ${APACHE_LOG_DIR}/shopware-platform.access.log combined
    LogLevel debug
</VirtualHost>
```

**Platzhalter ersetzen:**
- `_HOST_NAME_` → eigene Domain (z.B. `www.meinshop.de`)
- `_SHOPWARE_DIR_` → absoluter Pfad zur SW6-Installation (z.B. `/var/www/shopware6`)

> **Wichtig:** `DocumentRoot` zeigt auf `/public/` — nicht auf das Hauptverzeichnis!

---

## 4. Migrationsdaten aufräumen

Nach erfolgreichem Livegang sollten die Migrationsdaten aus der Datenbank entfernt werden.

**Pfad:** Einstellungen > Erweiterungen > Migrations-Assistent

**Aktion:** Kontextmenü > **„Migrationsdaten aufräumen"**

**Effekt:** Löscht alle für die Migration zwischengespeicherten Datensätze aus der Datenbank.

> ⚠️ **Nach dem Aufräumen** können keine Daten-Updates mehr über den Migrationsassistenten
> aus dem Quellshop übertragen werden!

### Wichtiger Hinweis für SW5 mit Plugin-Migrationsassistent
Falls während der Migration der **Plugin-Migrationsassistent** genutzt wurde, um Testlizenzen zu buchen:
→ Dort zuerst die **Migration finalisieren**, bevor im Migrationsassistenten „Migration abschließen" geklickt wird!

---

## Magento-spezifischer Hinweis: Erweiterung nicht deinstallieren

> ⚠️ Bei einer Magento-Migration: Die **Migrationserweiterung NICHT deinstallieren!**
>
> Begründung: Die von Magento verwendeten **Passwort-Algorithmen** sind in der Erweiterung
> enthalten. Ohne die Erweiterung können sich migrierte Kunden **nicht mehr einloggen**.

---

## Checkliste Livegang

- [ ] Lizenzierungshost in SW6 auf neue Domain umgetragen (Einstellungen > System > Shopware Account)
- [ ] Domain in **allen** Verkaufskanälen umgetragen
- [ ] Quellshop auf Unterordner / alternative Domain umgestellt
- [ ] Apache/Nginx: DocumentRoot zeigt auf `/public/`
- [ ] DNS-Propagation abgewartet (kann einige Zeit dauern)
- [ ] Shop unter neuer Domain erreichbar und funktionsfähig
- [ ] Migrationsdaten aufgeräumt (Kontextmenü > „Migrationsdaten aufräumen")
- [ ] Bei Magento: Migrationserweiterung NICHT deinstalliert

---

*Quelle: https://docs.shopware.com/de/migration-de/Livegang*
