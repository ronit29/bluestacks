import os

import discord
from discord.ext import commands
import stacks_config as cnf, google, storage as strg

TOKEN = cnf.DISCORD_TOKEN

'''Intializing Bot with command '''
bot = commands.Bot(command_prefix='!')

'''
INPUT
    -command_name: String to respond
'''
@bot.command(name='hi', help='Responds to HI Message.')
async def handle_message(rsp):
    response = 'hey'
    await rsp.send(response)

'''
INPUT
    -query: String to search
Queries google Data using Google Search library and returns top 5 results
'''
@bot.command(name='google', help='Queries Google to display results.')
async def handle_google_search(rsp, query: str):
    response = ''
    for result in google.get_google_response(query):
        response += str(result) + '\n '
    if response:
        db.write(query)
    await rsp.send(response)

'''
INPUT
    -query: String to search
Retrieves Searched google Data from storage and returns results
'''
@bot.command(name='recent', help='Searches Recent Google searches to display results.')
async def handle_google_search(rsp, query: str):
    response = ''
    data = db.read()
    res = list(filter(lambda item: query in item[0], data.items()))
    for tups in res:
        response += tups[0] + '\n'
    if not response:
        response = "No Data Found in History"
    await rsp.send(response)



if __name__ == '__main__':
    db = strg.Storage()
    bot.run(TOKEN)