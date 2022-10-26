from telethon import functions

from Legendbot import legend

from ..Config import Config
from ..core import CMD_INFO, GRP_INFO, PLG_INFO
from ..core.managers import eod, eor
from ..helpers.utils import reply_id

cmdprefix = Config.HANDLER

menu_category = "ᴛᴏᴏʟꜱ"

hemojis = {
    "ᴀᴅᴍɪɴꜱ": "🥀",
    "ᴜꜱᴇʀʙᴏᴛ": "🥀",
    "ꜰᴜɴ": "🥀",
    "ᴍɪꜱᴄ": "🥀",
    "ᴛᴏᴏʟꜱ": "🥀",
    "ᴜᴛɪʟꜱ": "🥀",
    "ᴇxᴛʀᴀ": "🥀",
    "ᴜꜱᴇʟᴇꜱꜱ": "🥀",
}


def get_key(val):
    for key, value in PLG_INFO.items():
        for cmd in value:
            if val == cmd:
                return key
    return None


def getkey(val):
    for key, value in GRP_INFO.items():
        for plugin in value:
            if val == plugin:
                return key
    return None


async def cmdinfo(input_str, event, plugin=False):
    if input_str[0] == cmdprefix:
        input_str = input_str[1:]
    try:
        about = CMD_INFO[input_str]
    except KeyError:
        if plugin:
            await eod(
                event,
                f"🥀**ᴛʜᴇʀᴇ ɪꜱ ɴᴏ ᴘʟᴜɢɪɴ ᴏʀ ᴄᴏᴍᴍᴀɴᴅ ᴀꜱ **`{input_str}`** iɴ ʏᴏᴜʀ ʙᴏᴛ.**🥀",
            )
            return None
        await eod(event, f"🥀**ᴛʜᴇʀᴇ ɪꜱ ɴᴏ ᴄᴏᴍᴍᴀɴᴅ ᴀꜱ **`{input_str}`** iɴ ʏᴏᴜʀ ʙᴏᴛ.**🥀")
        return None
    except Exception as e:
        await eod(event, f"**Error**\n`{e}`")
        return None
    outstr = f"**🥀𝕮𝖔𝖒𝖒𝖆𝖓𝖉🥀 :** `{cmdprefix}{input_str}`\n"
    plugin = get_key(input_str)
    if plugin is not None:
        outstr += f"**🥀𝕻𝖑𝖚𝖌𝖎𝖓𝕾🥀 :** `{plugin}`\n"
        category = getkey(plugin)
        if category is not None:
            outstr += f"**🥀𝕮𝖆𝖙𝖊𝖌𝖔𝖗𝖞🥀 :** `{category}`\n\n"
    outstr += f"**🥀𝕴𝖓𝖙𝖗𝖔🥀 :**\n{about[0]}"
    return outstr


async def plugininfo(input_str, event, type):
    try:
        cmds = PLG_INFO[input_str]
    except KeyError:
        outstr = await cmdinfo(input_str, event, plugin=True)
        return outstr
    except Exception as e:
        await eod(event, f"**Error**\n`{e}`")
        return None
    if len(cmds) == 1 and (type is None or (type and type != "-p")):
        outstr = await cmdinfo(cmds[0], event, plugin=False)
        return outstr
    outstr = f"**🥀𝕻𝖑𝖚𝖌𝖎𝖓𝕾 : **`{input_str}`\n"
    outstr += f"**🥀𝕮𝖔𝖒𝖒𝖆𝖓𝖉𝖘 𝕬𝖛𝖆𝖎𝖑𝖆𝖇𝖑𝖊🥀 :** `{len(cmds)}`\n"
    category = getkey(input_str)
    if category is not None:
        outstr += f"**🥀𝕮𝖆𝖙𝖊𝖌𝖔𝖗𝖞🥀 :** `{category}`\n\n"
    for cmd in sorted(cmds):
        outstr += f"**🥀𝕮𝖔𝖒𝖒𝖆𝖓𝖉🥀 :** `{cmdprefix}{cmd}`\n"
        try:
            outstr += f"**🥀𝕴𝖓𝖋𝖔🥀 :** __{CMD_INFO[cmd][1]}__\n\n"
        except IndexError:
            outstr += "**🥀𝕴𝖓𝖋𝖔🥀 :** `None`\n\n"
    outstr += f"**🥀 𝖀𝖘𝖆𝖌𝖊 : ** `{cmdprefix}help <command name>`\
        \n**Note : **ɪꜰ ᴄᴏᴍᴍᴀɴᴅ ɴᴀᴍᴇ ɪꜱ ꜱᴀᴍᴇ ᴀꜱ ᴘʟᴜɢɪɴ ɴᴀᴍᴇ ᴛʜᴇɴ ᴜꜱᴇ ᴛʜɪꜱ `{cmdprefix}help -l <command name>`."
    return outstr


