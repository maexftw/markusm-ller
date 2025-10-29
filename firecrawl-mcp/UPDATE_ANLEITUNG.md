# ⚠️ WICHTIG: Bestehende Konfiguration aktualisieren

Sie haben bereits eine Claude Desktop Konfiguration mit anderen MCP-Servern!

## 🔄 So aktualisieren Sie die Konfiguration:

### Option 1: Automatisch ersetzen (EMPFOHLEN)

1. **Öffnen Sie Windows Explorer**

2. **Geben Sie in die Adresszeile ein:**
   ```
   %APPDATA%\Claude
   ```

3. **Erstellen Sie ein Backup Ihrer aktuellen Konfiguration:**
   - Kopieren Sie `claude_desktop_config.json`
   - Benennen Sie die Kopie um in `claude_desktop_config_BACKUP.json`

4. **Ersetzen Sie die Datei:**
   - Kopieren Sie diese Datei:
     ```
     I:\Ai Claude\Markus Müller\firecrawl-mcp\claude_desktop_config_UPDATED.json
     ```
   - Nach:
     ```
     %APPDATA%\Claude\claude_desktop_config.json
     ```
   - (Überschreiben Sie die alte Datei)

5. **Starten Sie Claude Desktop neu**

---

### Option 2: Manuell hinzufügen

Falls Sie die Konfiguration manuell bearbeiten möchten:

1. **Öffnen Sie:**
   ```
   %APPDATA%\Claude\claude_desktop_config.json
   ```

2. **Fügen Sie im `mcpServers` Bereich hinzu:**
   ```json
   "firecrawl": {
     "command": "node",
     "args": [
       "I:\\Ai Claude\\Markus Müller\\firecrawl-mcp\\dist\\index.js"
     ],
     "env": {
       "FIRECRAWL_API_KEY": "fc-d21288c226fd43bba3a8ca4418996218"
     }
   }
   ```

3. **Die komplette Datei sollte so aussehen:**
   ```json
   {
     "mcpServers": {
       "webflow": {
         "command": "npx",
         "args": [
           "mcp-remote",
           "https://mcp.webflow.com/sse"
         ]
       },
       "firecrawl": {
         "command": "node",
         "args": [
           "I:\\Ai Claude\\Markus Müller\\firecrawl-mcp\\dist\\index.js"
         ],
         "env": {
           "FIRECRAWL_API_KEY": "fc-d21288c226fd43bba3a8ca4418996218"
         }
       }
     },
     "preferences": {
       "legacyQuickEntryEnabled": false,
       "menuBarEnabled": false
     }
   }
   ```

4. **Speichern und Claude Desktop neu starten**

---

## ✅ Prüfen, ob es funktioniert

Nach dem Neustart von Claude Desktop:

1. Fragen Sie: **"Welche MCP Tools habe ich verfügbar?"**
2. Sie sollten sehen:
   - Webflow Tools (Ihre bestehenden)
   - **scrape_url** (NEU!)
   - **crawl_website** (NEU!)
   - **map_website** (NEU!)

## 🚀 Jetzt loslegen!

Sobald die Tools verfügbar sind, können Sie sagen:

```
Scrape bitte diese Website: https://example.com
```

Und ich baue sie 1:1 für Sie nach!
