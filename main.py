
#cursor.execute("CREATE TABLE classes(id numeric(23) NOT NULL,location varchar (500) NOT NULL,classname varchar (500) NOT NULL, starttime TIME, endtime TIME );")

def housingentry(content,dorm):
    cursor.execute(f"SELECT * FROM housing WHERE id={content.user.id}")
    data=cursor.fetchone()
    if data==None:
        #cursor.execute(f"INSERT INTO servers VALUES({content.guild.id},{content.guild.name},\"F\",0,\"F\")")
        #cursor.execute("INSERT INTO table VALUES (%s, %s, %s, %s, %s)", (content.guild.id, content.guild.name, "F",0,"F"))
        cursor.execute("INSERT INTO housing VALUES (%s,%s,%s)", (content.user.id, dorm.name, 0))
        mycon.commit()
    return data

def support(buttons):
    buttons.add_item(discord.ui.Button(label="Invite Bot",style=discord.ButtonStyle.link,url="https://discord.com/api/oauth2/authorize?client_id=1119329341671747584&permissions=2164329472&scope=bot"))
    buttons.add_item(discord.ui.Button(label="Support Server",style=discord.ButtonStyle.link,url="https://discord.gg/Se4VW4Vcey"))
    buttons.add_item(discord.ui.Button(label="Write Review",style=discord.ButtonStyle.link,url="https://top.gg/bot/1119329341671747584#reviews"))

#cursor.execute("DELETE FROM servers")
#cursor.execute("DELETE FROM votekick")
#cursor.execute("DELETE FROM vip_block")
#mycon.commit()

'''
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
import datetime
from discord.ext import tasks
import pytz

client = commands.Bot(command_prefix=['d.'], intents=discord.Intents.all())
client.remove_command("help")

@client.event
async def on_ready():
  print ('We have logged in as {0.user}' .format (client))
  await client.wait_until_ready()
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/busreport"))
  await client.tree.sync()



@client.tree.command(name="help", description="Help command.")
async def help(content: discord.Interaction):
    myEmbed = discord.Embed(title="RU On Time", description="I help save your time..\n\n</buschhousing:1160279628703862784>: Ask for a drag.\n</livihousing:1160291767032221708>: Invite a member to the VC.\n</votekick:1128508073733017734>: Vote kick users in the VC.\n</setup:1123342867126026370>: Bot setup commands.", color=0x00ff00)
    buttons=Empty()
    support(buttons)
    await client.response.send_message(embed=myEmbed, view=buttons)

class Empty(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    async def Empty(self,content:discord.Interaction):
        await content.response.send_message(view=self)

'''
est = pytz.timezone("eastern")
now= datetime.datetime.now(tz=est)
print(now)

# If no tzinfo is given then UTC is assumed.
time = datetime.time(hour=8, minute=30, tzinfo=utc)

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.my_task.start()

    def cog_unload(self):
        self.my_task.cancel()

    @tasks.loop(time=time)
    async def my_task(self):
        print("My task is running!")          

