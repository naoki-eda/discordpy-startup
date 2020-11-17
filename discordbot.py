#coding:UTF-8
import os
import discord
from discord.ext import tasks
from datetime import datetime 

token = os.environ['DISCORD_BOT_TOKEN'] #トークン
channel_id = os.environ['CHANNEL_ID'] #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

await client.wait_until_ready()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    # now = datetime.now().strftime('%H:%M')
    # if now == '15:15':
        channel = client.get_channel(channel_id)
        await channel.send('てすと')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(token)
