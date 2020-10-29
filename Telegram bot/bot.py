import telegram
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.updater import Updater
from telegram.ext.dispatcher import Dispatcher
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.bot import Bot
from telegram.parsemode import ParseMode




updater = Updater(API_TOKEN,use_context=True)

dispatcher = updater.dispatcher


with open("users.txt",'r') as f:
    users = f.readline()

def tag(update: Update, context: CallbackContext):
    with open("users.txt",'r') as f:
        list_of_users = f.readline()

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=
        list_of_users,
        parse_mode=ParseMode.HTML,
    )

def add(update: Update, context: CallbackContext):
    u = []
    for i in context.args:
        if "@" not in i:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=
                "I can accept only usernames",
                parse_mode=ParseMode.HTML,
            )
            break
        u.append(i)
    u = list(set(u))
    with open("users.txt",'a') as f:
        f.write(" " + " ".join(u))

dispatcher.add_handler(CommandHandler("tag", tag))
dispatcher.add_handler(CommandHandler("add", add))

updater.start_polling()
# updater.idle()
