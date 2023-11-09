# MIT License

# Copyright (c) 2020 Anil Chauhan // This file is part of ZeroTsu

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import yaml
from telegram import BotCommand
from telegram.ext import Updater
from telegram import Update
import logging
from telegram.ext import (
    Application,
    CallbackContext,
    CommandHandler,
    CallbackQueryHandler
)
from bot.start import start
from bot.help import help, chelp
from bot.nekos import *
from bot.nekos_fun import asfile

# load config
try:
    CONFIG = yaml.load(open('config.yml', 'r'), Loader=yaml.SafeLoader)
except FileNotFoundError:
    print("Read README.md file again. you missed something.")
    quit(1)
except Exception as eee:
    print(
        f"Ah, look like there's error(s) while trying to load your config. It is\n!!!! ERROR BELOW !!!!\n {eee} \n !!! ERROR END !!!"
    )
    quit(1)
 

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

COMMANDS = [
        BotCommand('start', 'check I\'m alive uwu'),
        BotCommand('neko', 'Sends Random SFW Neko source Images.'),
        BotCommand('feet', 'Sends Random Anime Feet Images.'),
        BotCommand('yuri', 'Sends Random Yuri source Images.'),
        BotCommand('trap', 'Sends Random Trap source Images.'),
        BotCommand('futanari', 'Sends Random Futanari source Images.'),
        BotCommand('hololewd', 'Sends Random Holo Lewds.'),
        BotCommand('lewdkemo', 'Sends Random Kemo Lewds'),
        BotCommand('sologif', 'Sends Random Solo GIFs.'),
        BotCommand('cumgif', ' Sends Random Cum GIFs.'),
        BotCommand('erokemo', 'Sends Random Ero-Kemo Images.'),
        BotCommand('lesbian', 'Sends Random Les Source Images.'),
        BotCommand('wallpaper', 'Sends Random Wallpapers.'),
        BotCommand('lewdk', 'Sends Random Kitsune Lewds.'),
        BotCommand('ngif', 'Sends Random Neko GIFs.'),
        BotCommand('tickle', 'Sends Random Tickle GIFs.'),
        BotCommand('lewd', 'Sends Random Lewds.'),
        BotCommand('feed', 'Sends Random Feeding GIFs.'),
        BotCommand('eroyuri', 'Sends Random Ero-Yuri source Images.'),
        BotCommand('eron', 'Sends Random Ero-Neko source Images.'),
        BotCommand('cum', 'Sends Random Cum Images.'),
        BotCommand('bjgif', 'Sends Random Blow Job GIFs.'),
        BotCommand('bj', 'Sends Random Blow Job source Images.'),
        BotCommand('nekonsfw', 'Sends Random NSFW Neko source Images.'),
        BotCommand('solo', 'Sends Random NSFW Neko GIFs.'),
        BotCommand('kemonomimi', 'Sends Random KemonoMimi source Images.'),
        BotCommand('avatarlewd', 'Sends Random Avater Lewd Stickers.'),
        BotCommand('gasm', 'Sends Random Orgasm Stickers.'),
        BotCommand('poke', 'Sends Random Poke GIFs.'),
        BotCommand('anal', 'Sends Random Anal GIFs.'),
        BotCommand('hentai', 'Sends Random Hentai source Images.'),
        BotCommand('avatar', 'Sends Random Avatar Stickers.'),
        BotCommand('erofeet', ' Sends Random Ero-Feet source Images.'),
        BotCommand('holo', 'Sends Random Holo source Images.'),
        BotCommand('tits', 'Sends Random Tits source Images.'),
        BotCommand('pussygif', 'Sends Random Pussy GIFs.'),
        BotCommand('holoero', 'Sends Random Ero-Holo source Images.'),
        BotCommand('pussy', 'Sends Random Pussy source Images.'),
        BotCommand('hentaigif', 'Sends Random Hentai GIFs.'),
        BotCommand('classic', 'Sends Random Classic Hentai GIFs.'),
        BotCommand('kuni', 'Sends Random Pussy Lick GIFs.'),
        BotCommand('waifu', 'Sends Random Waifu Stickers.'),
        BotCommand('kiss', 'Sends Random Kissing GIFs.'),
        BotCommand('femdom', 'Sends Random Femdom source Images.'),
        BotCommand('cuddle', 'Sends Random Cuddle GIFs.'),
        BotCommand('erok', 'Sends Random Ero-Kitsune source Images.'),
        BotCommand('foxgirl', 'Sends Random FoxGirl source Images.'),
        BotCommand('titsgif', ' Sends Random Tits GIFs.'),
        BotCommand('smug', 'Sends Random Smug GIFs.'),
        BotCommand('baka', 'Sends Random Baka Shout GIFs.'),
        BotCommand('dva', 'Sends Random D.VA source Images.'),
        
    ]

