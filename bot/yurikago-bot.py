# Easy Discord Bot Builderによって作成されました！ 製作：@himais0giiiin
# Created with Easy Discord Bot Builder! created by @himais0giiiin!
# Optimized Version

import discord
from discord import app_commands
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.voice_states = True

# Botの作成
bot = commands.Bot(command_prefix='!', intents=intents)

# ----------------------------

# --- ユーザー作成部分 ---

from numbers import Number

_E4_BD_95_E5_88_86 = None
_E4_BD_95_E7_A7_92 = None



@bot.tree.command(name="graduated_timer", description="graduated_timer command")
async def graduated_timer_cmd(interaction: discord.Interaction):
    ctx = interaction
    user = interaction.user
    _E4_BD_95_E5_88_86 = # Argument '何分' needed
    _E4_BD_95_E7_A7_92 = # Argument '何秒' needed
    if _E4_BD_95_E5_88_86 == 0:
        
        if 'ctx' in locals():
            if isinstance(ctx, discord.Interaction):
                if ctx.response.is_done():
                    await ctx.followup.send(content=''.join([str(x) for x in ['残り時間:\\n', '# ', _E4_BD_95_E7_A7_92, '秒']]), ephemeral=False)
                else:
                    await ctx.response.send_message(content=''.join([str(x) for x in ['残り時間:\\n', '# ', _E4_BD_95_E7_A7_92, '秒']]), ephemeral=False)
            elif isinstance(ctx, commands.Context):
                await ctx.send(content=''.join([str(x) for x in ['残り時間:\\n', '# ', _E4_BD_95_E7_A7_92, '秒']]))
            elif isinstance(ctx, discord.Message):
                await ctx.reply(content=''.join([str(x) for x in ['残り時間:\\n', '# ', _E4_BD_95_E7_A7_92, '秒']]))
    else:
        
        if 'ctx' in locals():
            if isinstance(ctx, discord.Interaction):
                if ctx.response.is_done():
                    await ctx.followup.send(content=''.join([str(x2) for x2 in ['残り時間:\\n', '# ', _E4_BD_95_E5_88_86, '分 ', _E4_BD_95_E7_A7_92, '秒']]), ephemeral=False)
                else:
                    await ctx.response.send_message(content=''.join([str(x2) for x2 in ['残り時間:\\n', '# ', _E4_BD_95_E5_88_86, '分 ', _E4_BD_95_E7_A7_92, '秒']]), ephemeral=False)
            elif isinstance(ctx, commands.Context):
                await ctx.send(content=''.join([str(x2) for x2 in ['残り時間:\\n', '# ', _E4_BD_95_E5_88_86, '分 ', _E4_BD_95_E7_A7_92, '秒']]))
            elif isinstance(ctx, discord.Message):
                await ctx.reply(content=''.join([str(x2) for x2 in ['残り時間:\\n', '# ', _E4_BD_95_E5_88_86, '分 ', _E4_BD_95_E7_A7_92, '秒']]))
    await asyncio.sleep(1)
    while not (_E4_BD_95_E7_A7_92 == 0 and _E4_BD_95_E5_88_86 == 0):
        if _E4_BD_95_E5_88_86 == 0:
            
            if 'ctx' in locals() and isinstance(ctx, discord.Interaction):
                await ctx.edit_original_response(content=''.join([str(x3) for x3 in ['残り時間:\\n', '# ', _E4_BD_95_E7_A7_92, '秒']]))
        else:
            
            if 'ctx' in locals() and isinstance(ctx, discord.Interaction):
                await ctx.edit_original_response(content=''.join([str(x4) for x4 in ['残り時間:\\n', '# ', _E4_BD_95_E5_88_86, '分 ', _E4_BD_95_E7_A7_92, '秒']]))
        if _E4_BD_95_E7_A7_92 == 0:
            _E4_BD_95_E5_88_86 = (_E4_BD_95_E5_88_86 if isinstance(_E4_BD_95_E5_88_86, Number) else 0) + -1
            _E4_BD_95_E7_A7_92 = 59
        else:
            _E4_BD_95_E7_A7_92 = (_E4_BD_95_E7_A7_92 if isinstance(_E4_BD_95_E7_A7_92, Number) else 0) + -1
        await asyncio.sleep(1)
    
    if 'ctx' in locals() and isinstance(ctx, discord.Interaction):
        await ctx.edit_original_response(content='終了しました。')
    
    _ch_id = int((ctx.channel.id if "ctx" in locals() and hasattr(ctx, "channel") else "Unknown")) if str((ctx.channel.id if "ctx" in locals() and hasattr(ctx, "channel") else "Unknown")).isdigit() else 0
    _channel = bot.get_channel(_ch_id)
    if _channel:
        await _channel.send(content=str(# Argument 'ユーザー' needed) + '\\n終了です！')

# --------------------------

if __name__ == "__main__":
    # トークンの設定
    # Set your token here
    token = "TOKEN"

    # Token check
    token = os.getenv("DISCORD_TOKEN", token) # 環境変数DISCORD_TOKENがあればそちらを優先 (If DISCORD_TOKEN environment variable is set, it will be used)
    if token == "TOKEN":
        print('\x1b[31m!!!!注意!!!! トークンを設定していない場合は、環境変数DISCORD_TOKENを設定するか、上のtoken変数を書き換えてください。\x1b[0m')
        print('\x1b[31m!!!!Warning!!!! If you have not set a token, please set the DISCORD_TOKEN environment variable or replace the token variable above.\x1b[0m')
        exit(1)

    bot.run(token)
