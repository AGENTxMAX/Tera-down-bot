import requests
import aria2p
from datetime import datetime
from status import format_progress_bar
import asyncio
import os, time
import logging
from pyrogram.errors import MessageNotModified, FloodWait

import asyncio
from yt_dlp import YoutubeDL

async def download_video(url, reply_msg, user_mention, user_id):
    response = requests.get(f"https://terabox.udayscriptsx.workers.dev/?url={url}")
    response.raise_for_status()
    data = response.json()

    fast_download_link = data["link"]
    thumbnail_url = data["thumb"]
    video_title = data["file_name"]

    download_dir = "downloads"
    os.makedirs(download_dir, exist_ok=True)

    output_template = os.path.join(download_dir, "%(title)s.%(ext)s")

    ydl_opts = {
        "outtmpl": output_template,
        "progress_hooks": [],
        "noplaylist": True,
    }

    start_time = datetime.now()

    def progress_hook(d):
        if d["status"] == "downloading":
            percentage = d.get("_percent_str", "0%").strip()
            done = d.get("downloaded_bytes", 0)
            total_size = d.get("total_bytes", 1)
            speed = d.get("_speed_str", "0B/s").strip()
            eta = d.get("_eta_str", "N/A").strip()
            elapsed_time_seconds = (datetime.now() - start_time).total_seconds()

            progress_text = format_progress_bar(
                filename=video_title,
                percentage=percentage,
                done=done,
                total_size=total_size,
                status="Downloading",
                eta=eta,
                speed=speed,
                elapsed=elapsed_time_seconds,
                user_mention=user_mention,
                user_id=user_id,
            )

            loop = asyncio.get_running_loop()
            asyncio.run_coroutine_threadsafe(reply_msg.edit_text(progress_text), loop)

        elif d["status"] == "finished":
            return d["filename"]

    ydl_opts["progress_hooks"].append(progress_hook)

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(fast_download_link, download=True)
        file_path = ydl.prepare_filename(info)

    # Download thumbnail
    thumbnail_path = os.path.join(download_dir, "thumbnail.jpg")
    thumbnail_response = requests.get(thumbnail_url)
    with open(thumbnail_path, "wb") as thumb_file:
        thumb_file.write(thumbnail_response.content)

    await reply_msg.edit_text("ᴜᴘʟᴏᴀᴅɪɴɢ...")

    return file_path, thumbnail_path, video_title


async def upload_video(client, file_path, thumbnail_path, video_title, reply_msg, collection_channel_id, user_mention, user_id, message):
    file_size = os.path.getsize(file_path)
    uploaded = 0
    start_time = datetime.now()
    last_update_time = time.time()

    async def progress(current, total):
        nonlocal uploaded, last_update_time
        uploaded = current
        percentage = (current / total) * 100
        elapsed_time_seconds = (datetime.now() - start_time).total_seconds()
        
        if time.time() - last_update_time > 2:
            progress_text = format_progress_bar(
                filename=video_title,
                percentage=percentage,
                done=current,
                total_size=total,
                status="Uploading",
                eta=(total - current) / (current / elapsed_time_seconds) if current > 0 else 0,
                speed=current / elapsed_time_seconds if current > 0 else 0,
                elapsed=elapsed_time_seconds,
                user_mention=user_mention,
                user_id=user_id,
                aria2p_gid=""
            )
            try:
                await reply_msg.edit_text(progress_text)
                last_update_time = time.time()
            except Exception as e:
                logging.warning(f"Error updating progress message: {e}")

    with open(file_path, 'rb') as file:
        collection_message = await client.send_video(
            chat_id=collection_channel_id,
            video=file,
            caption=f"✨ {video_title}\n👤 ʟᴇᴇᴄʜᴇᴅ ʙʏ : {user_mention}\n📥 ᴜsᴇʀ ʟɪɴᴋ: tg://user?id={user_id}",
            thumb=thumbnail_path,
            progress=progress
        )
        await client.copy_message(
            chat_id=message.chat.id,
            from_chat_id=collection_channel_id,
            message_id=collection_message.id
        )
        await asyncio.sleep(1)
        await message.delete()
        await message.reply_sticker("CAACAgIAAxkBAAEZdwRmJhCNfFRnXwR_lVKU1L9F3qzbtAAC4gUAAj-VzApzZV-v3phk4DQE")

    await reply_msg.delete()

    os.remove(file_path)
    os.remove(thumbnail_path)
    return collection_message.id
