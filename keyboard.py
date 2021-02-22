import telebot

MainKeyboard = telebot.types.ReplyKeyboardMarkup()
help_key = telebot.types.KeyboardButton("Помощь")
drivers_standing = telebot.types.KeyboardButton("Личный зачет")
constructors_standing = telebot.types.KeyboardButton("Кубок конструктуров")
grand_prix = telebot.types.KeyboardButton("Список Гран-при")
change_year = telebot.types.KeyboardButton('Сменить год')
calendar = telebot.types.KeyboardButton("Календарь")

MainKeyboard.add(help_key,
                 drivers_standing,
                 constructors_standing,
                 grand_prix,
                 change_year,
                 calendar)
