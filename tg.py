#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards.
"""
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters,ConversationHandler
from search import get_coord
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

with open('token.txt') as f:
    TOKEN = f.read().strip()

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
    #chat_id = update.message.chat_id
    text = update.message.text
    print(text)
    output = get_coord(text)
    print(output)
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


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    #updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(conv_handler)
    #updater.dispatcher.add_handler(CommandHandler('stop', stop))
    #updater.dispatcher.add_handler(MessageHandler(Filters.text, sort_input))
    #updater.dispatcher.add_handler(MessageHandler(Filters.text, to_search))
    #updater.dispatcher.add_handler(CallbackQueryHandler(callback=sort_input))
    #updater.dispatcher.add_handler(CallbackQueryHandler(callback=get_main_menu_keyboard))
    #updater.dispatcher.add_handler(CommandHandler('help', help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
