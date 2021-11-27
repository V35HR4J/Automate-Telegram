import logging
import json
import subprocess
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

#Read Token:
f=open("config.json",'r')
data = json.load(f)
token=data['TOKEN']


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Hi there!\nType /cmd yourcommand for executing terminal commands and /send filename to get files downloaded.')


def cmd(update: Update, context: CallbackContext) -> None:
    """Execute Command when the command /cmd is issued."""
    comand = update.message.text.split(" ",1)[1]
    output = subprocess.getoutput(comand)
    update.message.reply_text(f'<code>{output}</code>', parse_mode='HTML')
    print(comand)

def send(update, context):
    """Send File when the command /send is issued."""
    chat_id = update.message.chat.id
    bot = context.bot
    file = update.message.text.split()[1]
    bot.send_document(chat_id=chat_id, document=open(file, 'rb'))

def main() -> None:
    updater = Updater(token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("cmd", cmd))
    dispatcher.add_handler(CommandHandler("send", send))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
