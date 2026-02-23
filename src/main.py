from fastapi import (
    FastAPI, staticfiles, status, Request, Response,
    routing
)
from fastapi.responses import JSONResponse

from .. import settings
from .helpers.http_helpers import ResponseHandler
from .apps.core.routes import router as core_router

app = FastAPI(
    debug=settings.DEBUG, title="Job Striker",
    summary="""
    Automated job application software
    """
)
app.mount(
    "/static", staticfiles.StaticFiles(directory="staticfiles"), name="static"
)


@app.get("/")
def home():
    return ResponseHandler.handle_response(
        data={"message": "Welcome to Job Striker!"}
    )

app.include_router(core_router, prefix="/api/v1")
