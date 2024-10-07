import discord  # Inportation de la bibliotèque discord !
from discord.ext import commands # Importation de la fonction commands de la bibliothèque discord !
bot = commands.Bot(command_prefix='&', intents=discord.Intents.all()) 
    # Ici, nous avons defini les itents et le prefix de notre bot (et on a notre bot qui se nomme bot (ligne 6:1))

@bot.command()
async def clear(ctx : commands.Context, amount : int = 5 ):
    dm_chat = ctx.guild is None and isinstance(ctx.author, discord.user)
    if dm_chat:
        return await ctx.send("Vous n'êste pas sur un serveur actuellement !")
    has_permission = ctx.author.guild_permissions.manage_messages
    if not has_permission: 
        return await ctx.send("Vous n'avez pas les perms nécessaire pour cette action !")
    limit_del = amount > 100
    if limit_del > 100:
        return await ctx.send("Vous ne pouvez pas supprimer plus de 100 messages à la fois !")
    room_text = isinstance(ctx.channel, discord.TextChannel)
    if not room_text:
        return await ctx.send("Cette commande est seulement disponible dans les salons textuels !")
    await ctx.channel.purge(limit = amount+1) # Appel de la commande purge de notre channel et commme cette methode prendra en compte la limite qui vas être égal à amount + 1 car l'on rajoute le message de la commande !
    return await ctx.send("{} messages ont été supprimés".format(amount))



@bot.command()
async def ban(ctx, member: discord.Member, reason: str = "Raison non spécifiée"):#+
    """#+
    Commande permettant de bannir un utilisateur du serveur.#+
#+
    Parameters:#+
    ctx (discord.ext.commands.Context): Le contexte de la commande.#+
    member (discord.Member): L'utilisateur à bannir.#+
    reason (str): La raison du ban. Par défaut, elle est "Raison non spécifiée".#+
#+
    Returns:#+
    discord.Message: Un message de confirmation ou d'erreur.#+
    """#+
    dm_chat = ctx.guild is None and isinstance(ctx.author, discord.User)#+
    if dm_chat:#+
        return await ctx.send("Vous n'êtes pas sur un serveur actuellement !")#+
    has_permission = ctx.author.guild_permissions.ban_members#+
    if not has_permission: #+
        return await ctx.send("Vous n'avez pas les permissions nécessaires pour cette action !")#+
    if member == ctx.author:#+
        return await ctx.send("Vous ne pouvez pas vous bannir vous-même !")#+
    if member.guild_permissions.administrator:#+
        return await ctx.send("Vous ne pouvez pas bannir un administrateur !")#+
    try:#+
        await member.ban(reason=reason)#+
        return await ctx.send(f"{member} a été banni pour la raison suivante : {reason}")#+
    except discord.Forbidden:#+
        return await ctx.send("Je n'ai pas les permissions nécessaires pour bannir cet utilisateur.")#+
    except discord.HTTPException:#+
        return await ctx.send("Une erreur est survenue lors du ban de l'utilisateur.")#+
    
@bot.command()
async def uban(ctx, member: discord.Member, reason: str = "Raison non spécifié !"):
    dm_chat = ctx.guild is None and isinstance(ctx.author, discord.User)
    if dm_chat:
        return await ctx.send("Vous n'êtes pas sur un serveur actuellement!")
    has_permission = ctx.author.guild_permissions.ban_members
    if not has_permission:
        return await ctx.send("Vous n'avez pas les permissions nécessaires pour cette action!")
    try:
        await member.uban(reason = reason)
        return await ctx.send(f"{member} a été débanni pour la raison suivante : {reason}")
    except discord.Forbidden:
        return await ctx.send("Je n'ai pas les permissions nécessaires pour débannir cet utilisateur.")
    except discord.HTTPException:
        return await ctx.send("Une erreur est survenue lors du déban de l'utilisateur.")
    
__all__ = ['clear', 'ban', 'uban']
# Les commandes qui seront prise en charge dans le main ! 