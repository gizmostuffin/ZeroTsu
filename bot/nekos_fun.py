from telegram import Update

from telegram.ext import CallbackContext

def asfile(update: Update, context: CallbackContext) -> None:
    bot = context.bot
    query = update.callback_query
    message = query.message
    data = query.data.split(", ")
    query_type = data[0]
    user_id = data[1]
   
    if query_type == "neko_callback":
        if data[2] == 'hexa':
            data = data[1][2:]
            data = data[:-3]
            link = f"https://dva.computerfreaker.cf/{data}"
            message.reply_document(link)
            
        elif data[2] == 'neko':
            data = data[1][2:]
            data = data[:-3]
            link = f"https://cdn.nekos.life/{data}"
            message.reply_document(link)
            
    elif query_type == "neko_delete":
        if query.from_user.id == int(user_id):
            bot.answer_callback_query(query.id,
                                      text="Deleted!"
                                      )
            message.delete()
        else:
            bot.answer_callback_query(query.id,
                                      text="You're not allowed to use this."
                                      )
       