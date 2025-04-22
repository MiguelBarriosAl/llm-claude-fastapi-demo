from fastapi import FastAPI
from fastmcp import FastMCP
from app.documents import read_file, list_files

app = FastAPI()
mcp = FastMCP("DocumentExplorer")

@app.on_event("startup")
async def startup_event():
    mcp.resource("file://{filename}")(read_file)
    mcp.tool()(list_files)
    mcp.mount(app)
