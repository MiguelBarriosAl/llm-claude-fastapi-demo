from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.file_utils import get_file_content
from app.claude_api import ask_claude

app = FastAPI()

class QueryRequest(BaseModel):
    filename: str
    query: str

@app.post("/ask-claude")
async def ask_claude_from_file(request: QueryRequest):
    try:
        contenido = get_file_content(request.filename)
        prompt = f"{request.query}\n\nArchivo:\n{contenido}"
        respuesta = await ask_claude(prompt)
        return {"respuesta": respuesta}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
