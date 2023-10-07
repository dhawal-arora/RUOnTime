

#cursor.execute("DELETE FROM servers")
#cursor.execute("DELETE FROM votekick")
#cursor.execute("DELETE FROM vip_block")
#mycon.commit()

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

@client.event
async def on_ready():
  print ('We have logged in as {0.user}' .format (client))
  await client.wait_until_ready()
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/dragme"))
  await client.tree.sync()


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
   #await content.response.send_message(content=f"{bhousing.name},{bhousing.value}")
   await content.user.send("HI")
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
                               discord.app_commands.Choice(name="Tinsley Hall", value="C14"),
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

@client.tree.command(name="liviclass", description="Step 2: Enter Class Location and Timings")
@discord.app_commands.choices(liviclasslocation=
                              [discord.app_commands.Choice(name="(BE) Beck Hall", value="1L"),
                               discord.app_commands.Choice(name="(LSH) Lucy Stone Hall", value="2L"),
                               discord.app_commands.Choice(name="(LSH-AUD) Lucy Stone Hall Auditorium", value="3L"),
                               discord.app_commands.Choice(name="(RC) Rutgers Cinema", value="4L"),
                               discord.app_commands.Choice(name="(TIL) Tillett Hall", value="5L"),
                               ])
async def liviclass(content: discord.Interaction, liviclasslocation:discord.app_commands.Choice[str], starttime:str, endtime:str):
   await content.response.send_message(content=f"{liviclasslocation.name},{liviclasslocation.value}")

@client.tree.command(name="collegeaveclass", description="Step 2: Enter Class Location and Timings")
@discord.app_commands.choices(collegeaveclasslocation=
                                [discord.app_commands.Choice(name="(AB) Rutgers Academic Building", value="1C"),
                                discord.app_commands.Choice(name="(BH) Bishop House", value="2C"),
                                discord.app_commands.Choice(name="(CA) Campbell Hall", value="3C"),
                                discord.app_commands.Choice(name="(CI) School of Communication and Information", value="4C"),
                                discord.app_commands.Choice(name="(ED) Graduate School of Education", value="5C"),
                                discord.app_commands.Choice(name="(FH) Frelinghuysen Hall", value="6C"),
                                discord.app_commands.Choice(name="(HC) Honors College", value="7C"),
                                discord.app_commands.Choice(name="(HH) Hardenbergh Hall", value="8C"),
                                discord.app_commands.Choice(name="(MI) Milledoler Hall", value="9C"),
                                discord.app_commands.Choice(name="(MU) Murray Hall", value="10C"),
                                discord.app_commands.Choice(name="(SC) Scott Hall", value="11C"),
                                discord.app_commands.Choice(name="(VD) Van Dyck Hall", value="12C"),
                                discord.app_commands.Choice(name="(VH) Voorhees Hall", value="13C"),
                                discord.app_commands.Choice(name="(ZAM) Zimmerli Art Museum", value="14C"),
                                ])
async def collegeaveclass(content: discord.Interaction, collegeaveclasslocation:discord.app_commands.Choice[str], starttime:str, endtime:str):
    await content.response.send_message(content=f"{collegeaveclasslocation.name},{collegeaveclasslocation.value},{starttime},{endtime}")


@client.tree.command(name="cookdougclass", description="Step 2: Enter Class Location and Timings")
@discord.app_commands.choices(cookdougclasslocation=
                            [discord.app_commands.Choice(name="(ARH) Art History Hall", value="1D"),
                            discord.app_commands.Choice(name="(BIO) Biological Sciences", value="2D"),
                            discord.app_commands.Choice(name="(BL) Blake Hall", value="3D"),
                            discord.app_commands.Choice(name="(BT) Bartlett Hall", value="4D"),
                            discord.app_commands.Choice(name="(CDL) Cook Douglass Lecture Hall", value="5D"),
                            discord.app_commands.Choice(name="(DAV) Davison Hall", value="6D"),
                            discord.app_commands.Choice(name="(FNH) Institute for Food Nutrition & Health", value="7D"),
                            discord.app_commands.Choice(name="(FOR) Foran Hall", value="8D"),
                            discord.app_commands.Choice(name="(FS) Food Science Building", value="9D"),
                            discord.app_commands.Choice(name="(HCK) Hickman Hall", value="10D"),
                            discord.app_commands.Choice(name="(HSB) Heldrich Science Building", value="11D"),
                            discord.app_commands.Choice(name="(LOR) Loree Classroom Building", value="12D"),
                            discord.app_commands.Choice(name="(KLG) Kathleen W Ludwig Global Village Learning Center", value="13D"),
                            discord.app_commands.Choice(name="(RAB) Ruth Adams Building", value="14D"),
                            discord.app_commands.Choice(name="(TH) Thompson Hall", value="15D"),
                            discord.app_commands.Choice(name="(WAL) Waller Hall", value="16D"),
                            ])
async def cookdougclass(content: discord.Interaction, cookdougclasslocation:discord.app_commands.Choice[str], starttime:str, endtime:str):
    await content.response.send_message(content=f"{cookdougclasslocation.name},{cookdougclasslocation.value},{starttime},{endtime}")


client.run(discordtoken)