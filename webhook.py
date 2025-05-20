import discord
import requests

TOKEN = "ODg1MDU4Nzg5MTA2MTQ3MzU4.Gc8bhd.1-0r5Cox-Tcu-LE4oK5e9-ru9rJY7IzWt3TqHY"  # Selfbot token (tài khoản người dùng)
name_owner = "KhanhDuy"
name_server = " | 𝗦𝗮𝗺𝗲 𝗛𝘄𝗶𝗱 | 𝟮𝟬𝟮𝟱"
invite_discord = "https://discord.gg/jsPAjFaB"
avt_owner = "https://media.discordapp.net/...gif"

webhooks = {
    "mirage": "https://discordapp.com/api/webhooks/1374403884470239404/L4GL5sIT28h12ICdUfnm-el5XOcer2kkZgmwXIXkmf56nAoO-nhieylH_1YWLq2kGJTY",
    "rare_boss": "https://discordapp.com/api/webhooks/1374404145158815894/wIowVysoDlOu65zGPWhpNnPBseVVLIrLoU7zrvAQBaHag0ivxEuJquAcoJfvwn1Lrgdv",
    "common_boss": "https://discordapp.com/api/webhooks/1374404251995996160/e_VuNq1j-QTBBThdOnYwDRI2nwceYoQSlP0x31XVMRfsqCXjjtQkSs61D5LV8xlqNLmI",
    "fullmoon": "https://discordapp.com/api/webhooks/1374403787124506686/zFfkP7jyD3RELxQdCDBO0e441BW8Isyjg_j36mMOp9qGx8FQnV0ijb8CL_4qiRGrd0bo",
    "moon": "https://discordapp.com/api/webhooks/1374331487326830703/OLRXoAzdlufAGMRQgueWUQPmg8XRXqvgbb4guqrIH1bdIWIT2GjqlIVjUccJeHIvqqtv",
    "sword": "https://discordapp.com/api/webhooks/1374404358015553689/1SnFRV3MEdIhQkIfpXQ1mMaawwgandAfWSIrORS3hEwjDrMWboE-PzKciUBGVTQ2gVC9",
    "haki_legend": "https://discordapp.com/api/webhooks/1374404469197901834/h902xXvKYo-DAZ7jlvlgUOkSDm__CZIefvru82kcbQrZSF0z7xbilYhajJmURth_82wo",
    "prehistoric": "https://discordapp.com/api/webhooks/1374404027416055949/S2JyAU8rcg7bcnEDUlwKJStiiGjfNFPIOArVGVJqZVAsGBjwWw6eLC0Z7C2eO0skgi4K"
}

ping_roles = {
    "boss": "",
    "sword": "",
    "mirage": "",
    "haki": {
        "normal": "",
        "legend": ""
    },
    "fullmoon": "",
    "moon": "",
    "near_full_moon": "",
    "fruit_drop": ""
}

client = discord.Client(self_bot=True)

def send_webhook(title, url, role, fields):
    if not url:
        return
    embed = {
        "title": title + name_server,
        "url": invite_discord,
        "color": 16777215,
        "fields": fields,
        "footer": {
            "text": f"Created By: @{name_owner} {invite_discord}",
            "icon_url": avt_owner
        }
    }
    requests.post(url, json={
        "content": role,
        "embeds": [embed]
    })

@client.event
async def on_ready():
    print("✅ Bot Connected")

