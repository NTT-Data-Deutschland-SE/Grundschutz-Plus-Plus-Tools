#!/usr/bin/env python3
"""Erzeugt die Ground-Truth-Dateien fuer das BSI-Beispiel RECPLAST aus dem PDF.

Quelle: "Beschreibung_Recplast.pdf" (BSI, Version 1.0, 2020, 69 Seiten,
SHA-256 e1a0b67810aa85b2cd2f8d3cfe911aaa19b094f65babf6d486b149d00ac03a9f).
Das PDF liegt nicht im Repo (BSI-Veroeffentlichung); Pfad als Argument.

Nur fuer die Entwicklung (Plan E5): RECPLAST ist Regressionsfixture des
SSP-Generators, kein Optimierungsziel. Tabellen mit klarer Zeilenstruktur
(Grundschutz-Check 21-23, Risikobewertung 28/29, Risikobehandlung 30) werden
aus dem PDF-Text geparst; Strukturanalyse-Namen und Schutzbedarfswerte sind
transkribiert, weil die Tabellenzellen im PDF ueber mehrere Zeilen umbrechen.

Aufruf:  python build_gold.py <Beschreibung_Recplast.pdf>
Ausgabe: zielobjekte.csv, schutzbedarf.csv, grundschutz_check.csv,
         risiken.csv, risikobehandlung.csv, realisierungsplan.csv,
         prozess_anwendungen.csv, rollen.csv (alle neben diesem Skript)
"""
import csv, hashlib, re, sys, pathlib

HERE = pathlib.Path(__file__).resolve().parent
PDF_SHA256 = "e1a0b67810aa85b2cd2f8d3cfe911aaa19b094f65babf6d486b149d00ac03a9f"

