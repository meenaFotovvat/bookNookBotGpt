import logging
from fastapi import FastAPI
from app.database.db import init_db
from app.routes import messages
from app.services.telegram_client import client

logging.basicConfig(level=logging.INFO)

app = FastAPI()
app.include_router(messages.router)

@app.on_event("startup")
async def startup_event():
    init_db()
    await client.start()
    logging.info("🚀 ربات آماده اجرا است!")

@app.on_event("shutdown")
async def shutdown_event():
    await client.disconnect()
