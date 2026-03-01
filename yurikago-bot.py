@bot.tree.command(name="graduated_timer", description="graduated_timer command")
@app_commands.describe(minutes="何分", seconds="何秒",user="タイマー終了時に通知するユーザー")
async def graduated_timer_cmd(
    interaction: discord.Interaction,
    minutes: int,
    seconds: int,
    user: discord.Member
):
    ctx = interaction

    remain_min = minutes
    remain_sec = seconds

    # 最初のメッセージ（必ず response.send_message で1回だけ出す）
    if remain_min == 0:
        msg = f"残り時間:\n# {remain_sec}秒"
    else:
        msg = f"残り時間:\n# {remain_min}分 {remain_sec}秒"

    await ctx.response.send_message(content=msg)

    await asyncio.sleep(1)

    while not (remain_sec == 0 and remain_min == 0):
        if remain_min == 0:
            msg = f"残り時間:\n# {remain_sec}秒"
        else:
            msg = f"残り時間:\n# {remain_min}分 {remain_sec}秒"

        await ctx.edit_original_response(content=msg)

        if remain_sec == 0:
            remain_min -= 1
            remain_sec = 59
        else:
            remain_sec -= 1

        await asyncio.sleep(1)

    await ctx.edit_original_response(content="終了しました。")

    ch = interaction.channel
    if ch is not None:
        await ch.send(f"{user.mention}\n終了です！")
