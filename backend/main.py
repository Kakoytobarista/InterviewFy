import logging

import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config.project_config import settings
from src.routes import get_apps_router


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_application() -> FastAPI:
    try:
        application = FastAPI(
            title=settings.PROJECT_NAME,
            debug=settings.DEBUG,
            version=settings.VERSION
        )
        application.include_router(get_apps_router())

        application.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
            allow_headers=["*"],
        )
        return application
    except Exception as e:
        logger.error(f"Error while construct app, Error: {e}")


app = get_application()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
