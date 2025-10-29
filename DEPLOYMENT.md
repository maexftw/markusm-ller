# Deployment Anleitung: Markus Müller Website

## 🚀 Option 1: GitHub Pages (Empfohlen)

### Automatische Aktivierung

1. **Gehe zu deinem GitHub Repository:**
   - https://github.com/maexftw/markusm-ller

2. **Aktiviere GitHub Pages:**
   - Klicke auf "Settings" (oben rechts)
   - Scrolle runter zu "Pages" (linke Sidebar)
   - Unter "Source" wähle: **Branch: master** und **Folder: / (root)**
   - Klicke "Save"

3. **Deine Website ist live unter:**
   - https://maexftw.github.io/markusm-ller/
   - Alternative URL wird dir in den Settings angezeigt

4. **Hauptseite festlegen:**
   - Die `index.html` wird automatisch als Startseite verwendet
   - Für die neueste Version: Benenne `.superdesign/design_iterations/markus_mueller_3.html` um

### Aktuellen Stand deployen

Da die neueste Version in `.superdesign/design_iterations/markus_mueller_3.html` liegt, sollten wir sie als Hauptseite einrichten:

```bash
# Option A: markus_mueller_3.html als index.html kopieren
cp .superdesign/design_iterations/markus_mueller_3.html index.html

# Git commit und push
git add index.html
git commit -m "Update: Deploy markus_mueller_3 as main page

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"

git push origin master
```

**⚠️ Wichtig:** GitHub Pages kann keine Dateien in Ordnern mit `.` am Anfang (wie `.superdesign/`) anzeigen!

---

## 🚀 Option 2: Netlify (Mehr Features)

### Vorteile von Netlify:
- Custom Domain ohne Zusatzkosten
- Automatische HTTPS
- Redirects & Headers
- Form Handling
- Schnelleres CDN

### Setup Schritte:

1. **Gehe zu [netlify.com](https://netlify.com)**
   - Login mit GitHub Account

2. **Neues Site erstellen:**
   - Klicke "Add new site" → "Import an existing project"
   - Wähle GitHub → Repository `markusm-ller` auswählen

3. **Build Settings:**
   - **Branch:** `master`
   - **Publish directory:** `/` (oder den Ordner mit der fertigen HTML)
   - **Build command:** Leer lassen (keine Build Steps nötig)

4. **Deploy:**
   - Klicke "Deploy site"
   - Netlify gibt dir eine URL: `https://random-name-12345.netlify.app`

5. **Custom Domain (Optional):**
   - Site Settings → Domain Management → Add custom domain
   - Folge den DNS-Anweisungen

---

## 📂 Projekt-Struktur für Deployment

### Aktuell (nicht optimal für Deployment):
```
Markus Müller/
├── index.html                      # Alte Version
├── .superdesign/
│   └── design_iterations/
│       ├── markus_mueller_1.html
│       ├── markus_mueller_2.html
│       └── markus_mueller_3.html   # ← Neueste Version (versteckt!)
├── images/
└── css/
```

### Empfohlene Struktur:
```
Markus Müller/
├── index.html                      # ← markus_mueller_3.html als Hauptseite
├── .superdesign/                   # Backup (wird nicht deployed)
├── images/                         # Verfügbar unter /images/
└── css/                            # Verfügbar unter /css/
```

---

## 🔄 Workflow für Updates

### Schritt 1: Lokale Änderungen
Arbeite normal in `.superdesign/design_iterations/`:
```bash
# Bearbeite: markus_mueller_3.html
```

### Schritt 2: Zur Hauptseite kopieren
```bash
# Kopiere die neueste Version
cp .superdesign/design_iterations/markus_mueller_3.html index.html

# Überprüfe Bild-Pfade (müssen relativ zu / sein)
# Beispiel: Ändere .superdesign/design_iterations/images/logo.png
#           zu: images/logo.png
```

### Schritt 3: Commit & Push
```bash
# Repository überprüfen (sehr wichtig!)
git remote -v
# Muss zeigen: origin https://github.com/maexftw/markusm-ller.git

# Änderungen committen
git add index.html
git commit -m "Update: Neue Version deployed

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"

# Pushen
git push origin master
```

### Schritt 4: Warten & Testen
- **GitHub Pages:** 1-2 Minuten
- **Netlify:** 30-60 Sekunden

Teste deine Website mit Hard Refresh (Ctrl+Shift+R)

---

## ⚠️ Wichtige Hinweise

### Bild-Pfade anpassen
Wenn `markus_mueller_3.html` Bilder aus `.superdesign/design_iterations/images/` lädt:

```html
<!-- ❌ FALSCH (funktioniert nicht deployed) -->
<img src=".superdesign/design_iterations/images/logo.png">

<!-- ✅ RICHTIG (funktioniert deployed) -->
<img src="images/logo.png">
```

### CSS/JS Pfade
```html
<!-- ❌ FALSCH -->
<link rel="stylesheet" href=".superdesign/design_iterations/theme.css">

<!-- ✅ RICHTIG -->
<link rel="stylesheet" href="css/theme.css">
```

---

## 🧪 Schnell-Test

Nach dem Deployment teste:

- [ ] Hauptseite lädt: `https://deine-url.com/`
- [ ] Alle Bilder werden angezeigt
- [ ] Navigation funktioniert
- [ ] Mobile Ansicht funktioniert
- [ ] Kontaktformular (falls vorhanden)
- [ ] Alle Links funktionieren

---

## 📞 URLs

- **GitHub Repository:** https://github.com/maexftw/markusm-ller
- **GitHub Pages (nach Aktivierung):** https://maexftw.github.io/markusm-ller/
- **Netlify (falls eingerichtet):** https://[dein-site-name].netlify.app

---

## 🆘 Häufige Probleme

### Problem: Bilder werden nicht angezeigt
**Lösung:** Überprüfe Pfade in der HTML - keine `.superdesign/` Referenzen

### Problem: GitHub Pages zeigt alte Version
**Lösung:**
1. Hard Refresh (Ctrl+Shift+R)
2. Warte 5 Minuten
3. Inkognito-Fenster testen

### Problem: 404 Fehler
**Lösung:** Stelle sicher dass `index.html` im Root-Verzeichnis liegt

---

**Erstellt:** 2025-10-29
**Für Projekt:** Markus Müller Website
**Empfohlene Option:** GitHub Pages für einfache Websites, Netlify für mehr Features