# --- Strukturanalyse (Tabelle 2, 3, 5-7, 10-12, 14) -------------------------
# (id, name, typ, tabelle, seite)
ZIELOBJEKTE = [
    # Geschaeftsprozesse, Tabelle 2 (S. 15-18); a-d sind Teilprozesse
    ("GP001", "Produktion", "geschaeftsprozess", 2, 15),
    ("GP002", "Angebotswesen", "geschaeftsprozess", 2, 16),
    ("GP003", "Auftragsabwicklung", "geschaeftsprozess", 2, 16),
    ("GP004", "Einkauf", "geschaeftsprozess", 2, 16),
    ("GP005", "Disposition", "geschaeftsprozess", 2, 16),
    ("GP006", "Personalverwaltung", "geschaeftsprozess", 2, 17),
    ("GP006a", "Gehaltszahlung", "teilprozess", 2, 17),
    ("GP006b", "Neueinstellung", "teilprozess", 2, 17),
    ("GP006c", "Entlassung Mitarbeiter", "teilprozess", 2, 15),
    ("GP007", "IT-Betrieb", "geschaeftsprozess", 2, 17),
    ("GP007a", "Betrieb Server", "teilprozess", 2, 17),
    ("GP007b", "Betrieb Clients", "teilprozess", 2, 17),
    ("GP007c", "Betrieb Netze", "teilprozess", 2, 18),
    ("GP007d", "Betrieb Produktions-IT", "teilprozess", 2, 18),
    ("GP008", "Betrieb der Webseite", "geschaeftsprozess", 2, 18),
    ("GP009", "Betrieb des Intranets", "geschaeftsprozess", 2, 18),
    ("GP010", "Verwaltung des Mobile Device Managements", "geschaeftsprozess", 2, 18),
    ("GP011", "Nutzung einer Cloud-Umgebung", "geschaeftsprozess", 2, 18),
    # Anwendungen, Tabelle 3 (S. 19-23)
    ("A001", "Textverarbeitung, Präsentation, Tabellenkalkulation", "anwendung", 3, 19),
    ("A002", "E-Mail-Client", "anwendung", 3, 19),
    ("A003", "Web-Browser", "anwendung", 3, 19),
    ("A004", "Prozessleitsystem", "anwendung", 3, 19),
    ("A005", "Entwicklungssystem", "anwendung", 3, 19),
    ("A006", "Personaldatenverarbeitung", "anwendung", 3, 19),
    ("A007", "Reisekostenabrechnung", "anwendung", 3, 19),
    ("A008", "Finanzbuchhaltung", "anwendung", 3, 20),
    ("A009", "Auftrags- und Kundenverwaltung", "anwendung", 3, 20),
    ("A010", "Active Directory", "anwendung", 3, 20),
    ("A011", "Systemmanagement", "anwendung", 3, 20),
    ("A012", "Zentrale Dokumentenverwaltung", "anwendung", 3, 20),
    ("A013", "Druckservice Bad Godesberg", "anwendung", 3, 20),
    ("A014", "Druckservice Beuel", "anwendung", 3, 21),
    ("A015", "Firewall", "anwendung", 3, 21),
    ("A016", "Steuerung der Produktionsanlagen", "anwendung", 3, 21),
    ("A017", "Content Management System", "anwendung", 3, 21),
    ("A018", "Backupsoftware", "anwendung", 3, 21),
    ("A019", "Webserver", "anwendung", 3, 21),
    ("A020", "Datenbanksystem", "anwendung", 3, 21),
    ("A021", "Internes Ticketsystem", "anwendung", 3, 21),
    ("A022", "Internes Wiki", "anwendung", 3, 22),
    ("A023", "Virtualisierungssoftware", "anwendung", 3, 22),
    ("A024", "Voice over IP", "anwendung", 3, 22),
    ("A025", "Chat-Anwendung", "anwendung", 3, 22),
    ("A026", "Mobile Device Management", "anwendung", 3, 22),
    ("A027", "ReCoBS", "anwendung", 3, 22),
    ("A028", "Updateverwaltung Windows", "anwendung", 3, 22),
    ("A029", "Updateverwaltung Linux", "anwendung", 3, 22),
    ("A030", "Cloud-APP", "anwendung", 3, 22),
    ("A031", "Cloud-Umgebung", "anwendung", 3, 23),
    ("A032", "CAD/CAM", "anwendung", 3, 23),
    # IT-Systeme, Tabelle 5 (S. 28-31)
    ("C001", "Clients der Finanzbuchhaltung", "client", 5, 28),
    ("C002", "Clients der Geschäftsführung", "client", 5, 28),
    ("C003", "Clients der Personalabteilung", "client", 5, 28),
    ("C004", "Clients der Informationstechnik", "client", 5, 28),
    ("C005", "Clients des Marketings & Vertrieb", "client", 5, 28),
    ("C006", "Clients der Fertigung und Lager", "client", 5, 28),
    ("C007", "Clients der Entwicklungsabteilung", "client", 5, 28),
    ("C008", "Clients der Einkaufsabteilung", "client", 5, 28),
    ("C009", "Clients in den Vertriebsbüros", "client", 5, 28),
    ("L001", "Laptops der Finanzbuchhaltung", "laptop", 5, 28),
    ("L002", "Laptops der Geschäftsführung", "laptop", 5, 28),
    ("L003", "Laptops der Personalabteilung", "laptop", 5, 29),
    ("L004", "Laptops der Informationstechnik", "laptop", 5, 29),
    ("L005", "Laptops Marketing & Vertrieb", "laptop", 5, 29),
    ("L006", "Laptops von Fertigung und Lager", "laptop", 5, 29),
    ("L007", "Laptops der Entwicklungsabteilung", "laptop", 5, 29),
    ("L008", "Laptops der Einkaufsabteilung", "laptop", 5, 29),
    ("L009", "Laptops in den Vertriebsbüros", "laptop", 5, 29),
    ("S001", "Domänen-Controller", "server", 5, 29),
    ("S002", "Dateiserver", "server", 5, 29),
    ("S003", "Druckserver", "server", 5, 29),
    ("S004", "Kommunikationsserver", "server", 5, 30),
    ("S005", "DB-Server der Kunden- und Auftragsbearbeitung", "server", 5, 30),
    ("S006", "DB-Server der Finanzbuchhaltung", "server", 5, 30),
    ("S007", "Virtualisierungsserver", "server", 5, 30),
    ("S008", "Server für Produktionssteuerung", "server", 5, 30),
    ("S009", "Wiki-Server", "server", 5, 30),
    ("S010", "Virtualisierungsserver2", "server", 5, 30),
    ("S011", "Ticketsystem", "server", 5, 30),
    ("S012", "Backupserver", "server", 5, 30),
    ("S013", "Windows-Update-Server", "server", 5, 30),
    ("S014", "Linux-Update-Server", "server", 5, 30),
    ("S015", "DB-Server fürs Systemmanagement", "server", 5, 31),
    # ICS, Tabelle 6 (S. 31)
    ("I001", "Speicherprogrammierbare Produktionsmaschinen", "ics", 6, 31),
    ("I002", "SCADA", "ics", 6, 31),
    ("I003", "Server für die Betriebsdatenerfassung", "ics", 6, 31),
    # IoT, Tabelle 7 (S. 31)
    ("O001", "Video-Überwachung", "iot", 7, 31),
    ("O002", "Kühlschrank", "iot", 7, 31),
    ("O003", "Alarmanlage", "iot", 7, 31),
    ("O004", "Kaffeevollautomat", "iot", 7, 31),
    ("O005", "Sprachassistent", "iot", 7, 31),
    # Netz- und TK-Komponenten, Tabelle 10 (S. 34-35)
    ("N001", "Router zum Internet", "netzkomponente", 10, 34),
    ("N002", "Firewall", "netzkomponente", 10, 34),
    ("N003", "Zentrale Switche in Bad Godesberg und Beuel", "netzkomponente", 10, 34),
    ("N004", "Router zur Verbindung der Standorte BG und BE", "netzkomponente", 10, 34),
    ("N005", "ReCoBS", "netzkomponente", 10, 34),
    ("N006", "Switche in den Vertriebsbüros", "netzkomponente", 10, 34),
    ("N007", "Router zum Internet der Vertriebsbüros", "netzkomponente", 10, 34),
    ("N008", "WLAN-Access-Points", "netzkomponente", 10, 35),
    ("T001", "Telefonanlagen Bad Godesberg und Beuel", "tk-komponente", 10, 35),
    ("T002", "Faxgeräte", "tk-komponente", 10, 35),
    # Kommunikationsverbindungen, Tabelle 11 (S. 35)
    ("K001", "Internetanschluss BG", "kommunikationsverbindung", 11, 35),
    ("K002", "Standleitung Bad Godesberg – Beuel", "kommunikationsverbindung", 11, 35),
    ("K003", "Verbindungen zwischen Netzkomponenten innerhalb der RECPLAST GmbH", "kommunikationsverbindung", 11, 35),
    ("K004", "Verbindungen zwischen Switches und Servern", "kommunikationsverbindung", 11, 35),
    ("K005", "Verbindungen zwischen Switches und Clients", "kommunikationsverbindung", 11, 35),
    ("K006", "Verbindungen zwischen Switches und Produktionsmaschinen", "kommunikationsverbindung", 11, 35),
    ("K007", "Internetanschlüsse der Vertriebsbüros", "kommunikationsverbindung", 11, 35),
    ("K008", "Mobile Internetanschlüsse der Laptops", "kommunikationsverbindung", 11, 35),
    # Gebaeude und Raeume, Tabelle 12 (S. 36-37)
    ("GB001", "Verwaltungsgebäude Bad Godesberg", "gebaeude", 12, 36),
    ("GB002", "Produktionsgebäude Beuel", "gebaeude", 12, 36),
    ("R001", "Technikraum Bad Godesberg", "raum", 12, 36),
    ("R002", "Serverraum Bad Godesberg", "raum", 12, 36),
    ("R003", "Büros IT-Abteilung", "raum", 12, 36),
    ("R009", "Serverraum Beuel", "raum", 12, 36),
    ("R010", "Technikraum Beuel", "raum", 12, 36),
    ("R011", "Büros Fertigung/Lager", "raum", 12, 36),
    ("R012", "Büros Entwicklungsabteilung", "raum", 12, 36),
    ("R013", "Produktionshalle", "raum", 12, 36),
    ("R014", "Vertriebsbüros", "raum", 12, 36),
    ("R018", "Technikraum Vertriebsbüros", "raum", 12, 36),
    ("R019", "Datenträgerarchiv", "raum", 12, 37),
]

