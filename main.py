import os
import discord
from requests import Request, Session
import json
from keep_alive import keep_alive

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {
  'symbol':'SOLBEAR',
  'convert':'USD'
}



header = {
  'Accepts':'application/json',
  'X-CMC_PRO_API_KEY': os.environ['CMC_API']
}

session = Session()
session.headers.update(header)

response = session.get(url, params=parameters)


value = json.loads(response.text)
value1 = value['data']['SOLBEAR']['quote']['USD']['price']
price = "{:.8f}".format(value1)

client = discord.Client()

@client.event
async def on_ready():
    print('We are logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$price'):
            await message.channel.send('🇸 🇴 🇱 🇦 🇷  🇧 🇪 🇦 🇷  🇵 🇷 🇮 🇨 🇪' + '\n' + '$' + price)


keep_alive()
client.run(os.environ['TOKEN'])
