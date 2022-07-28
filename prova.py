
from setuptools import Command
from telegram.ext import Updater,CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update
import logging
TOKEN = "5247296052:AAEaZtE7W6mpDTrL754r3DCUAJZ59TYYn04"
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)


updater = Updater(token = TOKEN, use_context= True)
dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Ciao peppozzo 2")

def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id = update.effective_chat.id, text = update.message.text)

def clear(update: Update, context: CallbackContext):
    print(updater.bot.messages
    .get_updates()[1])
    #context.bot.deleteMessage(chat_id = update.effective_chat.id, message_id = update.message.message_id)

start_handler = CommandHandler('start',start)
clear_handler = CommandHandler('clear',clear)
echo_handler =  MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(clear_handler)

updater.start_polling()