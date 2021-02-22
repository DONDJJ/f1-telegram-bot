from telebot import types

MainKeyboard = types.ReplyKeyboardMarkup()
help_key = types.KeyboardButton("Помощь")
drivers_standing = types.KeyboardButton("Личный зачет")
constructors_standing = types.KeyboardButton("Кубок конструктуров")
grand_prix = types.KeyboardButton("Список Гран-при")
change_year = types.KeyboardButton('Сменить год')
calendar = types.KeyboardButton("Календарь")

MainKeyboard.add(help_key,
                 drivers_standing,
                 constructors_standing,
                 grand_prix,
                 change_year,
                 calendar)
