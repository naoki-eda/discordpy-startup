#coding:UTF-8
import discord
from discord.ext import tasks
from datetime import datetime 

TOKEN = "Nzc3ODg4MTEzNzg2NjE3OTA2.X7J-wg.-wL1XP8s3eVPU0PWv3-ZebUELus" #トークン
CHANNEL_ID = 687202041856000003 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '00:28':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('てすと')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
