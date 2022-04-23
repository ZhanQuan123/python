def start():
    from config import config
    import os
    import discord
    from discord.ext import commands, tasks
    import asyncio
    import wavelink

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix=config.prefix(), intents=intents)




    @bot.command()
    async def unload(ctx, *, value):
        if ctx.message.author.id =='710499387431845909':
            await bot.remove_cog(value)
            await ctx.send(f"successfully unloaded {value}")

    @bot.command()
    async def load(ctx, *, value):
        if ctx.message.author.id =='710499387431845909':
            await bot.reload_extension(f"bot.cogs.{value}")
            await ctx.send(f"successfully loaded {value}")

        
    @bot.event
    async def on_connect( ):
        for file in os.listdir(f"{os.path.dirname(__file__)}\cogs"):
            if file.endswith(".py"):
                name = file[:-3]
                print(f"loaded extension {name}.")
                await bot.load_extension(f"bot.cogs.{name}")
        print(bot.user.name + " has started.")


    bot.run(config.token())
