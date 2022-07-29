
from asyncio import ALL_COMPLETED
from email.mime import application
from setuptools import Command
from telegram.ext import ApplicationBuilder,ContextTypes, CommandHandler, MessageHandler, filters
from telegram import Update
import logging
TOKEN = "5247296052:AAEaZtE7W6mpDTrL754r3DCUAJZ59TYYn04"
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Ciao peppozzo 2")
    print((await context.bot.get_updates())[0])

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.copy_message(chat_id = update.effective_chat.id, from_chat_id= update.effective_chat.id, message_id= update.effective_message.id)

async def unk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id = update.effective_chat.id, text = 'Ma c cazz e scritt')

async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.bot.callback_data_cache.clear_callback_data()
    context.bot.callback_data_cache.clear_callback_queries()
    await update.effective_message.reply_animation()
    #context.bot.deleteMessage(chat_id = update.effective_chat.id, message_id = update.message.message_id)


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler('start',start)
    clear_handler = CommandHandler('clear',clear)
    echo_handler =  MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    unk_handler =  MessageHandler(filters.COMMAND, unk)
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(clear_handler)
    application.add_handler(unk_handler)
    
    application.run_polling()