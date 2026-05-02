# Multilingual Text Preprocessing Engine

A FastAPI service for preprocessing English and Arabic text through a single API endpoint.

## Features

- English and Arabic preprocessing
- Optional stopword removal
- Optional stemming and lemmatization
- Arabic normalization support
- Web UI served at `/`
- OpenAPI docs available at `/docs`

## Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic
- NLTK
- Jinja2

## Run Locally

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start the app:

```bash
uvicorn src.main:app --reload
```

3. Open:

- App: `http://127.0.0.1:8000`
- API docs: `http://127.0.0.1:8000/docs`
- Health check: `http://127.0.0.1:8000/health`

## Run with Docker

Build image:

```bash
docker build -t text-preprocessor .
```

Run container:

```bash
docker run -p 8000:8000 text-preprocessor
```

## API

### `POST /preprocess`

Request body:

```json
{
  "text": "This is a sample text for preprocessing.",
  "language": "english",
  "remove_stopwords": true,
  "stemming": false,
  "lemmatization": false,
  "normalization": true
}
```

Example response:

```json
{
  "original_text": "This is a sample text for preprocessing.",
  "processed_text": "sample text preprocessing",
  "language": "english",
  "applied_steps": {
    "remove_stopwords": true,
    "stemming": false,
    "lemmatization": false,
    "normalization": true
  },
  "success": true,
  "message": "Text preprocessing completed successfully."
}
```

Supported `language` values:

- `english`
- `arabic`