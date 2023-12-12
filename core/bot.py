import os
import discord
import jishaku
from discord.ext import commands
import sqlite3
import aiohttp
import threading
import logging

os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
os.environ["JISHAKU_HIDE"] = "True"
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"

logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;129m[\x1b[0m%(asctime)s\x1b[38;5;129m]\x1b[0m -> \x1b[38;5;129m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",)

    
class Bot(commands.AutoShardedBot):
    def __init__(self, *args , **kwargs) -> None:
        super().__init__(sync_commands=True, shard_count=1, case_insensitive=True,command_prefix=".", intents=discord.Intents.all())
        owner_ids = [1033579545254711336,289100850285117460]
        self.owner_ids = owner_ids
        self.remove_command('help')
        self._BotBase__cogs = commands.core._CaseInsensitiveDict()
        self.session = aiohttp.ClientSession()
    
    def dbms(self):
        dbt = threading.Thread(target=self.database_connect)
        dbt.start()
        dbt.join()

    def database_connect(self):
        with sqlite3.connect('db/database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS data (userid INTEGER, username TEXT)''')
        logging.info("Sucessfully Loaded Database (SQLITE3)")
        
    async def on_ready(self) -> None:
        logging.info(f" Sucessfully {(self.user.display_name)} is Loaded.")
        logging.info("All the Systems Are Ready.")

    async def setup_hook(self) -> None:
        await self.load_extension('jishaku')
        logging.info(f"Sucessfully Loaded Jishaku")
        self.dbms()
        for filename in os.listdir('./cogs'):
            try:
                if filename.endswith('.py') and filename not in ['__init__.py']:
                    await self.load_extension(f'cogs.{filename[:-3]}')
                    logging.info(f'Sucessfully Loaded Cog: `{filename[:-3]}`')
            except Exception as e:
                logging.info(e)

    async def on_guild_join(self, guild: discord.Guild) -> None:
        o = guild.owner_id
        us = self.get_user(o)
        if us:
            e = discord.Embed(color=0x2e2e2e, description=f"Thanks for adding me to **{guild.name}**.")
            await us.send(embed=e)
        else:
            logging.info("Problem in Bot.py guildjoin event.")
        
        
    
            

 
 

                    
   
   
   
