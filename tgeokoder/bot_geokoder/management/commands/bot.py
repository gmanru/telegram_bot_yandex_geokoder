from django.core.management.base import BaseCommand
from django.conf import settings


import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters,ConversationHandler

from telegram.utils.request import Request

from search import get_coord
from bot_geokoder.models import Profile, Result

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


MENU,SEARCH,HISTORY = range(3)

BUTTON_SEARCH = 'Новый поиск' 
BUTTON_HISTORY = 'История'


def start(update, context):
    #update.message.reply_text('Привет!')
    reply_keyboard = [[BUTTON_SEARCH, BUTTON_HISTORY]]

    update.message.reply_text('Привет!',reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return MENU 

def sort_input(update, contex):
    chat_id = update.message.chat_id
    current_text = update.message.text
    if current_text == BUTTON_SEARCH:
        #print('кнопка тыкнута')
        update.message.reply_text('Введите адрес?', reply_markup=ReplyKeyboardRemove())
        #to_search(update, context)
        return SEARCH 
    elif current_text == BUTTON_HISTORY:
        pass
    else:
        update.message.reply_text('Ну как хочешь...')
        return ConversationHandler.END

def to_search(update, context):
    #update.message.reply_text('Введите запрос на поиск')
    chat_id = update.message.chat_id
    text = update.message.text
    print(text)
    output = get_coord(text)
    print(output)
    p, _ = Profile.objects.get_or_create(
    user_id=chat_id,)
    #defaults={
    #    'request': update.message.from_user.username,})
    return ConversationHandler.END 



def stop(update, context):
    update.message.reply_text("Жаль. А было бы интересно пообщаться. Хорошего дня!")
    return ConversationHandler.END

conv_handler = ConversationHandler(
    # Точка входа в диалог.
    # В данном случае — команда /start. Она задаёт первый вопрос.
    entry_points=[CommandHandler('start', start)],
    
    # Словарь состояний внутри диалога. 
    # Наш вариант с двумя обработчиками,
    # фильтрующими текстовые сообщения.
    states={
    # Функция читает ответ на первый вопрос и задаёт второй.
    MENU: [MessageHandler(Filters.regex('^(Новый поиск|История)$'), sort_input)],
    # Функция читает ответ на второй вопрос и завершает диалог.
    SEARCH: [MessageHandler(Filters.text, to_search)]
    },
    
    # Точка прерывания диалога. В данном случае — команда /stop.
    fallbacks=[CommandHandler('stop', stop)]
)






class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        # 1 -- правильное подключение

        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
        updater = Updater(settings.TOKEN, use_context=True)
        updater.dispatcher.add_handler(conv_handler)

        updater.start_polling()
        updater.idle()