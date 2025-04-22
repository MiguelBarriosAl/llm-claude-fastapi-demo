# LLM Claude API Server Demo – Claude API + FastAPI

Este proyecto es una demostración simple de cómo interactuar con archivos locales y obtener respuestas de Claude a través de su API oficial.

---

## ¿Qué hace esta API?

- Lee archivos `.txt` almacenados en una carpeta local (`files/`)
- Recibe una pregunta o instrucción para aplicar al archivo (por ejemplo, "resume este archivo")
- Envía el contenido como prompt a Claude (vía API REST)
- Devuelve la respuesta de Claude como texto JSON

---

## Estructura del proyecto

    ├── app
    │   ├── claude_api.py
    │   ├── document.py
    │   ├── file_utils.py
    │   ├── main.py
    │       
    ├── files
    │   └── informe.txt
    ├── poetry.lock
    ├── pyproject.toml
    ├── README.md

## Requisitos

- Python 3.10 o superior
- [Poetry](https://python-poetry.org/)
- Una API Key de Claude (https://console.anthropic.com)

---

## Instalación

    poetry install
    poetry shell

## RUN

    mkdir -p files
    echo "Contenido del informe..." > files/informe.txt

    export CLAUDE_API_KEY="sk-ant-apiKEY-xxxxxxxxxxxxxxxx"
    uvicorn app.main:app --reload

### Terminal

    curl -X POST http://localhost:8000/ask-claude \
    -H "Content-Type: application/json" \
    -d '{
        "filename": "informe.txt",
        "query": "Resume este documento en 3 frases."
    }'

