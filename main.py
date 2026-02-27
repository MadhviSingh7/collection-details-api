from fastapi import FastAPI, Request
from script.core.handlers.handlers import router
from script.core.utilities.logger import logger
import uvicorn

app = FastAPI()


# Request Logging Middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):

    response = await call_next(request)

    logger.info(
        f"{request.method} | {request.url.path} | {response.status_code}"
    )

    return response


# Include routers
app.include_router(router)


# Run using python main.py
if __name__ == "__main__":
    uvicorn.run(
        "main:app",   # Correct for your structure
        host="0.0.0.0",
        port=8004,
        reload=True
    )