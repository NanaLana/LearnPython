from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    print('Вызван /start')

def greet_user(bot, update):
    text = 'Привет, я бот'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text("Ты сказал: " + user_text + " Повтори")

def main():
    updater = Updater("407493484:AAFkb5klovJCbajbz_vid_4cLgqdZn7r6Tk")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    updater.start_polling()
    updater.idle()

main()
