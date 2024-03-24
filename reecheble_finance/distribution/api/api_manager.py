"""
Reecheble Finance Swagger Documentation - http://0.0.0.0:8000/docs
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_versioning import VersionedFastAPI

from reecheble_finance.distribution.api.routers import loan_controller, loan_account_controller
from reecheble_finance.domain.utilities.logger import LogManager

__all__ = [
    "App",
    "AppManager"
]

logger = LogManager().logger


class App:
    _title = "Reecheble Finance: Web-API Host Service"
    name = "Web-API Host"
    application = None

    def __init__(self):
        logger.info("Loading API Endpoints...")
        hosting_application = FastAPI(
            title=self._title,
            description="Reecheble Finance Loans Microservice"
        )
        # Add application routers
        hosting_application.include_router(loan_account_controller.router)
        hosting_application.include_router(loan_controller.router)

        self.application = VersionedFastAPI(
            hosting_application,
            version_format='{major}',
            prefix_format='/v{major}',
            enable_latest=True
        )

        # TODO: This should be in some sort of a config for different environments.
        origins = [
            "http://localhost:4200"  # Add angular client.
        ]
        self.application.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
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