# --- Schutzbedarf (Tabelle 15-19, S. 40-50; S. 60) ---------------------------
# Werte je Grundwert wie im PDF: normal | hoch | sehr hoch.
# Quelle "S60": Aufzaehlung der Zielobjekte fuer die Risikoanalyse (Kap. 9.2),
# dort nur "hoch" ohne Grundwert-Tabelle.
SCHUTZBEDARF = [
    ("GP001", "hoch", "hoch", "sehr hoch", 15, 40),
    ("GP002", "hoch", "hoch", "normal", 15, 41),
    ("GP003", "hoch", "hoch", "hoch", 15, 41),
    ("GP004", "hoch", "normal", "normal", 15, 41),
    ("GP005", "normal", "hoch", "hoch", 15, 41),
    ("GP010", "hoch", "hoch", "hoch", 15, 42),
    ("A002", "hoch", "hoch", "hoch", "S60", 60),
    ("A005", "hoch", "hoch", "hoch", 16, 43),
    ("A010", "hoch", "hoch", "sehr hoch", 16, 43),
    ("A011", "hoch", "hoch", "sehr hoch", 16, 43),
    ("A027", "hoch", "hoch", "normal", 16, 44),
    ("C001", "hoch", "hoch", "normal", 17, 45),
    ("C002", "hoch", "hoch", "", "S60", 60),
    ("C003", "hoch", "hoch", "", "S60", 60),
    ("C004", "hoch", "hoch", "", "S60", 60),
    ("C005", "hoch", "hoch", "", "S60", 60),
    ("C006", "hoch", "hoch", "", "S60", 60),
    ("C007", "hoch", "hoch", "", "S60", 60),
    ("C008", "hoch", "hoch", "", "S60", 60),
    ("C009", "hoch", "hoch", "", "S60", 60),
    ("L003", "hoch", "hoch", "normal", 17, 45),
    ("N001", "hoch", "hoch", "sehr hoch", 17, 45),
    ("S001", "hoch", "hoch", "normal", 17, 46),
    ("S007", "hoch", "hoch", "hoch", "S60", 60),
    ("T001", "hoch", "hoch", "normal", 17, 46),
    ("K001", "sehr hoch", "hoch", "sehr hoch", 18, 47),
    ("K002", "sehr hoch", "hoch", "sehr hoch", 18, 48),
    ("K006", "hoch", "hoch", "sehr hoch", 18, 48),
    ("GB001", "sehr hoch", "sehr hoch", "sehr hoch", 19, 49),
    ("R003", "hoch", "hoch", "normal", 19, 49),
    ("R009", "sehr hoch", "hoch", "sehr hoch", 19, 50),
]

