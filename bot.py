from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


key_token = "6834299372:AAGkrPpOGzsZFen39_VDI5GqKvjeWYuWwzU" 
user_bot: Final = "oshikawa_bot" 


async def start_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Terimakasih udh chat dengan saya ")
    
async def help_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Kirim pesan, bot akan membalas pesan..")

async def custom_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ini command custom")
#respon

async def handle_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    proccesed : str = update.message.text
    print(f"Pesan diterima : {proccesed}")
    text_accept = proccesed.lower()
    if 'halo' in text_accept:
        await update.message.reply_text("halooo makhluk")
    elif 'apa kabarmu' in text_accept:
        await update.message.reply_text("aku baik baik sajah")
    elif 'oshikawa' in text_accept:
        await update.message.reply_text(f"Apa?")
    else:
        await update.message.reply_text("saya tidak mengerti apa yang anda katakan")



async def photo_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    return await update.message.reply_text("ni gambar bagus juga")


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')




    
if __name__ == '__main__':
    print('starting bot....')
    app = Application.builder().token(key_token).build()

    #commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(MessageHandler(filters.PHOTO, photo_message))

    #errors
    app.add_error_handler(error)

    # polls 
    print('polling.....')
    app.run_polling(poll_interval=3)