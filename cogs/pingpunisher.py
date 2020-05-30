import discord
from discord.ext import commands
import logging
logger = logging.getLogger('salc1bot')
automation_logger = logging.getLogger('salc1bot.automated')

# People constantly ping the mods for no reason and they get very angry for the pings
# Now when someone attempts to ping them, they get pinged back! They delete after 30 sec too!
# Can also be disabled/enabled via !togglepunish. People should maybe try to ping just one active mod/a few instead!
# Note: some of this python code might be worse than expected, since I basically only know other languages (It seams to work though!)


class PingPunisher(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Various public channels of the Discord server (not packpng channels)
        self.p_channels = [548308507636662283, 588040378188431486, 436411303351943188, 436410903273930753,
                           699723964225683506, 533701359141257231, 587129065132130304, 715819967164973126]
        self.enabled = True
        # How a mention of the SalC1 moderator role looks like
        self.modRole = "<@&447520420623548428>"

    def isExempt(self, author: discord.User):
        for role in ["Administrator", "Moderator", "Private Chat Access"]:
            if role in map(str, author.roles):
                return True
        return False

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.modRole in message.content and self.enabled and (not self.isExempt(message.author)):
            for channelid in self.p_channels:
                channel = self.bot.get_channel(channelid)
                await channel.send(message.author.mention, delete_after=30)
            # Inform of the punishment, note: I dont know if this channel still exists on the server, I *currently* dont have the means to check
            automation_logger.info(
                f"Ping punishment triggered by user {message.author} ({message.author.id}) in {message.channel.name}")

    @commands.has_any_role("Moderator", "Administrator")
    @commands.command(name='togglepunish')
    async def togglePunishment(self, ctx):
        self.enabled = not self.enabled
        await ctx.send(f"Toggled punishment responses to {self.enabled}")


def setup(bot):
    bot.add_cog(PingPunisher(bot))
