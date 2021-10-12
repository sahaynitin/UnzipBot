from unzipbot import app
from Config import Config
from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = "Hey {}. \n\nWelcome to {} \n\nI can unzip & unrar files you send me and upload them to your private chat. \nI will also total the contents & number of files."

    if Config.OWNER_ID != 0:
        if Config.OWNER_NAME:
            START += (
                f"\n\nMy Owner :- [{Config.OWNER_NAME}](tg://user?id={Config.OWNER_ID})"
            )
        else:
            print(
                "You added OWNER_ID but not OWNER_NAME. You need to put both or neithers"
            )
            print("Quitting the bot")
            raise SystemExit
    else:
        START += f"\n\nMade With 💕 By @Tellybots_4u"

    # About Message
    ABOUT = "**About This Bot** \n\nA Telegram Unzipper bot by Tellybots_4u \n\n👲 Maintained By : [Tellybots4u](https://t.me/tellybots_4u) \n\n🗃️ Framework : [Pyrogram](docs.pyrogram.org) \n\n📚 Language : [Python](www.python.org) \n\n🧒 Developer : [TellyBots4u](https://t.me/tellybots_4u)"

    if Config.OWNER_ID != 0:
        if Config.OWNER_NAME:
            ABOUT += (
                f"\n\nMy Owner :- [{Config.OWNER_NAME}](tg://user?id={Config.OWNER_ID})"
            )
        else:
            print(
                "You added OWNER_ID but not OWNER_NAME. You need to put both or neither"
            )
            print("Quitting the bot")
            raise SystemExit

    # Deploy Message
    DEPLOY = """
**Wanna create your own such bot??** 

This is simple and open source bot. 
Just click below on source code and tap on "Deploy to Heroku" to create your own bot. 

Click Here for [Source Code](https://github.com/sahaynitin/UnzipBot)
"""
    
    HELP = """
**Need Help ?? **

Send any zip/rar file then choose a mode and your work is done! 
I'll unzip/unrar it and return you it's contents.

**Available Commands** :-
/modes - Know about both modes.
/about - About this bot and source code.
/help - This Message.
/start - Check if bot is alive.

**📡 Update Channel** - @Tellybots_4u
"""
    
    MODES = """
**What are Modes ❔**

1) **Tortoise 🐢**
Bit Slow but Steady. 

While using this mode you will can be notified about the all progresses happening.

Progresses include:
- downloaded so far
- contents in provided file
- number of files in provided file
- uploaded too far with number of the file being uploaded

It doesn't take too much time than other mode and is the recommended method. 

2) ** Rabbit 🐇**
Bit Fast but less user friendly.

While using this mode you won't be notified about any progresses that go on. Just download completion and upload completion will be notified. 

This is bit fast but only recommended for larger files as smaller files won't have much time difference.   
    """

    CHOOSE_MODE = "**CHOOSE MODE ** \n\nChoose a mode from below to start extracting files..."

    # Home Button
    home_button = [[InlineKeyboardButton(text="🏡 Return Home", callback_data="home")]]

    # Modes Buttons

    modes_buttons = [
        [
            InlineKeyboardButton("Tortoise 🐢", callback_data="tortoise"),
            InlineKeyboardButton("Rabbit 🐇", callback_data="rabbit")
        ],
        [InlineKeyboardButton("What are Modes❔", callback_data="modes")]
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("What are Modes ❔", callback_data="modes"),
            InlineKeyboardButton("📤 About 📤", callback_data="about"),
        ],
        [InlineKeyboardButton("How to Use me ❔", callback_data="help")],
        [InlineKeyboardButton("Create Your Own Bot", callback_data="deploy")],
        [InlineKeyboardButton("📡 Update Channel", url="https://t.me/tellybots_4u")],
        [InlineKeyboardButton("💬 Support Group", url="https://t.me/tellybots_support")],
    ]
