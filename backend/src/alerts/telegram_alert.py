import logging
import os
import telebot
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


load_dotenv()


class TelegramAlert:
    def __init__(self):
        self.bot = telebot.TeleBot(os.getenv('TELEGRAM_TOKEN'), 'None')

    def send_alert_in_chat(self, text, chat_id=None):
        chat_id = chat_id if chat_id else os.getenv('CHAT_ID')
        try:
            logger.debug(f'Starting to send notification with text: {text}')
            self.bot.send_message(chat_id=chat_id, text=text)
            logger.debug(f'Successfully sent notification with text: {text}')
        except Exception as e:
            logger.error(f'Error while sending notification in telegram, message: {text}, error: {e}')