'''
#----------------HOUSING--------------------------------------------

@client.tree.command(name="buschhousing", description="Step 1: Enter On-campus Housing Location")
@discord.app_commands.choices(buschhousing=
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
async def buschhousing(content: discord.Interaction, buschhousing:discord.app_commands.Choice[str]):
   housingentry(content, buschhousing)
   await content.response.send_message(content=f"{buschhousing.name} has been added as your housing. Use /createschedule to add classes.", ephemeral=True)


@client.tree.command(name="collegeavehousing", description="Step 1: Enter On-campus Housing Location")
@discord.app_commands.choices(collegeavehousing=
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
async def collegeavehousing(content: discord.Interaction, collegeavehousing:discord.app_commands.Choice[str]):
   housingentry(content, collegeavehousing)
   await content.response.send_message(content=f"{collegeavehousing.name} has been added as your housing. Use /createschedule to add classes.", ephemeral=True)

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
   housingentry(content, dhousing)
   await content.response.send_message(content=f"{dhousing.name} has been added as your housing. Use /createschedule to add classes.", ephemeral=True)

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
   housingentry(content, lhousing)
   await content.response.send_message(content=f"{lhousing.name} has been added as your housing. Use /createschedule to add classes.", ephemeral=True)

#--------------------REGULAR COMMANDS--------------------------------

@client.tree.command(name="startschedule", description="Start making your one time schedule")
async def startschedule(content: discord.Interaction):
    cursor.execute(f"SELECT * FROM housing WHERE id={content.user.id}")
    data=cursor.fetchone()
    if data==None:
        await content.response.send_message(content="Add On-Campus Dorm First (Step:1)", ephemeral=True)
    elif data[2]==1:
        await content.response.send_message(content="Already in adding class mode. Use relevant command (Step:2)", ephemeral=True)
    elif data[2]==0:
        cursor.execute(f"UPDATE housing SET scheduleopen=1 WHERE id={content.user.id}")
        mycon.commit()
        await content.response.send_message(content="Now in class adding mode.")

@startschedule.error
async def on_shutdown_error(interaction: discord.Interaction, error: discord.app_commands.AppCommandError):
    if isinstance(error, discord.app_commands.MissingPermissions):
        await interaction.response.send_message(str(error), ephemeral=True)


@client.tree.command(name="closeschedule", description="Submit Final Schedule")
async def closeschedule(content: discord.Interaction):
    cursor.execute(f"SELECT * FROM housing WHERE id={content.user.id}")
    data=cursor.fetchone()
    print(data)
    if data==None:
        await content.response.send_message(content="Add On-Campus Dorm First (Step:1)", ephemeral=True)
    elif data[2]==1:
        cursor.execute(f"UPDATE housing SET scheduleopen=0 WHERE id={content.user.id}")
        mycon.commit()
        await content.response.send_message(content="Schedule submitted.")
    elif data[2]==0:
        await content.response.send_message(content="Already closed.", ephemeral=True)

@closeschedule.error
async def on_shutdown_error(interaction: discord.Interaction, error: discord.app_commands.AppCommandError):
    if isinstance(error, discord.app_commands.MissingPermissions):
        await interaction.response.send_message(str(error), ephemeral=True)


#----------------------CLASSES-----------------------------------

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
@discord.app_commands.choices(starthour=
                              [discord.app_commands.Choice(name=0, value=0),
                               discord.app_commands.Choice(name=1, value=1),
                               discord.app_commands.Choice(name=2, value=2),
                               discord.app_commands.Choice(name=3, value=3),
                               discord.app_commands.Choice(name=4, value=4),
                               discord.app_commands.Choice(name=5, value=5),
                               discord.app_commands.Choice(name=6, value=6),
                               discord.app_commands.Choice(name=7, value=7),
                               discord.app_commands.Choice(name=8, value=8),
                               discord.app_commands.Choice(name=9, value=9),
                               discord.app_commands.Choice(name=10, value=10),
                               discord.app_commands.Choice(name=11, value=11),
                               discord.app_commands.Choice(name=12, value=12),
                               discord.app_commands.Choice(name=13, value=13),
                               discord.app_commands.Choice(name=14, value=14),
                               discord.app_commands.Choice(name=15, value=15),
                               discord.app_commands.Choice(name=16, value=16),
                               discord.app_commands.Choice(name=17, value=17),
                               discord.app_commands.Choice(name=18, value=18),
                               discord.app_commands.Choice(name=19, value=19),
                               discord.app_commands.Choice(name=20, value=20),
                               discord.app_commands.Choice(name=21, value=21),
                               discord.app_commands.Choice(name=22, value=22),
                               discord.app_commands.Choice(name=23, value=23),
                               discord.app_commands.Choice(name=24, value=24),
                               ])

@discord.app_commands.choices(startminute=
                              [discord.app_commands.Choice(name=00, value=00),
                               discord.app_commands.Choice(name=5, value=12),
                               discord.app_commands.Choice(name=10, value=13),
                               discord.app_commands.Choice(name=15, value=14),
                               discord.app_commands.Choice(name=20, value=15),
                               discord.app_commands.Choice(name=25, value=16),
                               discord.app_commands.Choice(name=30, value=17),
                               discord.app_commands.Choice(name=35, value=18),
                               discord.app_commands.Choice(name=40, value=19),
                               discord.app_commands.Choice(name=45, value=20),
                               discord.app_commands.Choice(name=50, value=21),
                               discord.app_commands.Choice(name=55, value=22),
                               ])
@discord.app_commands.choices(endhour=
                              [discord.app_commands.Choice(name=0, value=0),
                               discord.app_commands.Choice(name=1, value=1),
                               discord.app_commands.Choice(name=2, value=2),
                               discord.app_commands.Choice(name=3, value=3),
                               discord.app_commands.Choice(name=4, value=4),
                               discord.app_commands.Choice(name=5, value=5),
                               discord.app_commands.Choice(name=6, value=6),
                               discord.app_commands.Choice(name=7, value=7),
                               discord.app_commands.Choice(name=8, value=8),
                               discord.app_commands.Choice(name=9, value=9),
                               discord.app_commands.Choice(name=10, value=10),
                               discord.app_commands.Choice(name=11, value=11),
                               discord.app_commands.Choice(name=12, value=12),
                               discord.app_commands.Choice(name=13, value=13),
                               discord.app_commands.Choice(name=14, value=14),
                               discord.app_commands.Choice(name=15, value=15),
                               discord.app_commands.Choice(name=16, value=16),
                               discord.app_commands.Choice(name=17, value=17),
                               discord.app_commands.Choice(name=18, value=18),
                               discord.app_commands.Choice(name=19, value=19),
                               discord.app_commands.Choice(name=20, value=20),
                               discord.app_commands.Choice(name=21, value=21),
                               discord.app_commands.Choice(name=22, value=22),
                               discord.app_commands.Choice(name=23, value=23),
                               discord.app_commands.Choice(name=24, value=24),
                               ])

@discord.app_commands.choices(endminute=
                              [discord.app_commands.Choice(name=00, value=00),
                               discord.app_commands.Choice(name=5, value=12),
                               discord.app_commands.Choice(name=10, value=13),
                               discord.app_commands.Choice(name=15, value=14),
                               discord.app_commands.Choice(name=20, value=15),
                               discord.app_commands.Choice(name=25, value=16),
                               discord.app_commands.Choice(name=30, value=17),
                               discord.app_commands.Choice(name=35, value=18),
                               discord.app_commands.Choice(name=40, value=19),
                               discord.app_commands.Choice(name=45, value=20),
                               discord.app_commands.Choice(name=50, value=21),
                               discord.app_commands.Choice(name=55, value=22),
                               ])
async def buschclass(content: discord.Interaction, buschclasslocation:discord.app_commands.Choice[str], classname: str, starthour:discord.app_commands.Choice[int], startminute:discord.app_commands.Choice[int], endhour:discord.app_commands.Choice[int], endminute:discord.app_commands.Choice[int]):
    cursor.execute(f"SELECT * FROM housing WHERE id={content.user.id}")
    data=cursor.fetchone()
    if data==None:
        await content.response.send_message(content="Please add Dorm first using /housing (Step:1)", ephemeral=True)
    else:
        if datetime.time(starthour.name,startminute.name) < datetime.time(endhour.name,endminute.name):
            cursor.execute("INSERT INTO classes VALUES (%s,%s,%s,%s,%s)", (content.user.id, buschclasslocation.name, classname,datetime.time(starthour.name,startminute.name), datetime.time(endhour.name,endminute.name)))
            mycon.commit()
            await content.response.send_message(content="Class Added. Add Next Class OR End Entering using /closeschedule", ephemeral=True)
        else: 
            await content.response.send_message(content="Start time after end time. Please Try Again.", ephemeral=True)

@client.tree.command(name="liviclass", description="Step 2: Enter Class Location and Timings")
@discord.app_commands.choices(liviclasslocation=
                              [discord.app_commands.Choice(name="(BE) Beck Hall", value="1L"),
                               discord.app_commands.Choice(name="(LSH) Lucy Stone Hall", value="2L"),
                               discord.app_commands.Choice(name="(LSH-AUD) Lucy Stone Hall Auditorium", value="3L"),
                               discord.app_commands.Choice(name="(RC) Rutgers Cinema", value="4L"),
                               discord.app_commands.Choice(name="(TIL) Tillett Hall", value="5L"),
                               ])
@discord.app_commands.choices(starthour=
                              [discord.app_commands.Choice(name=0, value=0),
                               discord.app_commands.Choice(name=1, value=1),
                               discord.app_commands.Choice(name=2, value=2),
                               discord.app_commands.Choice(name=3, value=3),
                               discord.app_commands.Choice(name=4, value=4),
                               discord.app_commands.Choice(name=5, value=5),
                               discord.app_commands.Choice(name=6, value=6),
                               discord.app_commands.Choice(name=7, value=7),
                               discord.app_commands.Choice(name=8, value=8),
                               discord.app_commands.Choice(name=9, value=9),
                               discord.app_commands.Choice(name=10, value=10),
                               discord.app_commands.Choice(name=11, value=11),
                               discord.app_commands.Choice(name=12, value=12),
                               discord.app_commands.Choice(name=13, value=13),
                               discord.app_commands.Choice(name=14, value=14),
                               discord.app_commands.Choice(name=15, value=15),
                               discord.app_commands.Choice(name=16, value=16),
                               discord.app_commands.Choice(name=17, value=17),
                               discord.app_commands.Choice(name=18, value=18),
                               discord.app_commands.Choice(name=19, value=19),
                               discord.app_commands.Choice(name=20, value=20),
                               discord.app_commands.Choice(name=21, value=21),
                               discord.app_commands.Choice(name=22, value=22),
                               discord.app_commands.Choice(name=23, value=23),
                               discord.app_commands.Choice(name=24, value=24),
                               ])

@discord.app_commands.choices(startminute=
                              [discord.app_commands.Choice(name=00, value=00),
                               discord.app_commands.Choice(name=5, value=12),
                               discord.app_commands.Choice(name=10, value=13),
                               discord.app_commands.Choice(name=15, value=14),
                               discord.app_commands.Choice(name=20, value=15),
                               discord.app_commands.Choice(name=25, value=16),
                               discord.app_commands.Choice(name=30, value=17),
                               discord.app_commands.Choice(name=35, value=18),
                               discord.app_commands.Choice(name=40, value=19),
                               discord.app_commands.Choice(name=45, value=20),
                               discord.app_commands.Choice(name=50, value=21),
                               discord.app_commands.Choice(name=55, value=22),
                               ])
@discord.app_commands.choices(endhour=
                              [discord.app_commands.Choice(name=0, value=0),
                               discord.app_commands.Choice(name=1, value=1),
                               discord.app_commands.Choice(name=2, value=2),
                               discord.app_commands.Choice(name=3, value=3),
                               discord.app_commands.Choice(name=4, value=4),
                               discord.app_commands.Choice(name=5, value=5),
                               discord.app_commands.Choice(name=6, value=6),
                               discord.app_commands.Choice(name=7, value=7),
                               discord.app_commands.Choice(name=8, value=8),
                               discord.app_commands.Choice(name=9, value=9),
                               discord.app_commands.Choice(name=10, value=10),
                               discord.app_commands.Choice(name=11, value=11),
                               discord.app_commands.Choice(name=12, value=12),
                               discord.app_commands.Choice(name=13, value=13),
                               discord.app_commands.Choice(name=14, value=14),
                               discord.app_commands.Choice(name=15, value=15),
                               discord.app_commands.Choice(name=16, value=16),
                               discord.app_commands.Choice(name=17, value=17),
                               discord.app_commands.Choice(name=18, value=18),
                               discord.app_commands.Choice(name=19, value=19),
                               discord.app_commands.Choice(name=20, value=20),
                               discord.app_commands.Choice(name=21, value=21),
                               discord.app_commands.Choice(name=22, value=22),
                               discord.app_commands.Choice(name=23, value=23),
                               discord.app_commands.Choice(name=24, value=24),
                               ])

@discord.app_commands.choices(endminute=
                              [discord.app_commands.Choice(name=00, value=00),
                               discord.app_commands.Choice(name=5, value=12),
                               discord.app_commands.Choice(name=10, value=13),
                               discord.app_commands.Choice(name=15, value=14),
                               discord.app_commands.Choice(name=20, value=15),
                               discord.app_commands.Choice(name=25, value=16),
                               discord.app_commands.Choice(name=30, value=17),
                               discord.app_commands.Choice(name=35, value=18),
                               discord.app_commands.Choice(name=40, value=19),
                               discord.app_commands.Choice(name=45, value=20),
                               discord.app_commands.Choice(name=50, value=21),
                               discord.app_commands.Choice(name=55, value=22),
                               ])
async def liviclass(content: discord.Interaction, liviclasslocation:discord.app_commands.Choice[str], classname: str, starthour:discord.app_commands.Choice[int], startminute:discord.app_commands.Choice[int], endhour:discord.app_commands.Choice[int], endminute:discord.app_commands.Choice[int]):
    cursor.execute(f"SELECT * FROM housing WHERE id={content.user.id}")
    data=cursor.fetchone()
    if data==None:
        await content.response.send_message(content="Please add Dorm first using /housing (Step:1)", ephemeral=True)
    else:
        if datetime.time(starthour.name,startminute.name) < datetime.time(endhour.name,endminute.name):
            cursor.execute("INSERT INTO classes VALUES (%s,%s,%s,%s,%s)", (content.user.id, liviclasslocation.name, classname,datetime.time(starthour.name,startminute.name), datetime.time(endhour.name,endminute.name)))
            mycon.commit()
            await content.response.send_message(content="Class Added. Add Next Class OR End Entering using /closeschedule", ephemeral=True)
        else: 
            await content.response.send_message(content="Start time after end time. Please Try Again.", ephemeral=True)


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
@discord.app_commands.choices(starthour=
                              [discord.app_commands.Choice(name=0, value=0),
                               discord.app_commands.Choice(name=1, value=1),
                               discord.app_commands.Choice(name=2, value=2),
                               discord.app_commands.Choice(name=3, value=3),
                               discord.app_commands.Choice(name=4, value=4),
                               discord.app_commands.Choice(name=5, value=5),
                               discord.app_commands.Choice(name=6, value=6),
                               discord.app_commands.Choice(name=7, value=7),
                               discord.app_commands.Choice(name=8, value=8),
                               discord.app_commands.Choice(name=9, value=9),
                               discord.app_commands.Choice(name=10, value=10),
                               discord.app_commands.Choice(name=11, value=11),
                               discord.app_commands.Choice(name=12, value=12),
                               discord.app_commands.Choice(name=13, value=13),
                               discord.app_commands.Choice(name=14, value=14),
                               discord.app_commands.Choice(name=15, value=15),
                               discord.app_commands.Choice(name=16, value=16),
                               discord.app_commands.Choice(name=17, value=17),
                               discord.app_commands.Choice(name=18, value=18),
                               discord.app_commands.Choice(name=19, value=19),
                               discord.app_commands.Choice(name=20, value=20),
                               discord.app_commands.Choice(name=21, value=21),
                               discord.app_commands.Choice(name=22, value=22),
                               discord.app_commands.Choice(name=23, value=23),
                               discord.app_commands.Choice(name=24, value=24),
                               ])

@discord.app_commands.choices(startminute=
                              [discord.app_commands.Choice(name=00, value=00),
                               discord.app_commands.Choice(name=5, value=12),
                               discord.app_commands.Choice(name=10, value=13),
                               discord.app_commands.Choice(name=15, value=14),
                               discord.app_commands.Choice(name=20, value=15),
                               discord.app_commands.Choice(name=25, value=16),
                               discord.app_commands.Choice(name=30, value=17),
                               discord.app_commands.Choice(name=35, value=18),
                               discord.app_commands.Choice(name=40, value=19),
                               discord.app_commands.Choice(name=45, value=20),
                               discord.app_commands.Choice(name=50, value=21),
                               discord.app_commands.Choice(name=55, value=22),
                               ])
@discord.app_commands.choices(endhour=
                              [discord.app_commands.Choice(name=0, value=0),
                               discord.app_commands.Choice(name=1, value=1),
                               discord.app_commands.Choice(name=2, value=2),
                               discord.app_commands.Choice(name=3, value=3),
                               discord.app_commands.Choice(name=4, value=4),
                               discord.app_commands.Choice(name=5, value=5),
                               discord.app_commands.Choice(name=6, value=6),
                               discord.app_commands.Choice(name=7, value=7),
                               discord.app_commands.Choice(name=8, value=8),
                               discord.app_commands.Choice(name=9, value=9),
                               discord.app_commands.Choice(name=10, value=10),
                               discord.app_commands.Choice(name=11, value=11),
                               discord.app_commands.Choice(name=12, value=12),
                               discord.app_commands.Choice(name=13, value=13),
                               discord.app_commands.Choice(name=14, value=14),
                               discord.app_commands.Choice(name=15, value=15),
                               discord.app_commands.Choice(name=16, value=16),
                               discord.app_commands.Choice(name=17, value=17),
                               discord.app_commands.Choice(name=18, value=18),
                               discord.app_commands.Choice(name=19, value=19),
                               discord.app_commands.Choice(name=20, value=20),
                               discord.app_commands.Choice(name=21, value=21),
                               discord.app_commands.Choice(name=22, value=22),
                               discord.app_commands.Choice(name=23, value=23),
                               discord.app_commands.Choice(name=24, value=24),
                               ])

@discord.app_commands.choices(endminute=
                              [discord.app_commands.Choice(name=00, value=00),
                               discord.app_commands.Choice(name=5, value=12),
                               discord.app_commands.Choice(name=10, value=13),
                               discord.app_commands.Choice(name=15, value=14),
                               discord.app_commands.Choice(name=20, value=15),
                               discord.app_commands.Choice(name=25, value=16),
                               discord.app_commands.Choice(name=30, value=17),
                               discord.app_commands.Choice(name=35, value=18),
                               discord.app_commands.Choice(name=40, value=19),
                               discord.app_commands.Choice(name=45, value=20),
                               discord.app_commands.Choice(name=50, value=21),
                               discord.app_commands.Choice(name=55, value=22),
                               ])
async def collegeaveclass(content: discord.Interaction, collegeaveclasslocation:discord.app_commands.Choice[str], classname: str, starthour:discord.app_commands.Choice[int], startminute:discord.app_commands.Choice[int], endhour:discord.app_commands.Choice[int], endminute:discord.app_commands.Choice[int]):
    cursor.execute(f"SELECT * FROM housing WHERE id={content.user.id}")
    data=cursor.fetchone()
    if data==None:
        await content.response.send_message(content="Please add Dorm first using /housing (Step:1)", ephemeral=True)
    else:
        if datetime.time(starthour.name,startminute.name) < datetime.time(endhour.name,endminute.name):
            cursor.execute("INSERT INTO classes VALUES (%s,%s,%s,%s,%s)", (content.user.id, collegeaveclasslocation.name, classname,datetime.time(starthour.name,startminute.name), datetime.time(endhour.name,endminute.name)))
            mycon.commit()
            await content.response.send_message(content="Class Added. Add Next Class OR End Entering using /closeschedule", ephemeral=True)
        else: 
            await content.response.send_message(content="Start time after end time. Please Try Again.", ephemeral=True)

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
@discord.app_commands.choices(starthour=
                              [discord.app_commands.Choice(name=0, value=0),
                               discord.app_commands.Choice(name=1, value=1),
                               discord.app_commands.Choice(name=2, value=2),
                               discord.app_commands.Choice(name=3, value=3),
                               discord.app_commands.Choice(name=4, value=4),
                               discord.app_commands.Choice(name=5, value=5),
                               discord.app_commands.Choice(name=6, value=6),
                               discord.app_commands.Choice(name=7, value=7),
                               discord.app_commands.Choice(name=8, value=8),
                               discord.app_commands.Choice(name=9, value=9),
                               discord.app_commands.Choice(name=10, value=10),
                               discord.app_commands.Choice(name=11, value=11),
                               discord.app_commands.Choice(name=12, value=12),
                               discord.app_commands.Choice(name=13, value=13),
                               discord.app_commands.Choice(name=14, value=14),
                               discord.app_commands.Choice(name=15, value=15),
                               discord.app_commands.Choice(name=16, value=16),
                               discord.app_commands.Choice(name=17, value=17),
                               discord.app_commands.Choice(name=18, value=18),
                               discord.app_commands.Choice(name=19, value=19),
                               discord.app_commands.Choice(name=20, value=20),
                               discord.app_commands.Choice(name=21, value=21),
                               discord.app_commands.Choice(name=22, value=22),
                               discord.app_commands.Choice(name=23, value=23),
                               discord.app_commands.Choice(name=24, value=24),
                               ])

@discord.app_commands.choices(startminute=
                              [discord.app_commands.Choice(name=00, value=00),
                               discord.app_commands.Choice(name=5, value=12),
                               discord.app_commands.Choice(name=10, value=13),
                               discord.app_commands.Choice(name=15, value=14),
                               discord.app_commands.Choice(name=20, value=15),
                               discord.app_commands.Choice(name=25, value=16),
                               discord.app_commands.Choice(name=30, value=17),
                               discord.app_commands.Choice(name=35, value=18),
                               discord.app_commands.Choice(name=40, value=19),
                               discord.app_commands.Choice(name=45, value=20),
                               discord.app_commands.Choice(name=50, value=21),
                               discord.app_commands.Choice(name=55, value=22),
                               ])
@discord.app_commands.choices(endhour=
                              [discord.app_commands.Choice(name=0, value=0),
                               discord.app_commands.Choice(name=1, value=1),
                               discord.app_commands.Choice(name=2, value=2),
                               discord.app_commands.Choice(name=3, value=3),
                               discord.app_commands.Choice(name=4, value=4),
                               discord.app_commands.Choice(name=5, value=5),
                               discord.app_commands.Choice(name=6, value=6),
                               discord.app_commands.Choice(name=7, value=7),
                               discord.app_commands.Choice(name=8, value=8),
                               discord.app_commands.Choice(name=9, value=9),
                               discord.app_commands.Choice(name=10, value=10),
                               discord.app_commands.Choice(name=11, value=11),
                               discord.app_commands.Choice(name=12, value=12),
                               discord.app_commands.Choice(name=13, value=13),
                               discord.app_commands.Choice(name=14, value=14),
                               discord.app_commands.Choice(name=15, value=15),
                               discord.app_commands.Choice(name=16, value=16),
                               discord.app_commands.Choice(name=17, value=17),
                               discord.app_commands.Choice(name=18, value=18),
                               discord.app_commands.Choice(name=19, value=19),
                               discord.app_commands.Choice(name=20, value=20),
                               discord.app_commands.Choice(name=21, value=21),
                               discord.app_commands.Choice(name=22, value=22),
                               discord.app_commands.Choice(name=23, value=23),
                               discord.app_commands.Choice(name=24, value=24),
                               ])

@discord.app_commands.choices(endminute=
                              [discord.app_commands.Choice(name=00, value=00),
                               discord.app_commands.Choice(name=5, value=12),
                               discord.app_commands.Choice(name=10, value=13),
                               discord.app_commands.Choice(name=15, value=14),
                               discord.app_commands.Choice(name=20, value=15),
                               discord.app_commands.Choice(name=25, value=16),
                               discord.app_commands.Choice(name=30, value=17),
                               discord.app_commands.Choice(name=35, value=18),
                               discord.app_commands.Choice(name=40, value=19),
                               discord.app_commands.Choice(name=45, value=20),
                               discord.app_commands.Choice(name=50, value=21),
                               discord.app_commands.Choice(name=55, value=22),
                               ])
async def cookdougclass(content: discord.Interaction, cookdougclasslocation:discord.app_commands.Choice[str], classname: str, starthour:discord.app_commands.Choice[int], startminute:discord.app_commands.Choice[int], endhour:discord.app_commands.Choice[int], endminute:discord.app_commands.Choice[int]):
    cursor.execute(f"SELECT * FROM housing WHERE id={content.user.id}")
    data=cursor.fetchone()
    if data==None:
        await content.response.send_message(content="Please add Dorm first using /housing (Step:1)", ephemeral=True)
    else:
        if datetime.time(starthour.name,startminute.name) < datetime.time(endhour.name,endminute.name):
            cursor.execute("INSERT INTO classes VALUES (%s,%s,%s,%s,%s)", (content.user.id, cookdougclasslocation.name, classname,datetime.time(starthour.name,startminute.name), datetime.time(endhour.name,endminute.name)))
            mycon.commit()
            await content.response.send_message(content="Class Added. Add Next Class OR End Entering using /closeschedule", ephemeral=True)
        else: 
            await content.response.send_message(content="Start time after end time. Please Try Again.", ephemeral=True)

client.run(discordtoken)
