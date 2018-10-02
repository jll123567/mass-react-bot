import discord

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
        await message.channel.send(message.channel, 'hello <:upvote:428244958504550411>')

    if message.content.startswith('m!help'):
        await message.channel.send(message.channel, "```m!startVote | reacts with :up_arrow: and :down_arrow:"
                                                    "to the channel the command is used in (for the last 100 "
                                                    "messages)\n\n "
                                                    "m!removeVote | remove the bot's reacts\n"
                                                    "m!help | this```")

    if message.content.startswith('m!startVote'):
        async for msg in message.channel.history():
            await msg.add_reaction(u"\U0001F44D")
            await msg.add_reaction(u"\U0001F44E")

    if message.content.startswith('m!removeVote'):
        async for msg in message.channel.history():
            await msg.clear_reactions()


client.run('token')
