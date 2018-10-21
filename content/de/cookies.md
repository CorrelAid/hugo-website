---
title: "Cookies"
date: 2018-08-23T12:35:49+02:00
draft: false
translationKey: "cookies"
menu: 
    essentials:
        weight: 2
---

# Cookies


### Was sind Cookies?

Cookies sind kleine Dateien, die wir auf deinem Computer speichern. Sie sind so angelegt, dass sie eine geringe Menge an clienten- und websitenspezifischen Daten sammeln. Meistens nur ein Wort oder eine Zahl. Auf diese kann entweder vom Web Server oder vom Computer des Clients zugegriffen werden. Dadurch wird dem Server erlaubt eine auf den Benutzer zugeschnittene Seite zu gestalten; oder die Seite selbst enthält ein Skript, das auf die Daten im Cookie zugreift, womit ermöglicht wird, dass wir die Seite während deines Besuchs auf dich anpassen. Wir benutzen Cookies nur, um uns während deines Besuchs zu merken, ob du eine Leiste nicht mehr sehen willst.

```javascript
function setCookie(cname, cvalue) {
    document.cookie = cname + "=" + cvalue + ";path=/";
}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}
```

### Warum Nutzen wir Cookies?

Wir nutzen Cookies in erster Linie um Euer/Ihr Surferlebnis auf unserer Seite zu verbesern. **Alle Cookies werden nach dem du den Browser geschlossen hast wieder gelöscht.** Weder verwenden wir Cookies um dich zurückzuverfolgen, noch erlauben wir Drittanbietern Cookies auf unserer Seite zu installieren. Um vollständige Transparenz zu bieten enthält die nachfolgende Liste Informationen über alle von uns genutzten Cookies und deren Spezifikationen.

### Welche Cookies speichern wir?

Name                      | Speicherzeit | Beschreibung                     |
------------------------- | ------------ | -------------------------------- |
correlaidx-bar-hidden     | 0 Tage       | CorrelAidX Standorte zeigen      |
cookie-bar-hidden         | 0 Tage       | Cookie Information zeigen        |


