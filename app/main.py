from fastapi import FastAPI

from app.api.routes import router


app = FastAPI(
    title="Political News Intelligence API",
    version="1.0"
)


@app.get("/")
def home():

    return {
        "message":
        "Political News Intelligence API"
    }


app.include_router(router)