async def grpinfo():
    outstr = "**🥀ᴘʟᴜɢɪɴꜱ ɪɴ ʟᴇɢᴇɴᴅxʙᴏᴛ ᴀʀᴇ🥀:**\n\n"
    outstr += f"**🥀 𝖀𝖘𝖆𝖌𝖊 : ** `{cmdprefix}help <plugin name>`\n\n"
    category = ["ᴀᴅᴍɪɴꜱ", "ᴜꜱᴇʀʙᴏᴛ", "ꜰᴜɴ", "ᴍɪꜱᴄ", "ᴛᴏᴏʟꜱ", "ᴜᴛɪʟꜱ", "ᴇxᴛʀᴀ", "ᴜꜱᴇʟᴇꜱꜱ"]
    for legend in category:
        plugins = GRP_INFO[legend]
        outstr += f"**{hemojis[legend]} {legend.title()} **({len(plugins)})\n"
        for plugin in plugins:
            outstr += f"`{plugin}`  "
        outstr += "\n\n"
    return outstr


async def cmdlist():
    outstr = "**🥀ᴛᴏᴛᴀʟ ʟɪꜱᴛ ᴏꜰ ᴄᴏᴍᴍᴀɴᴅꜱ ɪɴ ʏᴏᴜʀ ʟᴇɢᴇɴᴅxʙᴏᴛ ᴀʀᴇ🥀 :**\n\n"
    category = ["ᴀᴅᴍɪɴꜱ", "ᴜꜱᴇʀʙᴏᴛ", "ꜰᴜɴ", "ᴍɪꜱᴄ", "ᴛᴏᴏʟꜱ", "ᴜᴛɪʟꜱ", "ᴇxᴛʀᴀ"]
    for legend in category:
        plugins = GRP_INFO[legend]
        outstr += f"**{hemojis[legend]} {legend.title()} ** - {len(plugins)}\n\n"
        for plugin in plugins:
            cmds = PLG_INFO[plugin]
            outstr += f"• **{plugin.title()} ʜᴀꜱ {len(cmds)} ᴄᴏᴍᴍᴀɴᴅꜱ**\n"
            for cmd in sorted(cmds):
                outstr += f"  - `{cmdprefix}{cmd}`\n"
            outstr += "\n"
    outstr += f"**🥀 𝖀𝖘𝖆𝖌𝖊 : ** `{cmdprefix}help -l <command name>`"
    return outstr


@legend.legend_cmd(
    pattern="help ?(-l|-p|-t)? ?([\s\S]*)?",
    command=("help", menu_category),
    info={
        "header": "To get guide for LegendBot.",
        "description": "To get information or guide for the command or plugin",
        "note": "if command name and plugin name is same then you get guide for plugin. So by using this type you get command guide",
        "flags": {
            "l": "To get info of command.",
            "p": "To get info of plugin.",
            "t": "To get all plugins in text format.",
        },
        "usage": [
            "{tr}help (plugin/command name)",
            "{tr}help -l (command name)",
        ],
        "examples": ["{tr}help help", "{tr}help -l help"],
    },
)
async def _(event):
    "To get guide for LegendBot."
    type = event.pattern_match.group(1)
    input_str = event.pattern_match.group(2)
    reply_to_id = await reply_id(event)
    if type and type == "-l" and input_str:
        outstr = await cmdinfo(input_str, event)
        if outstr is None:
            return
    elif input_str:
        outstr = await plugininfo(input_str, event, type)
        if outstr is None:
            return
    elif type == "-t":
        outstr = await grpinfo()
    else:
        results = await event.client.inline_query(Config.BOT_USERNAME, "help")
        await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
        await event.delete()
        return
    await eor(event, outstr)


@legend.legend_cmd(
    pattern="cmds(?:\s|$)([\s\S]*)",
    command=("cmds", menu_category),
    info={
        "header": "To show list of cmds.",
        "description": "if no input is given then will show list of all commands.",
        "usage": [
            "{tr}cmds for all cmds",
            "{tr}cmds <plugin name> for paticular plugin",
        ],
    },
)
async def _(event):
    "To get list of commands."
    input_str = event.pattern_match.group(1)
    if not input_str:
        outstr = await cmdlist()
    else:
        try:
            cmds = PLG_INFO[input_str]
        except KeyError:
            return await eod(event, "__Invalid plugin name recheck it.__")
        except Exception as e:
            return await eod(event, f"**Error**\n`{e}`")
        outstr = f"**🥀 {input_str.title()} has {len(cmds)} commands**\n"
        for cmd in cmds:
            outstr += f"  - `{cmdprefix}{cmd}`\n"
        outstr += f"**🥀  𝖀𝖘𝖆𝖌𝖊 : ** `{cmdprefix}help -l <command name>`"
    await eor(event, outstr, aslink=True, linktext="Total Commands of LegendBot are :")


@legend.legend_cmd(
    pattern="dc$",
    command=("dc", menu_category),
    info={
        "header": "To show dc of your account.",
        "description": "Dc of your account and list of dc's will be showed",
        "usage": "{tr}dc",
    },
)
async def _(event):
    "To get dc of your bot"
    result = await event.client(functions.help.GetNearestDcRequest())
    result = f"**🥀Dc details of your account:**\
              \n**Country :** {result.country}\
              \n**Current Dc :** {result.this_dc}\
              \n**Nearest Dc :** {result.nearest_dc}\
              \n\n**List Of Telegram Data Centres:**\
              \n**DC1 : **Miami FL, USA\
              \n**DC2 :** Amsterdam, NL\
              \n**DC3 :** Miami FL, USA\
              \n**DC4 :** Amsterdam, NL\
              \n**DC5 : **Singapore, SG\
                "
    await eor(event, result)
