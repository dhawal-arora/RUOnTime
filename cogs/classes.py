import datetime

import discord
from discord import app_commands
from discord.ext import commands

import database

# Shared choice lists — defined once, reused across all campus class commands.
_HOURS = [app_commands.Choice(name=h, value=h) for h in range(24)]
_MINUTES = [app_commands.Choice(name=m, value=m) for m in range(0, 60, 5)]
_DAYS = [
    app_commands.Choice(name="Monday",    value="Monday"),
    app_commands.Choice(name="Tuesday",   value="Tuesday"),
    app_commands.Choice(name="Wednesday", value="Wednesday"),
    app_commands.Choice(name="Thursday",  value="Thursday"),
    app_commands.Choice(name="Friday",    value="Friday"),
    app_commands.Choice(name="Saturday",  value="Saturday"),
    app_commands.Choice(name="Sunday",    value="Sunday"),
]

_BUSCH_LOCATIONS = [
    app_commands.Choice(name="(ARC) Allison Road Classroom",                              value="(ARC) Allison Road Classroom"),
    app_commands.Choice(name="(BME) Biomedical Engineering Building",                     value="(BME) Biomedical Engineering Building"),
    app_commands.Choice(name="(BST) BEST West Residence Hall",                            value="(BST) BEST West Residence Hall"),
    app_commands.Choice(name="(CCB) Chemistry & Chemical Biology",                        value="(CCB) Chemistry & Chemical Biology"),
    app_commands.Choice(name="(CoRE) Computing Research & Education Building",            value="(CoRE) Computing Research & Education Building"),
    app_commands.Choice(name="(EN) Engineering Building",                                 value="(EN) Engineering Building"),
    app_commands.Choice(name="(HLL) Hill Center",                                         value="(HLL) Hill Center"),
    app_commands.Choice(name="(PH) Pharmacy Building (William Levin Hall)",               value="(PH) Pharmacy Building (William Levin Hall)"),
    app_commands.Choice(name="(PHY) Physics Building",                                    value="(PHY) Physics Building"),
    app_commands.Choice(name="(RWH) Richard Weeks Hall of Engineering",                   value="(RWH) Richard Weeks Hall of Engineering"),
    app_commands.Choice(name="(SEC) Science & Engineering Resource Center",               value="(SEC) Science & Engineering Resource Center (T. Alexander Pond)"),
    app_commands.Choice(name="(WL) Wright Rieman Laboratories",                           value="(WL) Wright Rieman Laboratories"),
]

_LIVI_LOCATIONS = [
    app_commands.Choice(name="(BE) Beck Hall",                        value="(BE) Beck Hall"),
    app_commands.Choice(name="(LSH) Lucy Stone Hall",                 value="(LSH) Lucy Stone Hall"),
    app_commands.Choice(name="(LSH-AUD) Lucy Stone Hall Auditorium",  value="(LSH-AUD) Lucy Stone Hall Auditorium"),
    app_commands.Choice(name="(RC) Rutgers Cinema",                   value="(RC) Rutgers Cinema"),
    app_commands.Choice(name="(TIL) Tillett Hall",                    value="(TIL) Tillett Hall"),
]

_COLLEGE_AVE_LOCATIONS = [
    app_commands.Choice(name="(AB) Rutgers Academic Building",                value="(AB) Rutgers Academic Building"),
    app_commands.Choice(name="(BH) Bishop House",                             value="(BH) Bishop House"),
    app_commands.Choice(name="(CA) Campbell Hall",                            value="(CA) Campbell Hall"),
    app_commands.Choice(name="(CI) School of Communication and Information",  value="(CI) School of Communication and Information"),
    app_commands.Choice(name="(ED) Graduate School of Education",             value="(ED) Graduate School of Education"),
    app_commands.Choice(name="(FH) Frelinghuysen Hall",                       value="(FH) Frelinghuysen Hall"),
    app_commands.Choice(name="(HC) Honors College",                           value="(HC) Honors College"),
    app_commands.Choice(name="(HH) Hardenbergh Hall",                         value="(HH) Hardenbergh Hall"),
    app_commands.Choice(name="(MI) Milledoler Hall",                          value="(MI) Milledoler Hall"),
    app_commands.Choice(name="(MU) Murray Hall",                              value="(MU) Murray Hall"),
    app_commands.Choice(name="(SC) Scott Hall",                               value="(SC) Scott Hall"),
    app_commands.Choice(name="(VD) Van Dyck Hall",                            value="(VD) Van Dyck Hall"),
    app_commands.Choice(name="(VH) Voorhees Hall",                            value="(VH) Voorhees Hall"),
    app_commands.Choice(name="(ZAM) Zimmerli Art Museum",                     value="(ZAM) Zimmerli Art Museum"),
]

