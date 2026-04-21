
# LangGraph Boilerplate Agent

## Overview
This repository provides a reusable boilerplate for building agent-based applications with LangGraph and LangChain. It includes environment management, observability with MLflow, and modern dependency management using `pyproject.toml` and `uv`.

## Features
- Loads environment variables from `.env`/`example.env`
- Initializes LLMs with LangChain and Google GenAI
- MLflow integration for experiment tracking
- Modern Python dependency management (no `requirements.txt` needed)
- FastAPI template for agent deployment as an API
- Docker and Docker Compose support for containerized deployment
- Ready-to-use testing setup with pytest

## Setup
1. Ensure Python 3.12 is installed (macOS/Homebrew):
   ```sh
   brew install python@3.12
   ```
   Or download from https://www.python.org/downloads/release/python-3120/

2. Create a new virtual environment with Python 3.12:
   ```sh
   python3.12 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```sh
   uv sync
   ```

4. Copy `example.env` to `.env` and fill in your API keys.

5. Run the main script:
   ```sh
   python main.py
   ```

## Development
- All dependencies are managed in `pyproject.toml` (use `uv sync` to install).
- Use `example.env` as a template for your `.env` file (never commit real secrets).

## Testing
Run all tests with:
```sh
pytest
```

## FastAPI Deployment
Run the agent as an API server:
```sh
uvicorn src.app:app --reload
```
You can POST to `/chat` with `{ "prompt": "your question" }` to interact with the agent.

## Docker
Build and run the agent in a container:
```sh
docker build -t langgraph-agent .
docker run --env-file .env -p 8000:8000 langgraph-agent
```

## Docker Compose
For local development or deployment:
```sh
docker compose up --build
```

## Observability
MLflow is included for experiment tracking. Set `MLFLOW_TRACKING_URI` in your `.env` file to enable logging.

## Notes
- This repo is designed as a reusable template. Use GitHub's "Use this template" feature or clone and re-init for new projects.
- `requirements.txt` is deprecated; use only `pyproject.toml` with uv.
- Never commit real API keys or secrets—use `.env` for your local values.

## License
MIT
