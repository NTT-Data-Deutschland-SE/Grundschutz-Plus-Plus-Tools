# Automatisiertes Rahmenwerk zur Erstellung von OSCAL-Komponentendefinitionen mittels KI-gestützter Abbildung und Anreicherung

Dieses Dokument beschreibt das technische Konzept und die Implementierungsdetails eines automatisierten Pipelinesystems zur Erstellung von OSCAL 1.2.2 Komponentendefinitionen. Das System unterstützt die Migration von BSI IT-Grundschutz Edition 2023 (Ed2023) zum modernisierten Grundschutz++ (G++). Es nutzt eine Strategie, die auf Python und Google Cloud Vertex AI (Gemini) basiert, um semantische 1:1 Abbildungen durchzuführen und die resultierenden Kontrollen mit KI-generierten Implementierungsdetails anzureichern.

## 1.0 Einleitung und strategischer Kontext

Die Weiterentwicklung vom modulbasierten IT-Grundschutz (Ed2023) zur datenzentrierten, vererbungsgesteuerten Grundschutz++ (G++) Methodik erfordert Mechanismen zur Migration bestehender Informationssicherheits-Managementsysteme (ISMS).

Dieses Rahmenwerk implementiert eine automatisierte Pipeline zur Erstellung von „Transitional Component Definitions“. Die Pipeline führt zwei Hauptaufgaben aus:

1.  **Migration (Mapping):** Abbildung eines Ed2023 **„Baustein“** auf das am nächsten entsprechende G++ **„Zielobjekt“** und anschließende 1:1 Abbildung jeder Ed2023 **„Anforderung“** auf eine G++ **„Kontrolle“**.
2.  **Anreicherung (Generation):** Generierung von detaillierten Implementierungsdetails (Maturitätsstufen 1-5) und Klassifizierungen für die G++ Kontrollen im Kontext des ursprünglichen BSI Bausteins.

## 2.0 Methodik und Einschränkungen

Die Methodik basiert auf einer Kombination aus deterministischer Datenanalyse und KI-gestützter semantischer Analyse (Google Vertex AI).

### 2.1 Die 1:1 Abbildungseinschränkung (Migration)

Für die Migrationsphasen erzwingt das Rahmenwerk eine strikte 1:1 Abbildung (N:M Beziehungen sind untersagt):

1.  **Baustein zu Zielobjekt (Stage `match_bausteine`):** Jeder relevante Ed2023 Baustein (definiert in `constants.ALLOWED_MAIN_GROUPS` und `constants.ALLOWED_PROCESS_BAUSTEINE`) wird auf genau ein G++ Zielobjekt abgebildet.
2.  **Anforderung zu Kontrolle (Stage `matching`):** Jede Ed2023 Anforderung wird auf genau eine G++ Kontrolle abgebildet.

### 2.2 Logik zur Abbildungspriorisierung und Kontextbegrenzung

Die Auswahl der entsprechenden G++ Kontrolle basiert auf einer definierten Logik, die den Kontext strikt eingrenzt:

1.  **Determinierung des Kontrollpools (Stage `gpp`):** Zuerst wird die Menge aller anwendbaren G++ Kontrollen für jedes Zielobjekt deterministisch ermittelt, unter Berücksichtigung der Vererbungshierarchie gemäß `zielobjekte.csv`.
2.  **Semantische Nähe im Kontext (Stage `matching`):** Die KI-gesteuerte Abbildung einer BSI Anforderung erfolgt ausschließlich gegen den Pool von G++ Kontrollen, der für das zuvor ausgewählte Zielobjekt ermittelt wurde.

### 2.3 Metadaten-Verarbeitung und KI-Anreicherung (Stage `component`)

In der finalen Stage wird die Implementierung der G++ Kontrolle dokumentiert. Im Gegensatz zu einer direkten Übernahme der BSI Altdaten verwendet das System einen generativen Ansatz:

1.  **Kontextualisierung:** Die Beschreibung der G++ Kontrolle wird mit einem Hinweis auf den Ursprungs-Baustein versehen (z.B. "(BSI Baustein APP.1)").
2.  **KI-Generierung:** Die KI (Gemini Pro) erhält die Texte der G++ Kontrolle (Prose, Guidance) und den Kontext des BSI Bausteins (Introduction, Risks). Basierend darauf generiert die KI:
    *   Detaillierte Beschreibungen für alle 5 Maturitätsstufen (Statement, Guidance, Assessment).
    *   Klassifizierungen (NIST Class, ISMS Phase, CIA Impact).

**Wichtiger Hinweis zur Architektur:** Die generierte Komponente basiert auf dem Profil des Zielobjekts (Ergebnis aus `stage_gpp`) und enthält daher *alle* anwendbaren G++ Kontrollen für dieses Zielobjekt, nicht nur die Teilmenge, die in `stage_matching` aus dem spezifischen Baustein migriert wurde.

## 3.0 Pipeline-Architektur und technische Implementierung

Die Architektur ist als modulare, mehrstufige Pipeline implementiert (Python). Die Orchestrierung erfolgt über `src/main.py` und `src/pipeline/processing.py`.

### 3.1 Unterstützende Infrastruktur

#### 3.1.1 KI-Client (`src/clients/ai_client.py`)

Der `AiClient` ist die zentrale Komponente für Interaktionen mit Google Vertex AI (nutzt das `google-genai` SDK).

*   **Modell-Konfiguration:** Ein Modell für alles, `gemini-4-argon` (`GEMINI_MODEL`); Qualität und Kosten werden je Call über den Thinking-Level gesetzt (`MAKER_THINKING_LEVEL` medium für Kandidaten- und Anreicherungs-Calls, `CHECKER_THINKING_LEVEL` high für Prüf- und Abwägungs-Calls), nie über ein zweites Modell. Kein explizites Caching: der stabile Prompt-Prefix (Korpus) wird implizit gecacht.
*   **Strukturierte Ausgabe:** Nutzt `GenerationConfig` mit `response_mime_type="application/json"` und `response_schema`.
*   **Asynchrone Verarbeitung:** Implementiert asynchrone Anfragen (via `.aio` accessor) für parallele Verarbeitung, gesteuert durch `asyncio.Semaphore`.
*   **Robuste Fehlerbehandlung:** Retry nur bei transienten Fehlern (429, 5xx, Timeouts) und bei Schema-Verstößen der Antwort, exponentieller Backoff, höchstens `API_MAX_RETRIES` (5) Wiederholungen je Call; permanente Fehler (400/401/403/404) brechen sofort mit Grund ab.
*   **Validierung:** Jede Antwort wird mittels `jsonschema.validate` validiert.

```python
# src/clients/ai_client.py (Auszug aus generate_validated_json_response)
# ...
# Asynchronous Generation call via .aio accessor
response = await self.client.aio.models.generate_content(
    model=model_to_use,
    contents=contents,
    config=gen_config,
)
# ...
except (errors.ClientError, ValueError, TypeError, ValidationError, httpx.ConnectError, httpx.TimeoutException) as e:
# ...