_COOK_DOUG_LOCATIONS = [
    app_commands.Choice(name="(ARH) Art History Hall",                                         value="(ARH) Art History Hall"),
    app_commands.Choice(name="(BIO) Biological Sciences",                                      value="(BIO) Biological Sciences"),
    app_commands.Choice(name="(BL) Blake Hall",                                                value="(BL) Blake Hall"),
    app_commands.Choice(name="(BT) Bartlett Hall",                                             value="(BT) Bartlett Hall"),
    app_commands.Choice(name="(CDL) Cook Douglass Lecture Hall",                               value="(CDL) Cook Douglass Lecture Hall"),
    app_commands.Choice(name="(DAV) Davison Hall",                                             value="(DAV) Davison Hall"),
    app_commands.Choice(name="(FNH) Institute for Food Nutrition & Health",                    value="(FNH) Institute for Food Nutrition & Health"),
    app_commands.Choice(name="(FOR) Foran Hall",                                               value="(FOR) Foran Hall"),
    app_commands.Choice(name="(FS) Food Science Building",                                     value="(FS) Food Science Building"),
    app_commands.Choice(name="(HCK) Hickman Hall",                                             value="(HCK) Hickman Hall"),
    app_commands.Choice(name="(HSB) Heldrich Science Building",                                value="(HSB) Heldrich Science Building"),
    app_commands.Choice(name="(LOR) Loree Classroom Building",                                 value="(LOR) Loree Classroom Building"),
    app_commands.Choice(name="(KLG) Kathleen W Ludwig Global Village Learning Center",         value="(KLG) Kathleen W Ludwig Global Village Learning Center"),
    app_commands.Choice(name="(RAB) Ruth Adams Building",                                      value="(RAB) Ruth Adams Building"),
    app_commands.Choice(name="(TH) Thompson Hall",                                             value="(TH) Thompson Hall"),
    app_commands.Choice(name="(WAL) Waller Hall",                                              value="(WAL) Waller Hall"),
]


class ClassesCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def _add_class(
        self,
        interaction: discord.Interaction,
        location: app_commands.Choice[str],
        classname: str,
        starthour: app_commands.Choice[int],
        startminute: app_commands.Choice[int],
        endhour: app_commands.Choice[int],
        endminute: app_commands.Choice[int],
        day: app_commands.Choice[str],
    ) -> None:
        conn = database.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT scheduleopen FROM housing WHERE id = %s", (interaction.user.id,))
        row = cur.fetchone()

        if row is None:
            await interaction.response.send_message(
                "Add your dorm first using a housing command (Step 1).",
                ephemeral=True,
            )
            return
        if row[0] == 0:
            await interaction.response.send_message(
                "Use `/openschedule` before adding classes.",
                ephemeral=True,
            )
            return

        start_mins = starthour.value * 60 + startminute.value
        end_mins = endhour.value * 60 + endminute.value
        if start_mins >= end_mins:
            await interaction.response.send_message(
                "Start time must be before end time. Please try again.",
                ephemeral=True,
            )
            return

        cur.execute(
            "INSERT INTO classes VALUES (%s, %s, %s, %s, %s, %s)",
            (
                interaction.user.id,
                location.value,
                classname,
                datetime.time(starthour.value, startminute.value),
                datetime.time(endhour.value, endminute.value),
                day.value,
            ),
        )
        conn.commit()
        await interaction.response.send_message(
            "Class added. Add another or use `/closeschedule` when done.",
            ephemeral=True,
        )

    @app_commands.command(name="buschclass", description="Step 2: Add a Busch campus class")
    @app_commands.choices(location=_BUSCH_LOCATIONS, starthour=_HOURS, startminute=_MINUTES, endhour=_HOURS, endminute=_MINUTES, day=_DAYS)
    async def buschclass(self, interaction: discord.Interaction, location: app_commands.Choice[str], classname: str, starthour: app_commands.Choice[int], startminute: app_commands.Choice[int], endhour: app_commands.Choice[int], endminute: app_commands.Choice[int], day: app_commands.Choice[str]) -> None:
        await self._add_class(interaction, location, classname, starthour, startminute, endhour, endminute, day)

    @app_commands.command(name="liviclass", description="Step 2: Add a Livingston campus class")
    @app_commands.choices(location=_LIVI_LOCATIONS, starthour=_HOURS, startminute=_MINUTES, endhour=_HOURS, endminute=_MINUTES, day=_DAYS)
    async def liviclass(self, interaction: discord.Interaction, location: app_commands.Choice[str], classname: str, starthour: app_commands.Choice[int], startminute: app_commands.Choice[int], endhour: app_commands.Choice[int], endminute: app_commands.Choice[int], day: app_commands.Choice[str]) -> None:
        await self._add_class(interaction, location, classname, starthour, startminute, endhour, endminute, day)

    @app_commands.command(name="collegeaveclass", description="Step 2: Add a College Ave campus class")
    @app_commands.choices(location=_COLLEGE_AVE_LOCATIONS, starthour=_HOURS, startminute=_MINUTES, endhour=_HOURS, endminute=_MINUTES, day=_DAYS)
    async def collegeaveclass(self, interaction: discord.Interaction, location: app_commands.Choice[str], classname: str, starthour: app_commands.Choice[int], startminute: app_commands.Choice[int], endhour: app_commands.Choice[int], endminute: app_commands.Choice[int], day: app_commands.Choice[str]) -> None:
        await self._add_class(interaction, location, classname, starthour, startminute, endhour, endminute, day)

    @app_commands.command(name="cookdougclass", description="Step 2: Add a Cook-Douglass campus class")
    @app_commands.choices(location=_COOK_DOUG_LOCATIONS, starthour=_HOURS, startminute=_MINUTES, endhour=_HOURS, endminute=_MINUTES, day=_DAYS)
    async def cookdougclass(self, interaction: discord.Interaction, location: app_commands.Choice[str], classname: str, starthour: app_commands.Choice[int], startminute: app_commands.Choice[int], endhour: app_commands.Choice[int], endminute: app_commands.Choice[int], day: app_commands.Choice[str]) -> None:
        await self._add_class(interaction, location, classname, starthour, startminute, endhour, endminute, day)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ClassesCog(bot))
