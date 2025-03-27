import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from mcrcon import MCRcon  # Using direct RCON communication

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
RCON_HOST = os.getenv("RCON_HOST")
RCON_PORT = int(os.getenv("RCON_PORT"))
RCON_PASSWORD = os.getenv("RCON_PASSWORD")

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents, help_command=None)

def send_announcement(username: str, message: str):
    formatted_message = f"[{username}]: {message[:128]}"  # Prefix username and truncate
    try:
        with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as rcon:
            response = rcon.command(f"broadcast {formatted_message}")
            print("Message successfully announced.")
    except Exception as e:
        print("Failed to send message:", str(e))

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        print(f"Listening for messages in: {channel.name} ({CHANNEL_ID})")
    else:
        print("Could not find the specified channel.")

@client.event
async def on_message(message):
    if message.author.bot or message.channel.id != CHANNEL_ID:
        return
    send_announcement(message.author.display_name, message.content)

client.run(DISCORD_TOKEN)


















