import asyncio
import discord

from redbot.core import Config, checks, commands
from redbot.core.bot import Red

class SauriCogs(commands.Cog):
    """
    Change various settings in other SauriCogs that are not otherwise accessible.
    """

    __author__ = "saurichable"
    __version__ = "0.0.1"

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(
            self, identifier=95603285604366, force_registration=True
        )
        self.config.register_global(
            advanced_lock={},
            application={},
            cookies={},
            cookie_store={},
            counting={},
            economy_raffle={},
            forwarding={},
            gallery={},
            lock={},
            lvlup_cookies={},
            marriage={},
            mentionable={},
            pick={},
            pingable={},
            suggestion={},
            unique_name={},
            user_log={},
        )

    @commands.group(autohelp=True)
    @commands.is_owner()
    async def sauricogs(self, ctx):
        """Various SauriCogs settings."""
        pass

    @sauricogs.group(autohelp=True)
    async def advancedlock(self, ctx):
        """Various SauriCogs settings."""
        pass

    @advancedlock.command(name="lock")
    async def advancedlock_lock(self, ctx: commands.Context):