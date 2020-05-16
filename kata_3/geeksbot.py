from telegram.ext import Updater

def main():
    updater = Updater(token = open('./bot_token').read(), use_context = True)
    update.start_polling()
    updater.idle()

main()