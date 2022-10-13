Small python code which can be handy when using telegram and you don't want to use VPS again and again.
By configuring the code in your VPS,
You can execute commands and get your output within telegram.
It can also be very useful in performing Recon.

## How to Get configs:
- ### Token - Your personal bots token
    - Goto @BotFather and create newbot, you will be given a unique token.
    - Replace the token with value XXXX on config.json with the unique API Token

- ### Tgid - It's the user that's only authenticated to run commands in Telegram
    - Send "/id" to @MissRose_bot to recieve your chat id to be used for authentication.
    - Replace the chat id with value YYYY in config.json.

## Installation
    Get the configs following the above Sections first 
- ### Normal Installation
    - Clone this repo and navigate to the project directory and install requirements by: `pip3 install -r requirements.txt`
    - Or you can also paste this one-liner : 
    - ```
       git clone https://github.com/V35HR4J/Automate-Telegram && cd Automate-Telegram && pip3 install -r requirements.txt && nano config.json
      ```
    - Replace the token with value XXXX with your unique API Token.
    - Run the program with `python3 main.py`
    - You are ready to go, type `/start` on bot's DM to get started.

   
- ### Docker Installation
    - Clone this repo and navigate to project directory. 
    - Run `docker build -t automate-telegram .`
    - Run `docker run -d automate-telegram`

## Commands available:

1. /cmd [Command]
2. /send [DesiredFilename]
3. /download [FileUrl]

## Watch the video:

[![Watch the video](https://i.imgur.com/yotnyJZ.jpeg)](https://youtu.be/cpdY3bkFBuY)

Let me know if i need to provide video tutorial for setup, I will be more than happy to help you out.

Pull Requests are also appreciated if you have idea to improve. 🙂
