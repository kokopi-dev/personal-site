#!/usr/bin/env python3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
from utils import Env
from utils.staticfiles import init_static
from routers import home


init_static()
# Env Specific Variables
if Env.ENV == "dev":
    origins = ["*"]
else:
    origins = [
        "https://derrickgee.dev",
        "https://www.derrickgee.dev",
        "www.derrickgee.dev",
        "derrickgee.dev"
    ]


app = FastAPI(docs_url=None, redoc_url=None)

# Routes
app.include_router(home.router)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"]
)

app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
