import logging
import os
from functools import lru_cache

import uvicorn
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic_settings import BaseSettings

from api.routes.v1_router import v1_router


class Settings(BaseSettings):
    model: str = "mistral"
    temperature: float = 0.0
    host: str = "0.0.0.0"
    port: int = 8080

    class Config:
        env_prefix = "APP_"


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
settings = Settings()

app = FastAPI(
    title="AI-App",
    version="0.1.0",
    docs_url=None,
    redoc_url=None,
    # lifespan=lifespan
)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(v1_router)


@app.get("/", include_in_schema=False)
def home() -> RedirectResponse:
    return RedirectResponse("/docs")


@app.get("/docs", include_in_schema=False)
async def get_docs():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title=app.title,
        swagger_favicon_url="/favicon.ico"
    )


@lru_cache
def _get_favicon() -> FileResponse:
    file_name = "favicon.ico"
    file_path = os.path.join("static", file_name)
    return FileResponse(path=file_path, headers={"Content-Disposition": f"attachment; filename={file_name}"})


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return _get_favicon()


if __name__ == "__main__":
    uvicorn.run(app, host=settings.host, port=settings.port, reload=False, log_level="warning")