# --- Zuordnung Geschaeftsprozess -> Anwendungen (Tabelle 4, S. 23-25) ---------
PROZESS_ANWENDUNGEN = {
    "GP001": ["A001", "A004", "A005", "A009", "A010", "A012", "A014", "A016", "A027", "A032"],
    "GP002": ["A001", "A002", "A003", "A009", "A010", "A012", "A013", "A020", "A027", "A024"],
    "GP003": ["A001", "A002", "A008", "A009", "A010", "A012", "A013", "A020", "A024"],
    "GP004": ["A001", "A002", "A003", "A008", "A010", "A012", "A013", "A024", "A027"],
    "GP005": ["A001", "A002", "A003", "A008", "A009", "A010", "A012", "A013", "A014", "A020", "A024", "A027"],
}

# --- Rollen und Verantwortliche, die das PDF nennt ---------------------------
ROLLEN = [
    "Geschäftsführung", "Informationssicherheitsbeauftragter", "ISB", "ICS-Informationssicherheitsbeauftragter",
    "ICS-ISB", "IS-Management-Team", "IS-Organisation", "IT-Abteilung", "Informationstechnik", "Zentrale IT",
    "Updateverwaltung", "Einkaufsabteilung", "Personalabteilung", "Abteilungsleiter", "Mitarbeiter",
    "Anwendungsverantwortliche", "Eigentümer", "Prozesseigentümer", "Systemeigentümer", "Informationseigentümer",
    "Projektgruppe", "Betriebsrat", "Vertrieb", "Produktion", "Telfcom", "Indust GmbH & Co.KG", "VPN Ware GmbH",
    "GetMobileDevice GmbH",
]

