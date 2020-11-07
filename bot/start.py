from telegram import (Update, ParseMode, InlineKeyboardMarkup, 
                      InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton )

from telegram.ext import CallbackContext

from bot.String import String


def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
            [
                InlineKeyboardButton(text="Commands available ❔",
                                     callback_data="zero_help")
            ],
            [
                InlineKeyboardButton(text="Source",
                                     callback_data="zero_source"),
                InlineKeyboardButton(text="Support",
                                     callback_data="zero_support")
            ]
               ]
    update.message.reply_text(
        String.START_MESSAGE.format(update.message.from_user.first_name),
        reply_markup=InlineKeyboardMarkup(keyboard),
        disable_web_page_preview=True,
        parse_mode=ParseMode.MARKDOWN
        )