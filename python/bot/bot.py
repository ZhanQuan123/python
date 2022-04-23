def start():
    from config import config
    import os
    import discord
    from discord.ext import commands, tasks

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix=config.prefix(), intents=intents)

    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

    @bot.event
    async def on_ready( ):
        print(bot.user.name + " has started.")
        os.chdir('../')


        # dir_path = os.path.dirname(os.path.realpath(__file__))
        # for file in os.listdir(f"{dir_path}/cogs/"): # lists all the cog files inside the cog folder.
        #     if file.endswith(".py"): # It gets all the cogs that ends with a ".py".
        #         name = file[:-3] # It gets the name of the file removing the ".py"
        #         await bot.load_extension(f"commands.{name}") # This loads the cog.

    bot.run(config.token())
