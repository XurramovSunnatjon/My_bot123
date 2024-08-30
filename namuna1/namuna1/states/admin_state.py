from aiogram.dispatcher.filters.state import State, StatesGroup

class tillarim(StatesGroup):
    bir=State()

class anketa(StatesGroup):
    familiya = State()
    ism = State()
    tug_yili = State()
    manzili = State()
    xizmat = State()
    narxlar = State()
    yubor = State()

class SuperAdminState(StatesGroup):
    SUPER_ADMIN_STATE_MAIN = State()
    SUPER_ADMIN_STATE_GET_ADVERTISEMENT = State()
    SUPER_ADMIN_SEND_MESSAGE_TO_ADMINS = State()
    SUPER_ADMIN_ADD_ADMIN = State()
    SUPER_ADMIN_ADD_FULLNAME = State()
    SUPER_ADMIN_ADD_CHANNEL = State()
    SUPER_ADMIN_UPDATE_CAPTION = State()
    SUPER_ADMIN_UPDATE_PHOTO = State()
