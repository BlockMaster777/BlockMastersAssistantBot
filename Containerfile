FROM ghcr.io/astral-sh/uv:0.13.5-python3.14-trixie

WORKDIR /app

ENV UV_PROJECT_ENVIRONMENT=/app/.venv \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev --no-install-project

COPY . .

CMD ["uv", "run", "--no-sync", "python", "assistant/main.py"]
