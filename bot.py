from pyrogram import Client, filters
from helpers.gdrive_downloader import download_gdrive
from helpers.dailymotion_downloader import download_dailymotion
from config import BOT_TOKEN, API_ID, API_HASH
import os

app = Client("gdrivebot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.private & filters.text)
async def handle_link(client, message):
    link = message.text.strip()

    if "drive.google.com" in link:
        await message.reply("📥 Google Drive link detected. Downloading...")
        filename = await download_gdrive(link)
        if filename:
            await message.reply_document(filename, caption="✅ File downloaded from Google Drive")
            os.remove(filename)
        else:
            await message.reply("❌ Failed to download Google Drive file.")

    elif "dailymotion.com" in link:
        await message.reply("📥 Dailymotion link detected. Downloading...")
        filename = await download_dailymotion(link)
        if filename:
            await message.reply_document(filename, caption="✅ File downloaded from Dailymotion")
            os.remove(filename)
        else:
            await message.reply("❌ Failed to download Dailymotion video.")
    else:
        await message.reply("❗ Please send a valid Google Drive or Dailymotion link.")

app.run()
