import discord
from discord import app_commands
from discord.ext import commands

import database

_BUSCH = [
    app_commands.Choice(name="Allen Hall",            value="Allen Hall"),
    app_commands.Choice(name="Barr Hall",             value="Barr Hall"),
    app_commands.Choice(name="BEST Hall",             value="BEST Hall"),
    app_commands.Choice(name="Buell Apartments",      value="Buell Apartments"),
    app_commands.Choice(name="Crosby Suites",         value="Crosby Suites"),
    app_commands.Choice(name="Johnson Apartments",    value="Johnson Apartments"),
    app_commands.Choice(name="Judson Suites",         value="Judson Suites"),
    app_commands.Choice(name="Mattia Hall",           value="Mattia Hall"),
    app_commands.Choice(name="Marvin Apartments",     value="Marvin Apartments"),
    app_commands.Choice(name="McCormick Suites",      value="McCormick Suites"),
    app_commands.Choice(name="Metzger Hall",          value="Metzger Hall"),
    app_commands.Choice(name="Morrow Suites",         value="Morrow Suites"),
    app_commands.Choice(name="Nichols Apartments",    value="Nichols Apartments"),
    app_commands.Choice(name="Richardson Apartments", value="Richardson Apartments"),
    app_commands.Choice(name="Silvers Apartments",    value="Silvers Apartments"),
    app_commands.Choice(name="Thomas",                value="Thomas"),
    app_commands.Choice(name="Winkler Suites",        value="Winkler Suites"),
]

_COLLEGE_AVE = [
    app_commands.Choice(name="Brett Hall",                    value="Brett Hall"),
    app_commands.Choice(name="Campbell Hall",                 value="Campbell Hall"),
    app_commands.Choice(name="Clothier Hall",                 value="Clothier Hall"),
    app_commands.Choice(name="Demarest Hall",                 value="Demarest Hall"),
    app_commands.Choice(name="Frelinghuysen Hall",            value="Frelinghuysen Hall"),
    app_commands.Choice(name="Hardenbergh Hall",              value="Hardenbergh Hall"),
    app_commands.Choice(name="Hegeman Hall",                  value="Hegeman Hall"),
    app_commands.Choice(name="Honors College",                value="Honors College"),
    app_commands.Choice(name="Leupp Hall",                    value="Leupp Hall"),
    app_commands.Choice(name="Mettler Hall",                  value="Mettler Hall"),
    app_commands.Choice(name="Pell Hall",                     value="Pell Hall"),
    app_commands.Choice(name="Sojourner Truth Apartments",    value="Sojourner Truth Apartments"),
    app_commands.Choice(name="Stonier Hall",                  value="Stonier Hall"),
    app_commands.Choice(name="Tinsley Hall",                  value="Tinsley Hall"),
    app_commands.Choice(name="Eastern Ave Apartments",        value="Eastern Ave Apartments"),
    app_commands.Choice(name="Wessels Hall",                  value="Wessels Hall"),
]

_COOK_DOUG = [
    app_commands.Choice(name="Helyar House",               value="Helyar House"),
    app_commands.Choice(name="Henderson Apartments",       value="Henderson Apartments"),
    app_commands.Choice(name="Jameson Hall",               value="Jameson Hall"),
    app_commands.Choice(name="Katzenbach Hall",            value="Katzenbach Hall"),
    app_commands.Choice(name="Lippincott Hall",            value="Lippincott Hall"),
    app_commands.Choice(name="New Gibbons Hall",           value="New Gibbons Hall"),
    app_commands.Choice(name="Newell Apartments",          value="Newell Apartments"),
    app_commands.Choice(name="Nicholas Hall",              value="Nicholas Hall"),
    app_commands.Choice(name="Perry Hall",                 value="Perry Hall"),
    app_commands.Choice(name="Starkey Apartments",         value="Starkey Apartments"),
    app_commands.Choice(name="Voorhees Hall",              value="Voorhees Hall"),
    app_commands.Choice(name="Woodbury Bunting-Cobb Hall", value="Woodbury Bunting-Cobb Hall"),
]

_LIVINGSTON = [
    app_commands.Choice(name="Livingston Apartments", value="Livingston Apartments"),
    app_commands.Choice(name="Lynton Towers North",   value="Lynton Towers North"),
    app_commands.Choice(name="Lynton Towers South",   value="Lynton Towers South"),
    app_commands.Choice(name="Quad 1",                value="Quad 1"),
    app_commands.Choice(name="Quad 2",                value="Quad 2"),
    app_commands.Choice(name="Quad 3",                value="Quad 3"),
]


class HousingCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def _set_housing(self, interaction: discord.Interaction, dorm_name: str) -> None:
        conn = database.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT dorm FROM housing WHERE id = %s", (interaction.user.id,))
        row = cur.fetchone()

        if row is None:
            cur.execute(
                "INSERT INTO housing VALUES (%s, %s, %s)",
                (interaction.user.id, dorm_name, 0),
            )
            conn.commit()
            await interaction.response.send_message(
                f"{dorm_name} saved as your housing. Use `/openschedule` to add classes.",
                ephemeral=True,
            )
        elif row[0] == dorm_name:
            await interaction.response.send_message(
                f"{dorm_name} is already set as your housing.",
                ephemeral=True,
            )
        else:
            cur.execute(
                "UPDATE housing SET dorm = %s WHERE id = %s",
                (dorm_name, interaction.user.id),
            )
            conn.commit()
            await interaction.response.send_message(
                f"Housing updated to {dorm_name}.",
                ephemeral=True,
            )

    @app_commands.command(name="buschhousing", description="Step 1: Set your Busch campus housing")
    @app_commands.choices(building=_BUSCH)
    async def buschhousing(self, interaction: discord.Interaction, building: app_commands.Choice[str]) -> None:
        await self._set_housing(interaction, building.value)

    @app_commands.command(name="collegeavehousing", description="Step 1: Set your College Ave campus housing")
    @app_commands.choices(building=_COLLEGE_AVE)
    async def collegeavehousing(self, interaction: discord.Interaction, building: app_commands.Choice[str]) -> None:
        await self._set_housing(interaction, building.value)

    @app_commands.command(name="cookdoughousing", description="Step 1: Set your Cook-Douglass campus housing")
    @app_commands.choices(building=_COOK_DOUG)
    async def cookdoughousing(self, interaction: discord.Interaction, building: app_commands.Choice[str]) -> None:
        await self._set_housing(interaction, building.value)

    @app_commands.command(name="livihousing", description="Step 1: Set your Livingston campus housing")
    @app_commands.choices(building=_LIVINGSTON)
    async def livihousing(self, interaction: discord.Interaction, building: app_commands.Choice[str]) -> None:
        await self._set_housing(interaction, building.value)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(HousingCog(bot))
