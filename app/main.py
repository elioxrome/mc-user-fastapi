from fastapi import FastAPI

from app.api.routes import health_router, users_router

app = FastAPI(title="mc-user-fastapi", version="1.0.0")

app.include_router(users_router)
app.include_router(health_router)
