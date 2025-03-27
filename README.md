# Palworld Discord to Chat Messenger
This is a simple Python script that listens to a specific Discord channel and sends messages from that channel to a Palworld server's chat using RCON.

Requirements
Python 3.x

Libraries:

discord.py

python-dotenv

mcrcon

You can install the required libraries by running:

bash
Copy
Edit
pip install discord.py python-dotenv mcrcon
Setup
Clone the repository:

bash
Copy
Edit
git clone <your-repo-url>
cd <your-repo-directory>
Create the .env file:

Copy the .env_example file to a new file named .env:

bash
Copy
Edit
cp .env_example .env
Configure the .env file:

Open the .env file and add the required values:

ini
Copy
Edit
DISCORD_TOKEN=your_discord_token_here
CHANNEL_ID=your_channel_id_here
BATTLEMETRICS_TOKEN=your_battlemetrics_token_here
RCON_HOST=your_rcon_host_here
RCON_PORT=your_rcon_port_here
RCON_PASSWORD=your_rcon_password_here
DISCORD_TOKEN: Your Discord bot token.

CHANNEL_ID: The ID of the Discord channel you want to listen to.

BATTLEMETRICS_TOKEN: (Optional) Your Battlemetrics API token.

RCON_HOST: The IP address of the Palworld server.

RCON_PORT: The RCON port of the Palworld server.

RCON_PASSWORD: The password for RCON access.

How It Works
The bot listens for messages in the specified Discord channel.

When a message is sent in that channel, the bot will take the message and send it to the Palworld server chat via RCON.

The message format will be [Username]: Message, and the message will be truncated to 128 characters to avoid overflow.

Running the Bot
Once everything is set up, run the bot with the following command:

bash
Copy
Edit
python bot.py
The bot will log in, listen for messages from the specified Discord channel, and send them to the Palworld server.

Example .env File
ini
Copy
Edit
DISCORD_TOKEN=your_discord_token_here
CHANNEL_ID=123456789012345678
BATTLEMETRICS_TOKEN=your_battlemetrics_token_here
RCON_HOST=your_rcon_host_here
RCON_PORT=25575
RCON_PASSWORD=your_rcon_password_here
License
This project is open-source and available under the MIT License. See the LICENSE file for more information.