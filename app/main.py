import uvicorn
import logging
import yaml

from fastapi import FastAPI, Request
from fastapi.logger import logger
from pydantic_settings import BaseSettings
from app.models import Registry, RegistryRequest
from hmac_http import verify
from pprint import pformat

# Disable uvicorn access logger
uvicorn_access = logging.getLogger("uvicorn.access")
uvicorn_access.disabled = True

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.getLevelName(logging.DEBUG))

secret = "asdf"

registry_list = []

app = FastAPI(
    title="Drone CI Registry Plugin",
    version="0.0.1",
    contact={
        "name": "Andrea Bettarini",
        "url": "https://monema.it",
        "email": "info@monema.it",
    },
)


class Settings(BaseSettings):
    drone_debug: bool = False
    drone_secret: str
    drone_config_file: str


@app.on_event("startup")
async def init_client() -> None:
    logger.info("Loading settings")
    logger.info(f"Config file: {Settings().drone_config_file}")

    with open(Settings().drone_config_file, "r") as file:
        registry_list = yaml.safe_load(file)

    logger.debug(f"Registry list: {pformat(registry_list)}")


@app.post("/")
async def get_credentials(data: RegistryRequest, request: Request):
    try:
        verify(request, secret)

        response_data = []
        response_data.append(
            Registry(
                username="user",
                password="password",
                address="address",
            )
        )
        return response_data

    except Exception as e:
        logger.error(e)
        return {"message": "error"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3000)
