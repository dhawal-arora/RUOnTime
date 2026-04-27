import datetime

import discord
from discord import app_commands
from discord.ext import commands

import database
import report


class ScheduleCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="help", description="How to use RU On Time")
    async def help(self, interaction: discord.Interaction) -> None:
        embed = discord.Embed(
            title="RU On Time",
            description=(
                "**Step 1 — Set your on-campus housing**\n"
                "`/buschhousing` `/livihousing` `/collegeavehousing` `/cookdoughousing`\n\n"
                "**Step 2 — Open your schedule**\n"
                "`/openschedule`\n\n"
                "**Step 3 — Add your classes**\n"
                "`/buschclass` `/liviclass` `/collegeaveclass` `/cookdougclass`\n\n"
                "**Step 4 — Submit your schedule**\n"
                "`/closeschedule`\n\n"
                "**Step 5 — Get today's bus report**\n"
                "`/busreport`\n\n"
                "**Other commands**\n"
                "`/deletehousing` — Remove stored housing\n"
                "`/deleteschedule` — Remove stored schedule"
            ),
            color=0x00FF00,
        )
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="openschedule", description="Start entering your class schedule")
    async def openschedule(self, interaction: discord.Interaction) -> None:
        conn = database.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT scheduleopen FROM housing WHERE id = %s", (interaction.user.id,))
        row = cur.fetchone()

        if row is None:
            await interaction.response.send_message(
                "Add your dorm first using a housing command (Step 1).",
                ephemeral=True,
            )
        elif row[0] == 1:
            await interaction.response.send_message(
                "Already in class-adding mode. Use a campus class command (Step 2).",
                ephemeral=True,
            )
        else:
            cur.execute("UPDATE housing SET scheduleopen = 1 WHERE id = %s", (interaction.user.id,))
            conn.commit()
            await interaction.response.send_message("Schedule opened. Add your classes now.")

    @app_commands.command(name="closeschedule", description="Submit your final class schedule")
    async def closeschedule(self, interaction: discord.Interaction) -> None:
        conn = database.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT scheduleopen FROM housing WHERE id = %s", (interaction.user.id,))
        row = cur.fetchone()

        if row is None:
            await interaction.response.send_message(
                "Add your dorm first using a housing command (Step 1).",
                ephemeral=True,
            )
        elif row[0] == 0:
            await interaction.response.send_message("Schedule is already closed.", ephemeral=True)
        else:
            cur.execute("UPDATE housing SET scheduleopen = 0 WHERE id = %s", (interaction.user.id,))
            conn.commit()
            await interaction.response.send_message("Schedule submitted.")

    @app_commands.command(name="deleteschedule", description="Delete your stored class schedule")
    async def deleteschedule(self, interaction: discord.Interaction) -> None:
        conn = database.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM housing WHERE id = %s", (interaction.user.id,))
        if cur.fetchone() is None:
            await interaction.response.send_message(
                "No housing on record. Add your dorm first (Step 1).",
                ephemeral=True,
            )
            return
        cur.execute("DELETE FROM classes WHERE id = %s", (interaction.user.id,))
        conn.commit()
        await interaction.response.send_message("Schedule deleted.", ephemeral=True)

    @app_commands.command(name="deletehousing", description="Delete your stored housing information")
    async def deletehousing(self, interaction: discord.Interaction) -> None:
        conn = database.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM housing WHERE id = %s", (interaction.user.id,))
        if cur.fetchone() is None:
            await interaction.response.send_message("No housing on record.", ephemeral=True)
            return
        cur.execute("DELETE FROM housing WHERE id = %s", (interaction.user.id,))
        conn.commit()
        await interaction.response.send_message("Housing deleted.", ephemeral=True)

    @app_commands.command(name="busreport", description="Get today's bus report for your classes")
    async def busreport(self, interaction: discord.Interaction) -> None:
        today = datetime.datetime.now().strftime("%A")
        result = report.check_class_timings(interaction.user.id, today)

        if "error" in result:
            await interaction.response.send_message(result["error"], ephemeral=True)
            return

        classes = result.get("classes", [])
        if not classes:
            await interaction.response.send_message(
                f"No classes scheduled for {today}.",
                ephemeral=True,
            )
            return

        lines = []
        for cls in classes:
            lines.append(f"**{cls['Class Name']}** — {cls['Location']}")
            lines.append(f"Time: {cls['Start Time']} – {cls['End Time']} | Closest stop: {cls['Closest Bus Stop']}")

            if "Bus Timings" in cls:
                for bus in cls["Bus Timings"]:
                    eta = bus["ETA"].strftime("%H:%M")
                    lines.append(f"  {bus['Bus Number']} arrives at {eta} ({bus['Load Percentage']}% full)")

            if "Estimated Arrival" in cls:
                lines.append(f"  Estimated arrival at class: **{cls['Estimated Arrival']}**")

            lines.append("")

        embed = discord.Embed(
            title=f"RU On Time — {today}",
            description="\n".join(lines),
            color=0x00FF00,
        )
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ScheduleCog(bot))
