#####################################
#            Created by             #
#                SBR                #
#               zzsxd               #
#####################################
import platform
import telebot
from config_parser import ConfigParser
from backend import TempUserData
####################################################################
config_name = 'secrets.json'
####################################################################


def main():

    @bot.message_handler(content_types=["new_chat_members"])
    def foo(message):
        print(1)
        bot.reply_to(message, config.get_config()['start_msg'], parse_mode='HTML')

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
        print(3)
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
