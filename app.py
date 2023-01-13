from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="my first api",
    description="primera api",
    version="0.0.1",
    openapi_tags=[{
        "name": "users",
        "description": "user routes"
    }]
)

app.include_router(user)