# --- Realisierungsplan (Tabelle 31, S. 69) -----------------------------------
REALISIERUNGSPLAN = [
    ("C001-C009", "SYS.2.1.A12", "Der Beschaffungsprozess wird von der Einkaufsabteilung überarbeitet und vervollständigt."),
    ("C001-C009", "SYS.2.1.A17", "Es wird ein Freigabeprozess definiert und eingesetzt."),
    ("C001-C009", "SYS.2.1.A21", "Die Funktion wird für alle Mitarbeiter des Vertriebs aktiviert."),
    ("C001-C009", "SYS.2.1.A37", "Es wird eine Zwei-Faktor-Authentisierung angeschafft."),
    ("C001-C009", "SYS.2.2.3.A4", "Nach erfolgreicher Prüfung wird über das Deaktivieren der Einstellungen entschieden."),
    ("GB001;GB002", "INF.4.A5", "Es wird bezüglich der Nutzung des Protokolls sensibilisiert."),
    ("GB001;GB002", "INF.4.A7", "Die IT-Verkabelungen werden auf nicht mehr benötigte Kabel überprüft."),
    ("N002", "NET.3.2.A16", "Es wird eine P-A-P-Netzstruktur aufgebaut."),
    ("N002", "NET.3.2.A26", "Beim Erreichen des End of Life-Cycles wird eine neue dedizierte Firewall angeschafft."),
    ("N002", "NET.3.2.A29", "Es soll eine weitere Firewall beschafft werden."),
]

# Elementare Gefaehrdungen (Titel laut IT-Grundschutz-Kompendium), weil die
# Titel in den Tabellen 28-30 ueber Zeilen umbrechen und im Textfluss hinter
# den Werten landen.
GEFAEHRDUNGEN = {
    1: "Feuer", 2: "Ungünstige klimatische Bedingungen", 3: "Wasser", 4: "Verschmutzung, Staub, Korrosion",
    5: "Naturkatastrophen", 6: "Katastrophen im Umfeld", 7: "Großereignisse im Umfeld",
    8: "Ausfall oder Störung der Stromversorgung", 9: "Ausfall oder Störung von Kommunikationsnetzen",
    10: "Ausfall oder Störung von Versorgungsnetzen", 11: "Ausfall oder Störung von Dienstleistern",
    12: "Elektromagnetische Störstrahlung", 13: "Abfangen kompromittierender Strahlung",
    14: "Ausspähen von Informationen (Spionage)", 15: "Abhören", 16: "Diebstahl von Geräten, Datenträgern oder Dokumenten",
    17: "Verlust von Geräten, Datenträgern oder Dokumenten", 18: "Fehlplanung oder fehlende Anpassung",
    19: "Offenlegung schützenswerter Informationen", 20: "Informationen oder Produkte aus unzuverlässiger Quelle",
    21: "Manipulation von Hard- oder Software", 22: "Manipulation von Informationen", 23: "Unbefugtes Eindringen in IT-Systeme",
    24: "Zerstörung von Geräten oder Datenträgern", 25: "Ausfall von Geräten oder Systemen", 26: "Fehlfunktion von Geräten oder Systemen",
    27: "Ressourcenmangel", 28: "Software-Schwachstellen oder -Fehler", 29: "Verstoß gegen Gesetze oder Regelungen",
    30: "Unberechtigte Nutzung oder Administration von Geräten und Systemen",
    31: "Fehlerhafte Nutzung oder Administration von Geräten und Systemen", 32: "Missbrauch von Berechtigungen",
    33: "Personalausfall", 34: "Anschlag", 35: "Nötigung, Erpressung oder Korruption", 36: "Identitätsdiebstahl",
    37: "Abstreiten von Handlungen", 38: "Missbrauch personenbezogener Daten", 39: "Schadprogramme",
    40: "Verhinderung von Diensten (Denial of Service)", 41: "Sabotage", 42: "Social Engineering",
    43: "Einspielen von Nachrichten", 44: "Unbefugtes Eindringen in Räumlichkeiten", 45: "Datenverlust",
    46: "Integritätsverlust schützenswerter Informationen", 47: "Schädliche Seiteneffekte IT-gestützter Angriffe",
}

