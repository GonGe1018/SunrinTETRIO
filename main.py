import discord
from discord.ui import Button, View
from discord.ext import commands
from discord.utils import get
import json
from discord.ext import commands
import GetLB#테트리오 API를 사용하여 사용자 정보를 받아오기
import manageDB#DB 관리하기
import requests

token=open("token.txt","r").readline()
game=discord.Game(' )도움 입력')
bot = commands.Bot(command_prefix=')',intents=discord.Intents.all(),activity=game)

def lbSend(username, ctx):#리더보드를 임베드로 반환
    _dict = GetLB.Get(username)
    if(_dict=='no user'):
        embed= discord.Embed(title='유저를 찾을 수 없습니다')
    else:
        embed = discord.Embed(title='**'+_dict['name'].upper()+'**님의 리더보드입니다',color=discord.Color.blue())
        img_url='https://tetr.io/user-content/avatars/'+_dict['_id']+'.jpg'
        if('<Response [404]>'==str(requests.get(img_url))):
            img_url='https://media.discordapp.net/attachments/1096103445024485488/1096103529506164867/logo.png'
        embed.set_thumbnail(url=img_url)
        embed.add_field(name='계정 생성일', value=_dict['ts'], inline=False)
        embed.add_field(name='40LINE 최고 기록', value=str(_dict['40L']//60)+'분 '+str(_dict['40L']%60)+'초', inline=True)
        embed.add_field(name='BLITZ 최고 기록', value=str(_dict['blitz']), inline=False)
        embed.add_field(name='LEAGUE 기록',value='', inline=False)
        embed.add_field(name='플레이 횟수', value=str(_dict['league']['playeds'])+'회', inline=True)
        embed.add_field(name='이긴 횟수', value=str(_dict['league']['wins'])+'회', inline=True)
        embed.add_field(name='RANK', value=str(_dict['league']['rank'])+' rank', inline=True)
        
    return(embed)

def helpSend():
    embed = discord.Embed(title='**SunrinTETRIO**에서 사용할 수 있는 명령어들 입니다',color=discord.Color.blue())
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1096103445024485488/1096103529506164867/logo.png")
    embed.add_field(name='`)추가 [사용자 이름] [게임 닉네임]`', value='DB에 사용자 정보를 업로드 합니다', inline=False)
    embed.add_field(name='`)리더보드 [게임 닉네임]`', value='게임 리더보드를 간략화하여 출력합니다', inline=False)
    embed.add_field(name='`)순위 [페이지 번호(기본:1)]`', value='선린고의 학생들의 40L기록을 순위로 나열하여 출력 합니다', inline=False)

    return(embed)

def rankSend(pageNum):
    userDB=open(file='./DB/userDB.json',mode='r',encoding="UTF-8").read()
    _dict = json.loads(userDB)
    rankLi=manageDB.updateRank()
    embed = discord.Embed(title='선린인고 학생들의 40L 순위입니다.',color=discord.Color.blue())
    
    for i in range(pageNum*5,pageNum*5+5):
        userCode=rankLi[i][0]
        userRecord=rankLi[i][1]
        embed.add_field(name=str(i+1)+'위', value=_dict[userCode]['name']+'('+_dict[userCode]['nick']+') '+str(userRecord//60)+'분'+str(userRecord%60)+'초', inline=False)
    
    return(embed)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()#리더보드 leaderboard
async def 리더보드(ctx, arg):

    await ctx.send(embed=lbSend(arg, ctx))

@bot.command()#DB 업로드 register
async def 추가(ctx,arg,arg2):
    check=manageDB.AddUser((arg,arg2.lower()))
    if(check=='no user'):
        await ctx.send('유저가 없습니다.')
    elif(check=='overlap user'):
        await ctx.send('이미 추가된 유저입니다')    
    else:
        await ctx.send('사용자 정보가 DB에 업로드 되었습니다')

@bot.command()
async def 순위(ctx,arg=0):
    try:
        if(int(arg)<=0):
            pageNum=0
        else:
            pageNum=int(arg)-1
    except:
        pageNum=0

    await ctx.send(embed=rankSend(pageNum))

@bot.command()
async def 도움(ctx):
    await ctx.send(embed=helpSend())



bot.run(token)