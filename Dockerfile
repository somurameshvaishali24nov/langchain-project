FROM python:3.12-slim

# Install Linux packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

WORKDIR /app

# Copy dependency files first (Docker cache)
COPY pyproject.toml ./

# If a lock file exists, copy it as well
COPY uv.lock* ./

# Install dependencies (including dev dependencies)
# Cache mount keeps downloaded wheels across rebuilds, even when this layer's cache is invalidated
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --group dev

# Copy project files
COPY . .

EXPOSE 8888

# Dev Container overrides this command
CMD ["sleep", "infinity"]