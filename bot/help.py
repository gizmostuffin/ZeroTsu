from telegram import (Update, ParseMode, InlineKeyboardMarkup, 
                      InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton )

from telegram.ext import CallbackContext

from bot.String import String


def chelp(update: Update, context: CallbackContext) -> None:
    keyboard = [
            [
                InlineKeyboardButton(text="Go back",
                                     callback_data="zero_back")
            ]
               ]
    update.message.reply_text(
        String.HELP_MESSAGE,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode=ParseMode.MARKDOWN
    )
    
def help(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if query.data == "zero_help":
        keyboard = [
            [
                InlineKeyboardButton(text="Go back",
                                     callback_data="zero_back")
            ]
               ]
        query.message.edit_text(
            String.HELP_MESSAGE,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode=ParseMode.MARKDOWN
        )
    elif query.data == "zero_back":
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
        query.message.edit_text(
            String.START_MESSAGE.format(query.from_user.first_name),
            reply_markup=InlineKeyboardMarkup(keyboard),
            disable_web_page_preview=True,
            parse_mode=ParseMode.MARKDOWN
        )
    elif query.data == "zero_support":
        keyboard = [
            [
                InlineKeyboardButton(text="Go back",
                                     callback_data="zero_back")
            ]
               ]
        query.message.edit_text(
            String.SUPPORT_MESSAGE,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode=ParseMode.MARKDOWN
        )
    elif query.data == "zero_source":
        keyboard = [
            [
                InlineKeyboardButton(text="Go back",
                                     callback_data="zero_back")
            ]
               ]
        query.message.edit_text(
            String.SOURCE_MESSAGE,
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode=ParseMode.MARKDOWN
        )
        
    