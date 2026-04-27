import asyncio
import discord
from discord.ext import commands

import config
import database


class RUOnTimeBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix="d.",
            intents=discord.Intents.all(),
            help_command=None,
        )

    async def setup_hook(self) -> None:
        await self.load_extension("cogs.housing")
        await self.load_extension("cogs.schedule")
        await self.load_extension("cogs.classes")
        await self.tree.sync()

    async def on_ready(self) -> None:
        print(f"Logged in as {self.user}")
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name="/busreport",
            )
        )


async def main() -> None:
    conn = database.get_connection()
    if conn.is_connected():
        print("Connected to MySQL")

    bot = RUOnTimeBot()
    async with bot:
        await bot.start(config.DISCORD_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
