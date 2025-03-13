from fastapi import APIRouter, HTTPException
from app.database.db import get_db_connection
from app.services.scraper import scrape_telegram_channels

router = APIRouter()

@router.get("/fetch_telegram_data")
async def fetch_telegram_data():
    channels = ['@chiiro', '@Tajrobeh_home', '@Khaneh_Agahi1', '@yarroshd']
    return await scrape_telegram_channels(channels)

@router.get("/get_messages")
async def get_messages():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT channel, message_id, text, date, sender_id FROM messages ORDER BY date DESC")
        messages = cursor.fetchall()
        conn.close()

        return [{"channel": msg["channel"], "message_id": msg["message_id"], "text": msg["text"], "date": msg["date"], "sender_id": msg["sender_id"]} for msg in messages]
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="خطا در دریافت پیام‌ها از دیتابیس")
