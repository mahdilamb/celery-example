FROM ghcr.io/astral-sh/uv:python3.13-alpine AS worker

WORKDIR /app
COPY pyproject.toml uv.lock ./

RUN uv sync --no-install-project --no-dev --frozen

# Install source
RUN touch README.md
RUN mkdir -p ./src/celery_example
RUN touch ./src/celery_example/__init__.py
COPY src/celery_example/tasks.py ./src/celery_example/tasks.py

RUN uv pip install -e . --no-deps

# Set non-sudo user
WORKDIR /app/src

RUN addgroup -S appgroup && adduser -S appuser -G appgroup
RUN chown -R appuser:appgroup /app
USER appuser


CMD ["uv", "run", "celery", "-A", "celery_example.tasks", "worker", "--loglevel=warning"]


FROM ghcr.io/astral-sh/uv:python3.13-alpine AS app


# Install dependencies

WORKDIR /app
COPY pyproject.toml uv.lock ./

RUN uv sync --no-install-project --no-dev --frozen

# Install source
RUN touch README.md
COPY src/ ./src/
RUN uv pip install -e . --no-deps

WORKDIR /app/src

CMD ["uv", "run", "python3", "-m", "celery_example"]
