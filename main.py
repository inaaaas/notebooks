from fastapi import FastAPI
from .routers import laptops

app = FastAPI()

app.include_router(laptops.router, prefix="/api", tags=["Laptops"])
