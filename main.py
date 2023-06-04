import discord
import requests
import os
import bcolors
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True
client = discord.Bot(intents=intents)  # specify the guild IDs in debug_guilds
TOKEN = os.getenv('TOKEN')

# // LOADING COGS //

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        try:
            try:
                client.unload_extension(f"cogs.{file[:-3]}")
            except:
                print("Cog Not Yet Loaded...")
                pass
            client.load_extension(f"cogs.{file[:-3]}")
            print(f'Loaded: {file}')

        except Exception as Error:
            print(f"Error whilst Starting up Cogs: {Error}")


@client.event
async def on_ready():
    print(f"\n{bcolors.FAIL}--------------------------------------\n{bcolors.FAIL}{client.user} is ready and online!\n{bcolors.FAIL}--------------------------------------")
    print(f'{bcolors.FAIL}-------------------------------------------------------\n{bcolors.FAIL}Successfully Established a Connection to the Database\n{bcolors.FAIL}-------------------------------------------------------\n')


client.run(TOKEN)
