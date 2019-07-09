# Importing telegram commands
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

# Importing settings
from conf.settings import TELEGRAM_TOKEN, HTTP_URL

# Starts the Telegram BOT
def start(bot, update):
    response_message = "=^._.^="
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

# Get the HTTP CATS API
def http_cats(bot, update, args):
    bot.sendPhoto(
        chat_id=update.message.chat_id,
        photo=HTTP_URL + args[0]
    )


# Define the Telegram BOT message unknown
def unknown(bot, update):
    response_message = "Meow? =^._.^="
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )


# Define the main method
def main():
    updater = Updater(token=TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', start)
    )
    dispatcher.add_handler(
        CommandHandler('http', http_cats, pass_args=True)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.command, unknown)
    )

    updater.start_polling()

    updater.idle()

# Main commands
if __name__ == '__main__':
    print("==========================")
    print("The server is running! (:")
    print("Press CTRL + C to cancel.")
    print("==========================")
    main()