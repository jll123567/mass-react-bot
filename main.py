import discord
import asyncio

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('m!test'):
        await client.send_message(message.channel, 'hello <:upvote:428244958504550411>')

    if message.content.startswith('m!startVote'):
        async for log in client.logs_from(message.channel, limit=100):
            await client.add_reaction(log, '⬆️')
            await client.add_reaction(log, '⬇️')

    if message.content.startswith('m!removeVote'):
        async for log in client.logs_from(message.channel, limit=100):
            await client.remove_reaction(log, '⬆', client.user)
            await client.remove_reaction(log, '⬇️', client.user)

client.run('token')
