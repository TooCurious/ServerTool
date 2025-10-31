FROM python:3.12-slim-trixie

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml /app/pyproject.toml

COPY uv.lock /app/uv.lock 

COPY main.py /app/main.py

WORKDIR /app
RUN uv sync --locked

CMD ["uv", "run", "python", "main.py"]