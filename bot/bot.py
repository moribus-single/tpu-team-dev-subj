from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from dotenv import load_dotenv
import logging
import os

from handlers import handle_msg

if __name__ == "__main__":
    # Load all the variables from environment
    load_dotenv()

    # Getting token, provided by BotFather
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    if TOKEN is None:
        raise EnvironmentError("Telegram token is not provided.")

    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Initializing bot
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot=bot)

    # some handlers
    # ...

    executor.start_polling(dp, skip_updates=True)
