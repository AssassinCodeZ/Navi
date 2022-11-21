[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Python: 3.8](https://img.shields.io/badge/Python-3.8+-brightgreen.svg)](https://www.python.org/) [![Database: SQLite](https://img.shields.io/badge/Database-SQLite-blue.svg)](https://www.sqlite.org/index.html)
# Navi

Reminder / Helper for EPIC RPG. This reminder supports the latest slash commands.  

# Setup
• Install python 3.8, 3.9 or 3.10. Note that python 3.11+ is currently not supported by the libraries the bot uses.  
• Install the third party libraries mentioned in `requirements.txt`.  
• Create a Discord application with a bot user and generate a bot token.  
• Rename `default.env` to `.env` and add your token.  
• Rename `database/default_db.db` to `database/navi_db.db`.  
• Upload all emojis in `images/emojis` to a private server Navi an see.  
• Change all emojis in `resources/emojis.py` to the ones you uploaded.  
• Run `bot.py`.  

# Required intents
• guilds  
• members  
• message_content  
• messages  

# Required permissions
• Send Messages  
• Embed Links  
• Add Reactions  
• Use External Emoji  
• Read Message History  

# Commands
• Navi uses slash commands but also supports some legacy commands.  
• Default prefix for legacy commands is `navi `.  
• Use `/help` for an overview.  

# Dev commands
 • The dev commands are not listed in `/help`.  
 • These can be used to set event reductions, change default cooldowns, load cogs, shutdown the bot, etc.  
