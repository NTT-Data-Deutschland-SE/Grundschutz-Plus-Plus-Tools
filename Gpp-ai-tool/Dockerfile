# Container der OSCAL-Pipeline (Cloud Run Job). Build-Kontext ist das Tool-Root (Gpp-ai-tool/),
# deploy.sh wechselt dorthin. Ein Image, jede Stage per `--stage`.
FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
WORKDIR /srv
# Abhängigkeiten zuerst (Layer-Cache); uv.lock wird genutzt, wenn vorhanden.
COPY pyproject.toml uv.lock* ./
RUN uv sync --no-dev --frozen
COPY src ./src
RUN addgroup --system app && adduser --system --ingroup app app && chown -R app:app /srv
USER app
# Das venv direkt ausführen: `uv run` würde neu syncen und braucht ein schreibbares HOME.
ENTRYPOINT ["/srv/.venv/bin/python", "src/main.py"]
