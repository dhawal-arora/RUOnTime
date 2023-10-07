#cursor.execute("DELETE FROM servers")
#cursor.execute("DELETE FROM votekick")
#cursor.execute("DELETE FROM vip_block")
#mycon.commit()

def serverentry(content):
    cursor.execute(f"SELECT * FROM servers WHERE id={content.guild.id}")
    data=cursor.fetchone()
    if data==None:
        #cursor.execute(f"INSERT INTO servers VALUES({content.guild.id},{content.guild.name},\"F\",0,\"F\")")
        #cursor.execute("INSERT INTO table VALUES (%s, %s, %s, %s, %s)", (content.guild.id, content.guild.name, "F",0,"F"))
        cursor.execute("INSERT INTO servers VALUES (%s,%s,%s,%s,%s)", (content.guild.id, content.guild.name, "F", 0, "F"))
        mycon.commit()
    return data

'''
CREATE database dragbot;
Use dragbot;
CREATE TABLE servers(
    id numeric(23) NOT NULL PRIMARY KEY,
    name varchar(100) NOT NULL,
    status varchar (1),
    no_drags integer,
    vk_status varchar(1),
);
CREATE TABLE blocked_vc(
    server_id numeric(23) NOT NULL,
    vc_id numeric(23) NOT NULL,
);
CREATE INDEX blocked_vc_ind1
ON blocked_vc(server_id)

CREATE TABLE vip_block(
    server_id numeric(23) NOT NULL,
    member_id numeric(23) NOT NULL); 

CREATE INDEX vip_block_ind1 
ON vip_block(server_id)

CREATE TABLE votekick (
  server_id numeric(23) NOT NULL,
  vc_id numeric(23) NOT NULL,
  member_id numeric(23) NOT NULL);

ALTER TABLE votekick 
ADD initialize varchar(1);
'''
from typing import Any
import os
import discord
from discord.ext import commands
from discord.interactions import Interaction
from discord.ui.item import Item
import math

client = commands.Bot(command_prefix=['d.'], intents=discord.Intents.all())
client.remove_command("help")

discordtoken = "MTE2MDIyMzU1NzUzNjcxMDczOA.GY-DAy.MR7qmCv8OfcajJIdmHU3eMKNWETO9r-VZiAwu0"

@client.event
async def on_ready():
  print ('We have logged in as {0.user}' .format (client))
  await client.wait_until_ready()
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/dragme"))
  await client.tree.sync()

@client.tree.command(name="help", description="Help command.")
async def help(content: discord.Interaction):
    serverentry(content)
    info="__**Use me to ask for drags or send VC invites!**__\n**Drag users with consent:** /dragme and tag member in slash command tab.\n**Invite users with consent:** /vcinvite and tag member in slash command tab.\n**Vote kick users in the VC (4 or more server members):** /votekick and tag member in slash command tab.(BETA-TESTING)"
    buttons=Empty()
    await content.response.send_message(content=info, view=buttons)