STATUS_MAP = {"Ja": "implemented", "Teilweise": "partial", "Entbehrlich": "not-applicable"}
ZIELOBJEKT_CHECK = {"ISMS.1": "Informationsverbund", "APP.1.1": "A001", "SYS.2.2.3": "C001"}


def page_texts(pdf_path):
    import pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        return {i + 1: (p.extract_text(layout=True) or "") for i, p in enumerate(pdf.pages)}


def parse_check(pages):
    """Tabelle 21-23: erste Zeile einer Anforderung traegt ID ... Status."""
    rows = []
    rx = re.compile(r"^\s*((?:ISMS\.1|APP\.1\.1|SYS\.2\.2\.3)\.A\d+)\b.*?\b(Ja|Teilweise|Entbehrlich)\b")
    for n in range(54, 60):
        for line in pages[n].splitlines():
            m = rx.match(line)
            if m:
                aid = m.group(1)
                baustein = aid.rsplit(".A", 1)[0]
                rows.append((aid, ZIELOBJEKT_CHECK[baustein], m.group(2), STATUS_MAP[m.group(2)], n))
    return rows


def parse_risk_table(pages, page_range, zielobjekt, tabelle):
    """Tabelle 28/29: 'G 0.x Titel ... haeufigkeit auswirkung risiko', Titel umbricht.
    Seite 64 traegt das Ende von Tabelle 28 und den Anfang von Tabelle 29; der
    Marker 'Tabelle 28: Risikobewertung' trennt beide."""
    marker = "Tabelle 28: Risikobewertung"
    chunks = []
    for n in page_range:
        t = pages[n]
        if marker in t:
            before, after = t.split(marker, 1)
            t = before if tabelle == 28 else after
        chunks.append(t)
    text = "\n".join(chunks)
    text = re.sub(r"\n\s*Seite \d+ von 69\s+Version 1\.0\s*", "\n", text)
    text = re.sub(r"\n\s*Gefährdung\s+Eintrittshäufigkeit\s+Auswirkungen\s+Risiko\s*", "\n", text)
    flat = re.sub(r"\s+", " ", text)
    rx = re.compile(r"G\s*0\.(\d+)\s+(.+?)\s+(selten|mittel|häufig|sehr häufig)\s+(vernachlässigbar|begrenzt|beträchtlich|existenzbedrohend)\s+(gering|mittel|hoch|sehr hoch)\b", re.I)
    rows = []
    for m in rx.finditer(flat):
        nr = int(m.group(1))
        rows.append((zielobjekt, f"G 0.{nr}", GEFAEHRDUNGEN[nr], m.group(3).lower(), m.group(4).lower(), m.group(5).lower(), tabelle))
    return rows


