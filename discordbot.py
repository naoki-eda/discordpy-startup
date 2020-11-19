#coding:UTF-8
import os
import discord
from discord.ext import tasks
from datetime import datetime 

token = os.environ['DISCORD_BOT_TOKEN'] #トークン
channel_id = os.environ['CHANNEL_ID'] #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

@tasks.loop(seconds=60)
async def loop():
    print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"), "start")
    print(client.is_ready())
    channel = client.get_channel(channel_id)
    if channel != None :
        print(channel)
        await channel.send('てすと')  

@client.event
async def on_ready():
    #ループ処理実行
    loop.start()

# Botの起動とDiscordサーバーへの接続
client.run(token)