class Empty(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    async def Empty(self,content:discord.Interaction):
        await content.response.send_message(view=self)

@client.tree.command(name="denydrags", description="Specify which VC should not allow drags.")
@discord.app_commands.checks.has_permissions(manage_messages=True, move_members=True)
async def denydrags(content: discord.Interaction, voice:discord.VoiceChannel):
    data=serverentry(content)
    if data[2] == "T":
        cursor.execute(f"SELECT * FROM blocked_vc WHERE server_id={content.guild.id} AND vc_id={voice.id}")
        data=cursor.fetchone()
        if data==None:
            cursor.execute(f"INSERT INTO blocked_vc VALUES({content.guild.id}, {voice.id})")
            mycon.commit()
            await content.response.send_message(content=f"No Drags will be given to {voice.mention}.")
        else:
            await content.response.send_message(content=f"{voice.mention} is already blocked for drags.")
    else:
        await content.response.send_message(content=f"Bot shutdown by Mod. Please turn on first.") 

@denydrags.error
async def on_denydrags_error(interaction: discord.Interaction, error: discord.app_commands.AppCommandError):
    if isinstance(error, discord.app_commands.MissingPermissions):
        await interaction.response.send_message(str(error), ephemeral=True)


@client.tree.command(name="buschhousing", description="Step 1: Enter On-campus Housing Location")
@discord.app_commands.choices(bhousing=
                              [discord.app_commands.Choice(name="Allen Hall", value="B1"),
                               discord.app_commands.Choice(name="Barr Hall", value="B2"),
                               discord.app_commands.Choice(name="BEST Hall", value="B3"),
                               discord.app_commands.Choice(name="Buell Apartments", value="B4"),
                               discord.app_commands.Choice(name="Crosby Suites", value="B5"),
                               discord.app_commands.Choice(name="Johnson Apartments", value="B6"),
                               discord.app_commands.Choice(name="Judson Suites", value="B7"),
                               discord.app_commands.Choice(name="Mattia Hall", value="B8"),
                               discord.app_commands.Choice(name="Marvin Apartments", value="B9"),
                               discord.app_commands.Choice(name="McCormick Suites", value="B10"),
                               discord.app_commands.Choice(name="Metzger Hall", value="B11"),
                               discord.app_commands.Choice(name="Morrow Suites", value="B12"),
                               discord.app_commands.Choice(name="Nichols Apartments", value="B13"),
                               discord.app_commands.Choice(name="Richardson Apartments", value="B14"),
                               discord.app_commands.Choice(name="Silvers Apartments", value="B15"),
                               discord.app_commands.Choice(name="Thomas", value="B16"),
                               discord.app_commands.Choice(name="Winkler Suites", value="B17"),
                               ])
async def buschhousing(content: discord.Interaction, bhousing:discord.app_commands.Choice[str]):
   await content.response.send_message(content=f"{bhousing.name},{bhousing.value}")

@client.tree.command(name="collegeavehousing", description="Step 1: Enter On-campus Housing Location")
@discord.app_commands.choices(chousing=
                              [discord.app_commands.Choice(name="Brett Hall", value="C1"),
                               discord.app_commands.Choice(name="Campbell Hall", value="C2"),
                               discord.app_commands.Choice(name="Clothier Hall", value="C3"),
                               discord.app_commands.Choice(name="Demarest Hall", value="C4"),
                               discord.app_commands.Choice(name="Frelinghuysen Hall", value="C5"),
                               discord.app_commands.Choice(name="Hardenbergh Hall", value="C6"),
                               discord.app_commands.Choice(name="Hegeman Hall", value="C7"),
                               discord.app_commands.Choice(name="Honors College", value="C8"),
                               discord.app_commands.Choice(name="Leupp Hall", value="C9"),
                               discord.app_commands.Choice(name="Mettler Hall", value="C10"),
                               discord.app_commands.Choice(name="Pell Hall", value="C11"),
                               discord.app_commands.Choice(name="Sojourner Truth Apartments", value="C12"),
                               discord.app_commands.Choice(name="Stonier Hall", value="C13"),
                               discord.app_commands.Choice(name="Silvers Apartments", value="C14"),
                               discord.app_commands.Choice(name="Eastern Ave Apartments", value="C15"),
                               discord.app_commands.Choice(name="Wessels Hall", value="C16"),
                               ])
async def collegeavehousing(content: discord.Interaction, chousing:discord.app_commands.Choice[str]):
   await content.response.send_message(content=f"{chousing.name},{chousing.value}")

@client.tree.command(name="cookdoughousing", description="Step 1: Enter On-campus Housing Location")
@discord.app_commands.choices(dhousing=
                              [discord.app_commands.Choice(name="Helyer House", value="D1"),
                               discord.app_commands.Choice(name="Henderson Apartments", value="D2"),
                               discord.app_commands.Choice(name="Jameson Hall", value="D3"),
                               discord.app_commands.Choice(name="Katzenbach Hall", value="D4"),
                               discord.app_commands.Choice(name="Lippincott Hall", value="D5"),
                               discord.app_commands.Choice(name="New Gibbons Hall", value="D6"),
                               discord.app_commands.Choice(name="Newell Apartments", value="D7"),
                               discord.app_commands.Choice(name="Nicholas Hall", value="D8"),
                               discord.app_commands.Choice(name="Perry Hall", value="D9"),
                               discord.app_commands.Choice(name="Starkey Apartments", value="D10"),
                               discord.app_commands.Choice(name="Voorhees Hall", value="D11"),
                               discord.app_commands.Choice(name="Woodbury Bunting-Cobb Hall", value="D12"),
                               ])
async def cookdoughousing(content: discord.Interaction, dhousing:discord.app_commands.Choice[str]):
   await content.response.send_message(content=f"{dhousing.name},{dhousing.value}")

@client.tree.command(name="livihousing", description="Step 1: Enter On-campus Housing Location")
@discord.app_commands.choices(lhousing=
                              [discord.app_commands.Choice(name="Livingston Apartments", value="L1"),
                               discord.app_commands.Choice(name="Lynton Towers North", value="L2"),
                               discord.app_commands.Choice(name="Lynton Towers South", value="L3"),
                               discord.app_commands.Choice(name="Quad 1", value="L4"),
                               discord.app_commands.Choice(name="Quad 2", value="L5"),
                               discord.app_commands.Choice(name="Quad 3", value="L6"),
                               ])
async def livihousing(content: discord.Interaction, lhousing:discord.app_commands.Choice[str]):
   await content.response.send_message(content=f"{lhousing.name},{lhousing.value}")

@client.tree.command(name="buschclass", description="Step 2: Enter Class Location and Timings")
@discord.app_commands.choices(buschclasslocation=
                              [discord.app_commands.Choice(name="(ARC) Allison Road Classroom", value="1B"),
                               discord.app_commands.Choice(name="(BME) Biomedical Engineering Building", value="2B"),
                               discord.app_commands.Choice(name="(BST) BEST West Residence Hall", value="3B"),
                               discord.app_commands.Choice(name="(CCB) Chemistry & Chemical Biology", value="4B"),
                               discord.app_commands.Choice(name="(CoRE) Computing Research & Education Building", value="5B"),
                               discord.app_commands.Choice(name="(EN) Engineering Building", value="6B"),
                               discord.app_commands.Choice(name="(HLL) Hill Center", value="7B"),
                               discord.app_commands.Choice(name="(PH) Pharmacy Building (William Levin Hall)", value="8B"),
                               discord.app_commands.Choice(name="(PHY) Physics Building", value="9B"),
                               discord.app_commands.Choice(name="(RWH) Richard Weeks Hall of Engineering", value="10B"),
                               discord.app_commands.Choice(name="(SEC) Science & Engineering Resource Center (T. Alexander Pond)", value="11B"),
                               discord.app_commands.Choice(name="(WL) Wright Rieman Laboratories", value="12B"),
                               ])
async def buschclass(content: discord.Interaction, buschclasslocation:discord.app_commands.Choice[str], starttime:str, endtime:str):
   await content.response.send_message(content=f"{buschclasslocation.name},{buschclasslocation.value}")

client.run(discordtoken)