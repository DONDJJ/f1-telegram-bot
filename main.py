import telebot

from config import API_TOKEN, help_message
from keyboard import MainKeyboard
from standings import *

bot = telebot.TeleBot(API_TOKEN)
cur_year = 2021


def change_year(message):
    global cur_year
    try:
        cur_year = int(message.text)
        if not 1957<cur_year<2022:
            raise ValueError
        bot.send_message(message.chat.id, "Текущий год - {}".format(cur_year))
    except ValueError:
        msg = bot.reply_to(message, "Введите число от 1958 до 2021!")
        bot.register_next_step_handler(msg, change_year)


def get_GP(message, href_list):
    try:
        num = int(message.text) - 1
        full_link = 'https://www.formula1.com/' + href_list[num]
        bot.send_message(message.chat.id, get_GP_results(full_link))
    except ValueError:
        exit_list = ['Выход', "Выйти", "Отмена", "отмена", "exit", "Exit", "Cancel", "cancel"]
        if message.text in exit_list:
            bot.send_message(message.chat.id, "Отменяю...")
        else:
            bot.send_message(message.chat.id, "Что-то пошло не по плану, попробуйте еще раз")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, help_message, reply_markup=MainKeyboard)


@bot.message_handler(content_types=['text'])
def ehco_message(message):
    if message.text == "Помощь":
        bot.send_message(message.chat.id, help_message)
    elif message.text == 'Личный зачет':
        bot.send_message(message.chat.id, standings_check('drivers', cur_year))

    elif message.text == 'Кубок конструктуров':
        bot.send_message(message.chat.id, standings_check('team', cur_year))

    elif message.text == 'Список Гран-при':
        races_all = standings_check('races', cur_year)
        bot.send_message(message.chat.id, races_all[0])
        msg = bot.reply_to(message,
                           "Выберите интересующий вас Гран-при (Введите соответствующий номер или 'отмена' для выхода)")
        bot.register_next_step_handler(msg, get_GP, races_all[1])

    elif message.text == "Календарь":
        bot.send_message(message.chat.id, standings_check('calendar', year=cur_year))

    elif message.text == 'Сменить год':
        msg = bot.reply_to(message, "Введите интересующий год (1958-2021)")
        bot.register_next_step_handler(msg, change_year)

try:
    bot.polling(none_stop=True)
except Exception:
    bot.polling(none_stop=True)

# пилот дня последнего вэ
# личный зачет \/
# кубок конструктуров \/
# список гран при => выбрать год => можно выбрать каждый из них
# инфо о пилотах(инсты и проч)
# инфо о командах
# инфо о трассах
# последние новости
