from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from prometheus_fastapi_instrumentator import Instrumentator

from app.controllers import math_controller
from app.database.session import Base, engine
from app.models.request_log import RequestLog

# Ensure all tables are created before app starts
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Math Microservice")
app.include_router(math_controller.router)
app.mount("/static", StaticFiles(directory="app/frontend"), name="static")
Instrumentator().instrument(app).expose(app)
