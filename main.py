import discord
from webserver import keep_alive
import os

discord_token_bot = 'token'

class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        word_list = []

        # don't respond to ourselves
        if message.author == self.user:
            return

        messageContent = message.content
        if len(messageContent) > 0:
            for word in word_list:
                if word in messageContent:
                    await message.delete()
                    await message.channel.send('Bruh!')
                    



client = MyClient()
keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(discord_token_bot)
