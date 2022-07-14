# sleepy-potion.py

from datetime import timedelta
import re

import discord
from discord.ext import commands

from database import errors, reminders, users
from resources import emojis, exceptions, functions, settings


class SleepyPotionCog(commands.Cog):
    """Cog that contains the sleepy potion detection commands"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        """Runs when a message is sent in a channel."""
        if message.author.id != settings.EPIC_RPG_ID: return
        if message.embeds: return
        message_content = message.content
        # Sleepy Potion
        search_strings = [
            'has slept for a day', #English
        ]
        if any(search_string in message_content.lower() for search_string in search_strings):
            user_name = user = None
            search_patterns = [
                r'^\*\*(.+?)\*\* drinks', #English
            ]
            user_name_match = await functions.get_match_from_patterns(search_patterns, message_content)
            if user_name_match:
                user_name = await functions.encode_text(user_name_match.group(1))
            else:
                await functions.add_warning_reaction(message)
                await errors.log_error('User not found in sleepy potion message.', message)
                return
            user = await functions.get_guild_member_by_name(message.guild, user_name)
            if user is None:
                await functions.add_warning_reaction(message)
                await errors.log_error('User not found in sleepy potion message.', message)
                return
            try:
                user_settings: users.User = await users.get_user(user.id)
            except exceptions.FirstTimeUserError:
                return
            if not user_settings.bot_enabled: return
            await reminders.reduce_reminder_time(user.id, timedelta(days=1))
            if user_settings.reactions_enabled: await message.add_reaction(emojis.NAVI)


# Initialization
def setup(bot):
    bot.add_cog(SleepyPotionCog(bot))