import uvicorn
from fastapi import FastAPI, APIRouter
from contextlib import asynccontextmanager
from app.core.config import settings
from app.logger import init_logger
from api.users.router import router as users_router
from api.groups.router import router as groups_router
from api.fields.router import router as fields_router
from api.entities.router import router as entities_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_logger(settings.PROJECT_NAME)
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan
)

api = APIRouter()

api.include_router(users_router, prefix="/user", tags=["users"])
api.include_router(groups_router, prefix="/group", tags=["groups"])
api.include_router(fields_router, prefix="/field", tags=["fields"])
api.include_router(entities_router, prefix="/entity", tags=["entities"])

app.include_router(api)

@app.get("/")
async def health_check():
    return {"status": "ok"}

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
