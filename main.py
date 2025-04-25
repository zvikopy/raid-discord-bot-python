import os
import pyfiglet
import asyncio
import discord 
from discord.ext import commands
#ARCHIVO DEL TOKEN
#Activa todos los intents
os.system('clear')
text = pyfiglet.figlet_format("BotRaidV1")
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
description="Use .kill (metodo .kill_speed o .kill_lento y pones lo que quieres enviar) y usa .kill stop_lento para detener y .kill stop_speed",
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

@bot.command()
async def nuke(ctx, nombre_canal: str, *, mensaje: str):
    if ctx.author.guild_permissions.manage_channels:
        # Mensaje inicial con conteo regresivo
        mensaje_inicio = await ctx.send("¡Preparando para comenzar en:")
        await ctx.send("1...", delete_after=3)
        await asyncio.sleep(1)
        await ctx.send("2...", delete_after=3)
        await asyncio.sleep(1)
        await ctx.send("3...", delete_after=3)
        await asyncio.sleep(1)

        await mensaje_inicio.delete()  # Elimina el mensaje inicial de preparación

        # Crear canales y enviar mensajes repetitivos
        for i in range(30):  # Crear 30 canales
            try:
                nuevo_canal = await ctx.guild.create_text_channel(nombre_canal)  # Crear canal con nombre especificado
                print(f"Canal creado: {nuevo_canal.name}")

                # Función para enviar mensajes repetitivos
                async def enviar_mensajes(canal):
                    while True:
                        await canal.send(mensaje)  # Enviar mensaje
                        await asyncio.sleep(0.5)  # Repite cada 0.5 segundos

                asyncio.create_task(enviar_mensajes(nuevo_canal))  # Crear la tarea de mensajes repetitivos
            except Exception as e:
                print(f"No se pudo crear el canal {nombre_canal}: {e}")

        await ctx.send("¡30 canales creados y mensajes enviados cada 0.5 segundos!")
    else:
        await ctx.send("No tienes permisos suficientes para gestionar canales.")
#poner token aqui 
bot.run('TOKEN Aqui')    
