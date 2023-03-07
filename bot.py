import asyncio
import dc_api
import discord
from bot_constants import *
from bot_token import BOT_TOKEN


async def get_latest_post_id(board: str) -> int:
    async with dc_api.API() as api:
        async for index in api.board(board_id=board, num=1):
            # print(f"{index.id}번: {index.title}")
            # async for com in index.comments():
            #     com_lines = com.contents.split("\n")
            #     print(f"\t{com_lines}")
            return index.id


class DCNewPostBot(discord.Client):
    async def on_ready(self):
        if GALLERY_TYPE not in [GalleryType.MAIN, GalleryType.MINOR, GalleryType.MINI]:
            raise UnknownGalleryTypeException(GALLERY_TYPE)
        old_id = int(await get_latest_post_id(GALLERY_NAME)) + 1
        channel = self.get_channel(TARGET_CHANNEL_ID)
        # await channel.send("I'm here!")
        print(f'Logged on as {self.user}!')
        while True:
            print("started main loop")
            new_id = int(await get_latest_post_id(GALLERY_NAME)) + 1
            print(f"updated new_id, {old_id=}, {new_id=}")
            for post_id in range(old_id, new_id):
                print(f"send new post url loop: iteration {post_id - old_id + 1}")
                if GALLERY_TYPE == GalleryType.MINOR:
                    await channel.send(f"https://gall.dcinside.com/mgallery/board/view/?id={GALLERY_NAME}&no={post_id}")
                elif GALLERY_TYPE == GalleryType.MINI:
                    await channel.send(f"https://gall.dcinside.com/mini/board/view/?id={GALLERY_NAME}&no={post_id}")
                else:
                    await channel.send(f"https://gall.dcinside.com/board/view/?id={GALLERY_NAME}&no={post_id}")
                await asyncio.sleep(NEW_LINK_DELAY)
            print("exited send new post url loop")
            old_id = new_id
            print(f"updated old_id with new_id, sleeping {REFRESH_TIME} secs")
            await asyncio.sleep(REFRESH_TIME)


intents = discord.Intents.default()
intents.message_content = True

client = DCNewPostBot(intents=intents)
client.run(BOT_TOKEN)
