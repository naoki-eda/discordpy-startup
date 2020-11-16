#coding:UTF-8
import os
import discord
from discord.ext import tasks
from datetime import datetime 

TOKEN = os.environ.get("DISCORD_BOT_TOKEN") #トークン
CHANNEL_ID = os.environ.get("CHANNEL_ID") #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '01:16':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('てすと')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
