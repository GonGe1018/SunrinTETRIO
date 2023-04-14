import discord
from discord.ext import commands
import GetUserLB#테트리오 API를 사용하여 사용자 정보를 받아오기
import userDB_manage#DB 관리하기

token=open("token.txt","r").readline()
game=discord.Game(' )help 입력')
bot = commands.Bot(command_prefix=')',intents=discord.Intents.all(),activity=game)

def lbSend(username):#리더보드를 임베드로 반환
    dict = GetUserLB.Get(username)
    if(dict=='no user'):
        embed= discord.Embed(title='유저를 찾을 수 없습니다')
    else:
        embed = discord.Embed(title='**'+dict['name'].upper()+'**님의 리더보드입니다',color=discord.Color.blue())
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1096103445024485488/1096103529506164867/logo.png")
        embed.add_field(name='계정 생성일', value=dict['ts'], inline=False)
        embed.add_field(name='40LINE 최고 기록', value=str(dict['40L']//60)+'분 '+str(dict['40L']%60)+'초', inline=True)
        embed.add_field(name='BLITZ 최고 기록', value=str(dict['blitz']), inline=False)
        embed.add_field(name='LEAGUE 기록',value='', inline=False)
        embed.add_field(name='플레이 횟수', value=str(dict['league']['playeds'])+'회', inline=True)
        embed.add_field(name='이긴 횟수', value=str(dict['league']['wins'])+'회', inline=True)
        embed.add_field(name='RANK', value=str(dict['league']['rank'])+' rank', inline=True)

    return(embed)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()#리더보드 leaderboard
async def lb(ctx, arg):
    await ctx.send(embed=lbSend(arg))

@bot.command()#DB 업로드 register
async def rg(ctx,arg,arg2):
    check=userDB_manage.AddUser((arg,arg2))
    if(check=='no user'):
        await ctx.send('유저가 없습니다.')
    else:
        await ctx.send('사용자 정보가 DB에 업로드 되었습니다')

# @bot.command()
# async def help(ctx)





bot.run(token)