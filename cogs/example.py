import discord
from discord.ext import commands


class mod(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.command()
    async def ping(self, ctx):
     await ctx.send(self.bot.latency*1000)

async def setup(bot):
 await bot.add_cog(mod(bot))
