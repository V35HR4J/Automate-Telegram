import logging
import json
import subprocess
import threading
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
with open("config.json", "r") as f:
    data = json.load(f)
    token = data["TOKEN"]
    tg_id = data["TGID"]


def message_display(output, update):
    try:
        if len(output) > 4096:
            pass
            for i in range(0, len(output), 4096):
                temp = output[i: i + 4096]
                update.effective_message.reply_text(
                    f"<code>{temp}</code>", parse_mode="HTML")
        else:
            update.effective_message.reply_text(
                f"<code>{output}</code>", parse_mode="HTML")
    except:
        update.effective_message.reply_text(
            f"<code>Some error has occured with your command</code>", parse_mode="HTML")


def command_handler(update, command):
    """ Run multiple Command without affecting the speed """
    output = subprocess.getoutput(command)
    message_display(output, update)


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    chat_id = update.effective_message.chat.id
    if str(chat_id) in tg_id:
        user = update.effective_user
        update.effective_message.reply_markdown_v2(
            rf"Hi {user.mention_markdown_v2()}\!",
            reply_markup=ForceReply(selective=True),
        )
    else:
        user = update.effective_user
        update.effective_message.reply_markdown_v2(
            rf"Hi {user.mention_markdown_v2()}\! You are not authorized to use this bot\! "
        )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    chat_id = update.effective_message.chat.id
    if str(chat_id) in tg_id:
        update.effective_message.reply_text(
            "<b> <code>/cmd [command]</code> - for executing terminal commands \n <code>/send [Filename]</code> - to get files downloaded \n <code>/download [file_from_server]</code> - to download file from server to your PC.</b>", parse_mode="HTML"
        )
    else:
        user = update.effective_user
        update.effective_message.reply_markdown_v2(
            rf"Hi {user.mention_markdown_v2()}\! You are not authorized to use this bot\! ",
            reply_markup=ForceReply(selective=True),
        )


def cmd(update: Update, context: CallbackContext) -> None:
    """Execute Command when the command /cmd is issued."""
    if str(update.effective_user.id) in tg_id:
        comand = update.effective_message.text.split(" ", 1)[1]
        print(comand)
        t = threading.Thread(target=command_handler, args=[update, comand])
        t.start()
    else:
        user = update.effective_user
        update.effective_message.reply_markdown_v2(
            rf"Hi {user.mention_markdown_v2()}\! You are not authorized to use this bot\! ",
            reply_markup=ForceReply(selective=True),
        )


def send(update, context):
    """Send File when the command /send is issued."""
    chat_id = update.effective_message.chat.id
    if str(chat_id) in tg_id:
        chat_id = update.effective_message.chat.id
        bot = context.bot
        file = update.effective_message.text.split()[1]
        bot.send_document(chat_id=chat_id, document=open(file, "rb"))
    else:
        user = update.effective_user
        update.effective_message.reply_markdown_v2(
            rf"Hi {user.mention_markdown_v2()}\! You are not authorized to use this bot\! ",
            reply_markup=ForceReply(selective=True),
        )


def download_files(update, context):
    """Download file to your computer"""
    chat_id = update.effective_message.chat.id
    if str(chat_id) in tg_id:
        comand = update.effective_message.text.split(" ", 1)[1]
        comand = f'curl -O {comand}'
        output = subprocess.getoutput(comand)
        message_display('File Downloaded, check your computer folder', update)
    else:
        user = update.effective_user
        update.effective_message.reply_markdown_v2(
            rf"Hi {user.mention_markdown_v2()}\! You are not authorized to use this bot\! ",
            reply_markup=ForceReply(selective=True),
        )


def main() -> None:
    updater = Updater(token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("download", download_files))
    dispatcher.add_handler(CommandHandler("cmd", cmd))
    dispatcher.add_handler(CommandHandler("send", send))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
