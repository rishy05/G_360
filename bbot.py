#MTE1MDI5NzUwNjExOTQzMDIyNA.Gb0CGh.DShosnDeg4hO2mQ_A7pOvzS818t_aE1HpNsZgs

from discord.ext import commands
import discord
from discord.ext import commands
import discord
import uuid
import requests
import shutil
from PIL import Image as img
import os
from time import sleep
from g_mail import auth_mail, send_mail
from ps_gen import pass_gen



auth_mail()
intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='CC ', intents=intents)

@client.event
async def on_ready():
    print("ready")


@client.command()
async def verify(ctx): 
    try:
        url = ctx.message.attachments[0].url
    except IndexError:
        print("No fille attached")
        await ctx.channel.send("No file attached")
    else:
        if url[0:26] == "https://cdn.discordapp.com":
            r = requests.get(url, stream=True)
            imgName = str(uuid.uuid4()) + '.jpg'
            with open(imgName, 'wb') as out_file:
                print(f"File saved as {imgName}") 
                shutil.copyfileobj(r.raw, out_file)
                await ctx.channel.send("Verificaton process will start soon.")
                sleep(4)
                await ctx.channel.send(f"Your password is: {pass_gen()}")

            # shutil.move(f'E:\obj_discord\content\yolov5\{imgName}', "E:\obj_discord\content\yolov5\data\imgss")

@client.command()
async def q(ctx, query):
    con = query.split(',')
    print(con)

client.run('MTE1MDI5NzUwNjExOTQzMDIyNA.Gb0CGh.DShosnDeg4hO2mQ_A7pOvzS818t_aE1HpNsZgs')