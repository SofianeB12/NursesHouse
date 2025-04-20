from fastapi import FastAPI
from .routers import composants
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(composants.router, prefix="/composants", tags=["Composants"])
