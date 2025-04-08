from fastapi import FastAPI
from controller.locadora import router

app = FastAPI()

app.include_router(router)
