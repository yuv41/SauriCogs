from .sauricogs import SauriCogs


def setup(bot):
    bot.add_cog(SauriCogs(bot))