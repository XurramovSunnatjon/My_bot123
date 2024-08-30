from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

uzbek_boss=ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
uzbek_boss.add(
    KeyboardButton(text="Shifoxonamiz haqida"),
        KeyboardButton(text="Online qabul"),
        KeyboardButton(text="Xizmat narxlari"),
        KeyboardButton(text="Ish vaqti"),
        KeyboardButton(text="📍Manzilimiz"),
        KeyboardButton(text="Operator bilan bog'lanish")
)

rus_boss=ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

rus_boss.add(
    KeyboardButton(text="О нашей больнице"),
        KeyboardButton(text="Онлайн-прием"),
        KeyboardButton(text="Цены на услуги"),
        KeyboardButton(text="Рабочее время"),
        KeyboardButton(text="📍Наш адрес"),
        KeyboardButton(text="Свяжитесь с оператором")
)

eng_boss=ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
eng_boss.add(
    KeyboardButton(text="About our hospital"),
        KeyboardButton(text="Online admission"),
        KeyboardButton(text="Service prices"),
        KeyboardButton(text="Working time"),
        KeyboardButton(text="📍Our address"),
        KeyboardButton(text="Contact the operator")
)
