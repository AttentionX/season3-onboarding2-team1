# main.py
from fastapi import FastAPI
from router import test_router

app = FastAPI()
app.include_router(test_router.router)