@client.event
async def on_message(message):
    if not message.embeds or not hasattr(message.embeds[0], "fields"):
        return

    fields = message.embeds[0].fields
    channel_id = str(message.channel.id)

    if channel_id == "1363206947192573992":
        send_webhook("Mirage Island", webhooks["mirage"], ping_roles["mirage"], [
            {"name": "**[🏝️] __Mirage Spawn:__**", "value": "```✅```"},
            {"name": "**[⏳] __Time In Server:__**", "value": fields[1].value},
            {"name": "**[👤] __Players In Server:__**", "value": fields[3].value},
            {"name": "**[🔗] __Banana JobID:__**", "value": fields[4].value},
            {"name": "**[🔗] __Banana JobID (Mobile):__**", "value": fields[5].value},
        ])

    elif channel_id == "1293189774189920286":
        send_webhook("Haki Legendary", webhooks["haki_legend"], ping_roles["haki"]["legend"], [
            {"name": "**[🌈] __Color Haki:__**", "value": fields[0].value},
            {"name": "**[🌏] __World (Sea):__**", "value": fields[1].value},
            {"name": "**[👤] __Players In Server:__**", "value": fields[2].value},
            {"name": "**[🔗] __Banana JobID:__**", "value": fields[3].value},
            {"name": "**[🔗] __Banana JobID (Mobile):__**", "value": fields[4].value},
        ])

    elif channel_id == "1292825815448293447":
        send_webhook("Rare Boss Spawn", webhooks["rare_boss"], ping_roles["boss"], [
            {"name": "**[👺] __Boss Name:__**", "value": fields[0].value},
            {"name": "**[👥] __Player:__**", "value": fields[1].value},
            {"name": "**[🔗] __Banana JobID:__**", "value": fields[2].value},
            {"name": "**[🔗] __Banana JobID (Mobile):__**", "value": fields[3].value},
        ])

    elif channel_id == "1146760460675326005":
        send_webhook("Common Boss Spawn", webhooks["common_boss"], ping_roles["boss"], [
            {"name": "**[👺] __Boss Name:__**", "value": fields[0].value},
            {"name": "**[👥] __Player:__**", "value": fields[1].value},
            {"name": "**[🔗] __Banana JobID:__**", "value": fields[2].value},
            {"name": "**[🔗] __Banana JobID (Mobile):__**", "value": fields[3].value},
        ])

    elif channel_id == "1293189855748161546":
        send_webhook("Sword Legend", webhooks["sword"], ping_roles["sword"], [
            {"name": "**[⚔️] __Sword Name:__**", "value": fields[0].value},
            {"name": "**[👤] __Players In Server:__**", "value": fields[1].value},
            {"name": "**[🔗] __Banana JobID:__**", "value": fields[2].value},
            {"name": "**[🔗] __Banana JobID (Mobile):__**", "value": fields[3].value},
        ])

    elif channel_id == "1355139542537081005":
        send_webhook("Full Moon", webhooks["fullmoon"], ping_roles["fullmoon"], [
            {"name": "**[🌑] __Full Moon:__**", "value": "```✅```"},
            {"name": "**[👤] __Player Count:__**", "value": fields[2].value},
            {"name": "**[⏳] __Time Remaining:__**", "value": fields[0].value},
            {"name": "**[🔗] __Banana JobID:__**", "value": fields[3].value},
            {"name": "**[🔗] __Banana JobID (Mobile):__**", "value": fields[4].value},
        ])

    elif channel_id == "1108002841408323666":
        send_webhook("Moon", webhooks["moon"], ping_roles["moon"], [
            {"name": "**[🌑] __Moon:__**", "value": "```✅```"},
            {"name": "**[👤] __Player Count:__**", "value": fields[2].value},
            {"name": "**[⏳] __Time Remaining:__**", "value": fields[0].value},
            {"name": "**[🔗] __Banana JobID:__**", "value": fields[3].value},
            {"name": "**[🔗] __Banana JobID (Mobile):__**", "value": fields[4].value},
        ])

    elif channel_id == "1317963371328307290":
        send_webhook("Prehistoric Island Spawned", webhooks["prehistoric"], "", [
            {"name": "**[🌋] __Prehistoric Island:__**", "value": fields[0].value},
            {"name": "**[👥] __Player:__**", "value": fields[3].value},
            {"name": "**[🔗] __Banana JobID:__**", "value": fields[4].value},
            {"name": "**[🔗] __Banana JobID (Mobile):__**", "value": fields[5].value},
        ])

client.run(TOKEN)