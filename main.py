import logging
import json
import subprocess
from telegram import Update, ForceReply
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

# Read Token:
f = open("config.json", "r")
data = json.load(f)
token = data["TOKEN"]
tg_id = data["TGID"]


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    chat_id = update.message.chat.id
    if tg_id == str(chat_id):
        user = update.effective_user
        update.message.reply_markdown_v2(
            rf"Hi {user.mention_markdown_v2()}\!",
            reply_markup=ForceReply(selective=True),
        )
    else:
        user = update.effective_user
        update.message.reply_markdown_v2(
            rf"Hi {user.mention_markdown_v2()}\! You are not authorized to use this bot\! ",
            reply_markup=ForceReply(selective=True),
        )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    chat_id = update.message.chat.id
    if tg_id == str(chat_id):
        update.message.reply_text(
            "Hi there!\nType /cmd yourcommand for executing terminal commands and /send filename to get files downloaded."
        )
    else:
        user = update.effective_user
        update.message.reply_markdown_v2(
            rf"Hi {user.mention_markdown_v2()}\! You are not authorized to use this bot\! ",
            reply_markup=ForceReply(selective=True),
        )


def cmd(update: Update, context: CallbackContext) -> None:
    """Execute Command when the command /cmd is issued."""
    chat_id = update.message.chat.id
    if tg_id == str(chat_id):
        comand = update.message.text.split(" ", 1)[1]
        output = subprocess.getoutput(comand)
        if len(output) > 4096:
            for i in range(0, len(output), 4096):
                temp = output[i : i + 4096]
                update.message.reply_text(f"<code>{temp}</code>", parse_mode="HTML")
        else:
            update.message.reply_text(f"<code>{output}</code>", parse_mode="HTML")
        print(comand)
    else:
        user = update.effective_user
        update.message.reply_markdown_v2(
            rf"Hi {user.mention_markdown_v2()}\! You are not authorized to use this bot\! ",
            reply_markup=ForceReply(selective=True),
        )


def send(update, context):
    """Send File when the command /send is issued."""
    chat_id = update.message.chat.id
    if tg_id == str(chat_id):
        chat_id = update.message.chat.id
        bot = context.bot
        file = update.message.text.split()[1]
        bot.send_document(chat_id=chat_id, document=open(file, "rb"))
    else:
        user = update.effective_user
        update.message.reply_markdown_v2(
            rf"Hi {user.mention_markdown_v2()}\! You are not authorized to use this bot\! ",
            reply_markup=ForceReply(selective=True),
        )


def main() -> None:
    updater = Updater(token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("cmd", cmd))
    dispatcher.add_handler(CommandHandler("send", send))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
