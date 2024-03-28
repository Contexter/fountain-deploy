# Event handlers for startup and shutdown actions
from fastapi import FastAPI

def create_start_app_handler(app: FastAPI) -> callable:
    async def start_app() -> None:
        # Perform startup actions here
        pass
    return start_app

def create_stop_app_handler(app: FastAPI) -> callable:
    async def stop_app() -> None:
        # Perform shutdown actions here
        pass
    return stop_app