# Create the Application and pass it your bot's token.
application = Application.builder().token(CONFIG['bot_token']).build()

application.bot.set_my_commands(COMMANDS)

application.add_handler(CommandHandler('start', start))
application.add_handler(CommandHandler('help', chelp))
application.add_handler(CallbackQueryHandler(help, pattern='zero_.*'))
application.add_handler(CallbackQueryHandler(asfile, pattern='neko_.*'))

application.add_handler(CommandHandler("lewdkemo", lewdkemo))
application.add_handler(CommandHandler("neko", neko))
application.add_handler(CommandHandler("feet", feet))
application.add_handler(CommandHandler("yuri", yuri))
application.add_handler(CommandHandler("trap", trap))
application.add_handler(CommandHandler("futanari", futanari))
application.add_handler(CommandHandler("hololewd", hololewd))
application.add_handler(CommandHandler("sologif", sologif))
application.add_handler(CommandHandler("cumgif", cumgif))
application.add_handler(CommandHandler("erokemo", erokemo))
application.add_handler(CommandHandler("lesbian", lesbian))
application.add_handler(CommandHandler("wallpaper", wallpaper))
application.add_handler(CommandHandler("lewdk", lewdk))
application.add_handler(CommandHandler("ngif", ngif))
application.add_handler(CommandHandler("tickle", tickle))
application.add_handler(CommandHandler("lewd", lewd))
application.add_handler(CommandHandler("feed", feed))
application.add_handler(CommandHandler("eroyuri", eroyuri))
application.add_handler(CommandHandler("eron", eron))
application.add_handler(CommandHandler("cum", cum))
application.add_handler(CommandHandler("bjgif", bjgif))
application.add_handler(CommandHandler("bj", bj))
application.add_handler(CommandHandler("nekonsfw", nekonsfw))
application.add_handler(CommandHandler("solo", solo))
application.add_handler(CommandHandler("kemonomimi", kemonomimi))
application.add_handler(CommandHandler("avatarlewd", avatarlewd))
application.add_handler(CommandHandler("gasm", gasm))
application.add_handler(CommandHandler("poke", poke))
application.add_handler(CommandHandler("anal", anal))
application.add_handler(CommandHandler("hentai", hentai))
application.add_handler(CommandHandler("avatar", avatar))
application.add_handler(CommandHandler("erofeet", erofeet))
application.add_handler(CommandHandler("holo", holo))
application.add_handler(CommandHandler("tits", tits))
application.add_handler(CommandHandler("pussygif", pussygif))
application.add_handler(CommandHandler("holoero", holoero))
application.add_handler(CommandHandler("pussy", pussy))
application.add_handler(CommandHandler("hentaigif", hentaigif))
application.add_handler(CommandHandler("classic", classic))
application.add_handler(CommandHandler("kuni", kuni))
application.add_handler(CommandHandler("waifu", waifu))
application.add_handler(CommandHandler("lewd", lewd))
application.add_handler(CommandHandler("kiss", kiss))
application.add_handler(CommandHandler("femdom",femdom))
application.add_handler(CommandHandler("cuddle", cuddle))
application.add_handler(CommandHandler("erok", erok))
application.add_handler(CommandHandler("foxgirl", foxgirl))
application.add_handler(CommandHandler('titsgif', titsgif))
application.add_handler(CommandHandler('ero', ero))
application.add_handler(CommandHandler('smug', smug))
application.add_handler(CommandHandler('baka', baka))
application.add_handler(CommandHandler('dva', dva))


application.run_polling(allowed_updates=Update.ALL_TYPES)