#!/bin/bash

# Dieses Skript generiert eine Statistik-Tabelle durch das Kombinieren
# einer JSON-Datei (UUID -> Array) und einer CSV-Datei (UUID -> Name).
#
# Es verwendet 'jq' zur JSON-Verarbeitung und 'awk' zur CSV-Verarbeitung.
# Es bereinigt die CSV-Datei von \r-Zeichen, um Fehler zu vermeiden.
#
# Verwendung: ./stats_v2.sh <json_datei> <csv_datei>
# Beispiel:   ./stats_v2.sh controls_map.json zielobjekte.csv

# --- Validierung ---

# 1. Prüfen, ob zwei Dateinamen als Argumente übergeben wurden
if [ $# -ne 2 ]; then
  echo "Fehler: Bitte gib die JSON-Datei und die CSV-Datei als Argumente an."
  echo "Verwendung: $0 <json_datei> <csv_datei>"
  exit 1
fi

JSON_FILE="$1"
CSV_FILE="$2"

# 2. Prüfen, ob die Dateien existieren
if [ ! -f "$JSON_FILE" ]; then
  echo "Fehler: Die JSON-Datei '$JSON_FILE' wurde nicht gefunden."
  exit 1
fi
if [ ! -f "$CSV_FILE" ]; then
  echo "Fehler: Die CSV-Datei '$CSV_FILE' wurde nicht gefunden."
  exit 1
fi

# 3. Prüfen, ob 'jq', 'awk', 'tr', 'cat' und 'mktemp' installiert sind
if ! command -v jq &> /dev/null; then
  echo "Fehler: 'jq' ist nicht installiert. (z.B. sudo apt install jq)"
  exit 1
fi
if ! command -v awk &> /dev/null; then
  echo "Fehler: 'awk' ist nicht installiert."
  exit 1
fi
if ! command -v tr &> /dev/null || ! command -v cat &> /dev/null || ! command -v mktemp &> /dev/null; then
  echo "Fehler: Core-Utils (tr, cat, mktemp) nicht gefunden."
  exit 1
fi

# --- Verarbeitung ---

# 1. Header-Zeile drucken
echo "| Name | UUID | Anzahl |"
echo "| --- | --- | --- |" # Markdown Tabellen-Trennlinie

# 2. [NEUE LOGIK] CSV-Datei bereinigen
#    Wir erstellen eine temporäre Kopie der CSV-Datei und entfernen alle
#    Carriage-Return-Zeichen (\r), die oft den String-Vergleich in 'awk' stören.
CLEAN_CSV=$(mktemp)
cat "$CSV_FILE" | tr -d '\r' | sed 's/"[^"]*"//g' > "$CLEAN_CSV"

# 3. Prozess-Substitution (wie in v5) kombiniert mit 'awk'-Logik (wie in v3)
#    Lese von jq
while read -r uuid count; do
  
  # Suche den Namen mit 'awk' in der BEREINIGTEN CSV-Datei.
  # Die UUID steht in der letzten Spalte ($NF): das BSI fügt Spalten ein
  # (2026-10-01: "Beispiel" als Spalte 3), eine feste Spaltennummer verrutscht dann.
  name=$(awk -F, -v id="$uuid" '
    NR > 1 {
      uuid_col = $NF;
      
      # Nur noch verbleibende Leerzeichen am Anfang/Ende entfernen
      sub(/^[[:space:]]+/, "", uuid_col);
      sub(/[[:space:]]+$/, "", uuid_col);
      
      if (uuid_col == id) {
        print $1
      }
    }' "$CLEAN_CSV") # Lese von der bereinigten Temp-Datei
  
  if [ -z "$name" ]; then
    # Fallback, falls die UUID in der CSV nicht gefunden wurde
    name="<Nicht gefunden>"
  fi
  
  # Drucke die finale Tabellenzeile
  echo "| $name | $uuid | $count |"

done < <(jq -r '.zielobjekt_controls_map | keys_unsorted[] as $uuid | "\($uuid) \(.[$uuid] | length)"' "$JSON_FILE")

# 4. Temporäre Datei löschen
rm "$CLEAN_CSV"