import asyncio
import dc_api
import discord
from bot_constants import *
from bot_token import BOT_TOKEN
from datetime import datetime


async def get_latest_post_id(board: str) -> int:
    async with dc_api.API() as api:
        async for index in api.board(board_id=board, num=1):
            # print(f"{index.id}번: {index.title}")
            # async for com in index.comments():
            #     com_lines = com.contents.split("\n")
            #     print(f"\t{com_lines}")
            return index.id


async def log_to_channel_with_timestamp(logtype, message, target_channel):
    now = datetime.now()
    dt_string = now.strftime("%Y/%m/%d %H:%M:%S")  # 2023-03-11 00:23:55
    await target_channel.send(f"**`{dt_string}`** -  **`{logtype.upper()}`**\t {message}")


class DCNewPostBot(discord.Client):
    async def on_ready(self):
        if GALLERY_TYPE not in [GalleryType.MAIN, GalleryType.MINOR, GalleryType.MINI]:
            raise UnknownGalleryTypeException(GALLERY_TYPE)
        old_id = int(await get_latest_post_id(GALLERY_NAME)) + 1
        channel = self.get_channel(TARGET_CHANNEL_ID)
        debug_log_channel = self.get_channel(DEBUG_LOG_CHANNEL_ID)
        await log_to_channel_with_timestamp("info", f"**__Bot started__**", debug_log_channel)
        while True:
            new_id = int(await get_latest_post_id(GALLERY_NAME)) + 1
            await log_to_channel_with_timestamp("info", f"Got new data: {old_id=}, {new_id=}", debug_log_channel)
            for post_id in range(old_id, new_id):
                await log_to_channel_with_timestamp("info", f"Sending new posts: Iter #{post_id - old_id + 1}", debug_log_channel)
                if GALLERY_TYPE == GalleryType.MINOR:
                    await channel.send(f"https://gall.dcinside.com/mgallery/board/view/?id={GALLERY_NAME}&no={post_id}")
                elif GALLERY_TYPE == GalleryType.MINI:
                    await channel.send(f"https://gall.dcinside.com/mini/board/view/?id={GALLERY_NAME}&no={post_id}")
                else:
                    await channel.send(f"https://gall.dcinside.com/board/view/?id={GALLERY_NAME}&no={post_id}")
                await asyncio.sleep(NEW_LINK_DELAY)
            await log_to_channel_with_timestamp("info", "Done sending new posts", debug_log_channel)
            old_id = new_id
            await log_to_channel_with_timestamp("info", f"Sleeping {REFRESH_TIME} secs", debug_log_channel)
            await asyncio.sleep(REFRESH_TIME)

    async def on_disconnect(self):
        debug_log_channel = self.get_channel(DEBUG_LOG_CHANNEL_ID)
        await log_to_channel_with_timestamp("info", f"**__Bot disconnected__**", debug_log_channel)


intents = discord.Intents.default()
intents.message_content = True

client = DCNewPostBot(intents=intents)
client.run(BOT_TOKEN)
