import discord
from discord.ext import commands
import GetUserLB

token=open("token.txt","r").readline()

bot = commands.Bot(command_prefix=')',intents=discord.Intents.all())

def LBsend(username):
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

@bot.command()
async def lb(ctx, arg):
    await ctx.send(embed=LBsend(arg))

@bot.command()
async def rg(ctx,arg):
    if(arg=='40L'):
        await ctx.send('asdf')



bot.run(token)