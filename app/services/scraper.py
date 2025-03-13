import logging
from telethon.tl.functions.messages import GetHistoryRequest
from app.database.db import get_db_connection
from app.services.telegram_client import client

logging.basicConfig(level=logging.INFO)

async def scrape_telegram_channels(channels):
    conn = get_db_connection()
    cursor = conn.cursor()
    all_data = {}

    for channel in channels:
        try:
            logging.info(f"📌 دریافت اطلاعات از: {channel}")
            channel_entity = await client.get_entity(channel)
            messages = await client(GetHistoryRequest(
            peer=channel_entity,
            limit=50,
            offset_id=0,
            offset_date=None,
            add_offset=0,
            max_id=0,
            min_id=0,
            hash=0
            ))


            for message in messages.messages:
                cursor.execute('''
                    INSERT INTO messages (channel, message_id, text, date, sender_id)
                    VALUES (?, ?, ?, ?, ?)
                ''', (channel, message.id, message.message, str(message.date), message.from_id.user_id if message.from_id else None))

            conn.commit()
            all_data[channel] = messages.messages
            logging.info(f"✅ پیام‌های {channel} دریافت و ذخیره شد.")

        except Exception as e:
            logging.error(f"❌ خطا در دریافت اطلاعات {channel}: {e}")

    conn.close()
    return all_data
