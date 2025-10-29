# Firecrawl MCP Server

Ein Model Context Protocol (MCP) Server für die Integration von Firecrawl in Claude Desktop.

## Features

- **scrape_url**: Scrapt eine einzelne URL und gibt den Inhalt als Markdown/HTML zurück
- **crawl_website**: Crawlt mehrere Seiten einer Website
- **map_website**: Erstellt eine Map aller URLs einer Website

## Installation

1. **Dependencies installieren:**
```bash
cd "I:\Ai Claude\Markus Müller\firecrawl-mcp"
npm install
```

2. **TypeScript kompilieren:**
```bash
npm run build
```

3. **Claude Desktop konfigurieren:**

Öffnen Sie die Claude Desktop Konfiguration:
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`

Fügen Sie folgendes hinzu:

```json
{
  "mcpServers": {
    "firecrawl": {
      "command": "node",
      "args": ["I:\\Ai Claude\\Markus Müller\\firecrawl-mcp\\dist\\index.js"],
      "env": {
        "FIRECRAWL_API_KEY": "fc-d21288c226fd43bba3a8ca4418996218"
      }
    }
  }
}
```

4. **Claude Desktop neu starten**

## Verwendung

Nach der Installation können Sie in Claude Desktop folgende Befehle verwenden:

### Eine Seite scrapen (1:1 Kopie erstellen)
```
Bitte scrape diese Website: https://example.com
```

### Ganze Website crawlen
```
Crawle bitte alle Seiten von https://example.com
```

### Website-Struktur analysieren
```
Zeige mir alle URLs von https://example.com
```

## Workflow: Webseite 1:1 nachbauen

1. **Seite scrapen:**
   ```
   Scrape bitte https://ihre-ziel-website.com mit allen Details (HTML, CSS, Bilder)
   ```

2. **Design nachbauen:**
   Nach dem Scraping können Sie sagen:
   ```
   Baue diese Seite 1:1 nach mit dem gleichen Layout, Design und Funktionen
   ```

3. **Anpassungen vornehmen:**
   ```
   Ändere die Farben zu [Ihre Wünsche]
   Ersetze die Bilder mit Platzhaltern
   ```

## API Key Sicherheit

⚠️ **Wichtig**: Der API-Key ist aktuell in der `.env` Datei gespeichert. Teilen Sie diese Datei NICHT öffentlich!

## Troubleshooting

- **Server startet nicht**: Prüfen Sie, ob Node.js installiert ist (`node --version`)
- **API-Fehler**: Überprüfen Sie Ihren Firecrawl API-Key
- **Claude erkennt Tools nicht**: Starten Sie Claude Desktop neu

## Tools Übersicht

### scrape_url
Perfekt für einzelne Seiten. Gibt Markdown und HTML zurück.
- `url`: Die zu scrapende URL
- `formats`: Array mit ['markdown', 'html', 'rawHtml', 'links', 'screenshot']
- `onlyMainContent`: Nur Hauptinhalt (default: true)

### crawl_website
Für mehrere Seiten einer Website.
- `url`: Start-URL
- `maxDepth`: Maximale Crawl-Tiefe (default: 2)
- `limit`: Max. Anzahl Seiten (default: 10)

### map_website
Erstellt eine URL-Übersicht ohne Content.
- `url`: Start-URL
- `limit`: Max. URLs (default: 5000)
- `includeSubdomains`: Subdomains einbeziehen
