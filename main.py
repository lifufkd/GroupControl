#####################################
#            Created by             #
#                SBR                #
#               zzsxd               #
#####################################
import platform
import time
import telebot
from config_parser import ConfigParser
import threading
from backend import TempUserData
####################################################################
config_name = 'secrets.json'
####################################################################


def delete_msg(chat_id, message):
    ss = 0
    while True:
        ss += 1
        if ss == 2:
            msg_id = bot.reply_to(message, config.get_config()['start_msg'], parse_mode='HTML').message_id
        if ss == 40:
            bot.delete_message(chat_id, msg_id)
            break
        time.sleep(1)


def main():

    @bot.message_handler(content_types=["new_chat_members"])
    def foo(message):
        chat_id = message.chat.id
        threading.Thread(target=delete_msg, args=(chat_id, message)).start()

    @bot.message_handler(commands=['change'])
    def tovar_msg(message):
        command = message.text.replace('/', '')
        user_id = message.from_user.id
        if user_id in config.get_config()['admins']:
            temp_data.temp_data(user_id)[user_id][0] = True
            bot.send_message(user_id, 'Введите новые правила группы')

    @bot.message_handler(content_types=['text', 'photo'])
    def text_message(message):
        user_input = message.text
        user_id = message.from_user.id
        if user_id in config.get_config()['admins'] and temp_data.temp_data(user_id)[user_id][0]:
            config.update_start_msg(user_input)
            temp_data.temp_data(user_id)[user_id][0] = False
            bot.send_message(user_id, 'Операция совершена успешно!')

    bot.polling(none_stop=True)


if '__main__' == __name__:
    os_type = platform.system()
    config = ConfigParser(config_name, os_type)
    temp_data = TempUserData()
    bot = telebot.TeleBot(config.get_config()['tg_api'])
    main()