def strip_title_words(text, title):
    """Entfernt fuehrende Woerter, die zum umgebrochenen Gefaehrdungstitel gehoeren."""
    words = set(re.findall(r"[\wäöüÄÖÜß-]+", title))
    tokens = text.split()
    while tokens and tokens[0].strip(",.()") in words:
        tokens.pop(0)
    return " ".join(tokens)


def parse_treatment(pages):
    """Tabelle 30 (S. 67-68): Gefaehrdung -> Risikoreduktion/Risikoakzeptanz + Massnahme."""
    text = "\n".join(pages[n] for n in (67, 68))
    text = re.sub(r"\n\s*Seite \d+ von 69\s+Version 1\.0\s*", "\n", text)
    text = re.sub(r"\n\s*Gefährdung\s+Risikobehandlungsoption\s*", "\n", text)
    flat = re.sub(r"\s+", " ", text)
    parts = re.split(r"(?=G 0\.\d+ )", flat)
    rows = []
    for part in parts:
        m = re.match(r"G 0\.(\d+) (.*?)(Risikoreduktion|Risikoakzeptanz):\s*(.*)", part)
        if not m:
            continue
        nr = int(m.group(1))
        rest = re.sub(r"Tabelle 30: Risikobehandlung.*$", "", m.group(4)).strip()
        rest = strip_title_words(rest, GEFAEHRDUNGEN[nr])
        rows.append(("S007", f"G 0.{nr}", GEFAEHRDUNGEN[nr], m.group(3), rest))
    return rows


def write(name, header, rows):
    with open(HERE / name, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(header)
        w.writerows(rows)
    print(f"{name}: {len(rows)} Zeilen")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    pdf = pathlib.Path(sys.argv[1])
    digest = hashlib.sha256(pdf.read_bytes()).hexdigest()
    if digest != PDF_SHA256:
        sys.exit(f"SHA-256 des PDF weicht ab: {digest}")
    pages = page_texts(pdf)

    write("zielobjekte.csv", ["id", "name", "typ", "tabelle", "seite"], ZIELOBJEKTE)
    def gspp(v, i, a):
        return "erhöht" if any(x in ("hoch", "sehr hoch") for x in (v, i, a)) else "normal-SdT"
    write("schutzbedarf.csv", ["id", "vertraulichkeit", "integritaet", "verfuegbarkeit", "gspp_sicherheitsniveau", "tabelle", "seite"],
          [(i, v, n, a, gspp(v, n, a), t, s) for (i, v, n, a, t, s) in SCHUTZBEDARF])
    check = parse_check(pages)
    assert len(check) == 49, f"Grundschutz-Check: {len(check)} statt 49 Anforderungen geparst"
    write("grundschutz_check.csv", ["anforderung", "zielobjekt", "status_pdf", "status_oscal", "seite"], check)
    r28 = parse_risk_table(pages, (63, 64), "S007", 28)
    r29 = parse_risk_table(pages, (64, 65, 66), "GP001", 29)
    assert len(r28) == 25, f"Tabelle 28: {len(r28)} statt 25"
    assert len(r29) == 45, f"Tabelle 29: {len(r29)} statt 45"
    write("risiken.csv", ["zielobjekt", "gefaehrdung", "titel", "haeufigkeit", "auswirkung", "risiko", "tabelle"], r28 + r29)
    treat = parse_treatment(pages)
    assert len(treat) == 25, f"Tabelle 30: {len(treat)} statt 25"
    write("risikobehandlung.csv", ["zielobjekt", "gefaehrdung", "titel", "option", "massnahme"], treat)
    write("realisierungsplan.csv", ["zielobjekt", "anforderung", "massnahme"], REALISIERUNGSPLAN)
    write("prozess_anwendungen.csv", ["geschaeftsprozess", "anwendung"],
          [(gp, a) for gp, apps in PROZESS_ANWENDUNGEN.items() for a in apps])
    write("rollen.csv", ["rolle"], [(r,) for r in ROLLEN])


if __name__ == "__main__":
    main()
