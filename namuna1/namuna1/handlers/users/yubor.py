from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import ADMINS
from filters import IsUser, IsSuperAdmin, IsGuest
from filters.admins import IsAdmin
from keyboards.inline.main_menu_super_admin import main_menu_for_super_admin, main_menu_for_admin, tillar, xizmatim,fuqaro,yubor, xizmatlar
from keyboards.default.tugmalar import uzbek_boss, rus_boss, eng_boss
from loader import dp, db, bot
from states.send_chanell import SuperAdminStateChannel
from states.admin_state import tillarim, anketa
from aiogram.dispatcher.filters.builtin import Text
@dp.callback_query_handler(IsSuperAdmin(),state="*")
async def uzbsres(call:CallbackQuery,state:FSMContext):

    if call.data.split("_")[0]=="yooq":
        await bot.send_message(chat_id=int(call.data.split("_")[1]), text="So'rovingiz bekor qilindi")
        await call.message.edit_text("Bekor qilish haqidagi xabaringiz yuborildi")
    elif call.data.split("_")[0]=="haha":
        await call.message.edit_text(call.message.text+"\n\n\nMarkazga kelish uchun aniq vaqtni yozing\nMasalan:Shanba kuni soat 13:30 da")
        await tillarim.bir.set()
        await state.update_data({"id": call.data.split("_")[1]})
        await bot.send_message(chat_id=int(call.data.split("_")[1]), text="Sorovingiz qabul qilindi")
@dp.message_handler(state=tillarim.bir)
async def uzres(message:types.Message,state:FSMContext):
    a=message.text
    data = await state.get_data()
    id = data.get("id")
    await bot.send_message(chat_id=int(id),text=a)
    await message.answer("Xabaringiz yuborildi")
    await state.finish()