x=1
y=''
def a(message):
  global x
  global y
  if x == 1:
    reply[message] = '?'
    y=message
    x=2
  else:
    reply[y] = message
    x=1

import discord
import os
TOKEN = os.environ['TOKEN']



# 取得 Discord client 物件才能操作
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
reply ={'dc':'幹嘛'}
# 調用 event 函式庫
@client.event






# 當機器人完成啟動時在終端機顯示提示訊息
async def on_ready():
    print(f'目前登入身份：{client.user}')

# 調用 event 函式庫
@client.event
# 當有訊息時
async def on_message(message):
  global x
  global y
  global reply
  global b

    # 排除機器人本身發出的訊息，避免機器人自問自答的無限迴圈
  if message.author == client.user:
    return
  
  if message.content.startswith('dc') :
    
    if message.content.startswith('dca') :
      for b in reply:
        await message.channel.send([b,reply[b]])
    elif message.content.startswith('dcf') :
      tmp = message.content.split(" ",2)
      y=tmp[1]
      reply[y]='?'
      x=2
    elif message.content.startswith('dcr'):
      reply={}
      reply ={'dc':'幹嘛'}
      
    else :  
      tmp = message.content.split(" ",2)
      if tmp[1] in reply:
        await message.channel.send(reply[tmp[1]])
      else:
        await message.channel.send('?')
  elif message.content in reply and reply[message.content]!='?':
    return
  else:
    a(message.content)


    
         
client.run(TOKEN) #TOKEN在剛剛Discord Developer那邊「BOT」頁面裡面
