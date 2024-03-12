"""
zoRn Distribution Swagger Documentation - http://0.0.0.0:8000/docs
"""

import uvicorn
from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI

from reecheble_finance.domain.utilities.logger import LogManager
from reecheble_finance.distribution.api.routers import zorn_event_management_api

__all__ = [
    "App",
    "AppManager"
]

logger = LogManager().logger


class App:
    _title = "zoRn Distribution: Microservice API Host Service"
    name = "Microservice API Host"
    application = None

    def __init__(self):
        logger.info("Loading API Endpoints...")
        hosting_application = FastAPI(
            title=self._title,
            description="zoRn Distribution Microservice"
        )
        hosting_application.include_router(zorn_event_management_api.router)
        self.application = VersionedFastAPI(
            hosting_application,
            version_format='{major}',
            prefix_format='/v{major}',
            enable_latest=True
        )


class AppManager:
    _host = '0.0.0.0'
    _port = 8000
    app = None

    def __init__(self) -> None:
        self._get_application()

    def start(self):
        self._get_application()
        logger.info(f"Starting - {self.app.name}")
        uvicorn.run(self.app.application, host=self._host, port=self._port, log_level="info")

    def _get_application(self):
        app_service = App
        app_name = app_service.name
        logger.info(f"Loading - {app_name} ...")
        app = app_service()
        self.app = app

