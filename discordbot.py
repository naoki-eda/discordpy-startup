#coding:UTF-8
import os
import discord
from discord.ext import tasks
from datetime import datetime 

token = os.environ['DISCORD_BOT_TOKEN'] #トークン
channel_id = os.environ['CHANNEL_ID'] #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# @tasks.loop(seconds=60)
# async def loop():
#     print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"), "start")
#     print("token", token)
#     print("channel_id", channel_id)
# #     await client.wait_until_ready()
#     print(client.is_ready())
#     channel = client.get_channel(channel_id)
#     print(channel)
#     await channel.send('てすと')  

# @client.event
# async def on_ready():
#     channel = client.get_channel(channel_id)
#     print(channel)
#     await channel.send('てすと')  
#     #ループ処理実行
#     loop.start()

# # Botの起動とDiscordサーバーへの接続
# client.run(token)

channel_sent = None
@tasks.loop(seconds=10)
async def send_message_every_10sec():
    await channel_sent.send("10秒経ったよ")

@client.event
async def on_ready():
    global channel_sent 
    channel_sent = client.get_channel(channel_id)
    send_message_every_10sec.start() #定期実行するメソッドの後ろに.start()をつける


client.run(token)
