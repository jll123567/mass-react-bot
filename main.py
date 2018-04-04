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

    if message.content.startswith('m!help'):
        await client.send_message(message.channel, "```m!startVote | reacts with :up_arrow: and :down_arrow:"
                                                   " to the channel the command is used in (for the last 100 messages)\n\n"
                                                   "m!removeVote | remove the bot's reacts\n"
                                                   "m!help | this```")


    if message.content.startswith('m!startVote'):
        async for log in client.logs_from(message.channel, limit=100):
            await client.add_reaction(log, u"\U0001F44D")
            await client.add_reaction(log, u"\U0001F44E")

    if message.content.startswith('m!removeVote'):
        async for log in client.logs_from(message.channel, limit=200):
            await client.remove_reaction(log, u"\U0001F44D", client.user)
            await client.remove_reaction(log, u"\U0001F44E", client.user)

client.run('token')
