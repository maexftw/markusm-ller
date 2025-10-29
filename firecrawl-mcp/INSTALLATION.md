# Installation Anleitung

## ✅ Was bereits erledigt ist:
- ✅ Dependencies installiert
- ✅ TypeScript kompiliert
- ✅ Server ist bereit

## 📋 Nächster Schritt:

### Claude Desktop Konfiguration einrichten

1. **Öffnen Sie den Windows Explorer**

2. **Geben Sie in die Adresszeile ein:**
   ```
   %APPDATA%\Claude
   ```

3. **Falls der Ordner nicht existiert:**
   - Erstellen Sie den Ordner manuell
   - Oder starten Sie Claude Desktop einmal, dann wird er automatisch erstellt

4. **Kopieren Sie die Datei:**
   ```
   I:\Ai Claude\Markus Müller\firecrawl-mcp\claude_desktop_config.json
   ```
   **Nach:**
   ```
   %APPDATA%\Claude\claude_desktop_config.json
   ```

   **ODER** falls dort bereits eine `claude_desktop_config.json` existiert:
   - Öffnen Sie die existierende Datei
   - Fügen Sie den Firecrawl Server zu den bestehenden `mcpServers` hinzu:

   ```json
   {
     "mcpServers": {
       "firecrawl": {
         "command": "node",
         "args": [
           "I:\\Ai Claude\\Markus Müller\\firecrawl-mcp\\dist\\index.js"
         ],
         "env": {
           "FIRECRAWL_API_KEY": "fc-d21288c226fd43bba3a8ca4418996218"
         }
       }
     }
   }
   ```

5. **Starten Sie Claude Desktop neu**

6. **Testen Sie den Server:**
   - Öffnen Sie Claude Desktop
   - Geben Sie ein: "Welche MCP Tools habe ich verfügbar?"
   - Sie sollten sehen: `scrape_url`, `crawl_website`, `map_website`

## 🎯 Verwendung

Nach erfolgreicher Installation können Sie sofort loslegen:

```
Scrape bitte diese Website: https://example.com
```

Claude wird dann die Firecrawl-Tools nutzen, um die Website zu analysieren und kann sie danach 1:1 für Sie nachbauen!

## 🔧 Troubleshooting

**Problem:** Claude erkennt die Tools nicht
- **Lösung:** Stellen Sie sicher, dass Claude Desktop komplett geschlossen und neu gestartet wurde

**Problem:** Server startet nicht
- **Lösung:** Führen Sie nochmal aus:
  ```bash
  cd "I:\Ai Claude\Markus Müller\firecrawl-mcp"
  npm run build
  ```

**Problem:** API-Fehler
- **Lösung:** Überprüfen Sie Ihren Firecrawl API-Key in der `.env` Datei

## 📞 Support

Bei Problemen können Sie:
1. Die `dist/index.js` Datei manuell ausführen und nach Fehlern suchen:
   ```bash
   node "I:\Ai Claude\Markus Müller\firecrawl-mcp\dist\index.js"
   ```
2. Die Logs von Claude Desktop prüfen
