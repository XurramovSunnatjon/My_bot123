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



@dp.callback_query_handler()
async def uzb(call: CallbackQuery,state:FSMContext):
    a = call.data
    print(a)
    if a == "uzb":
        await call.message.delete()
        await call.message.answer("<b>Botdan foydalanish uchun quyidagi tugmalardan foydalaning</b>", reply_markup=uzbek_boss)
    elif a == "ru":
        await call.message.delete()
        await call.message.answer("<b>Для использования бота используйте кнопки ниже</b>", reply_markup=rus_boss)
    elif a == "eng":
        await call.message.delete()
        await call.message.answer("<b>Use the buttons below to use the bot</b>", reply_markup=eng_boss)

@dp.message_handler(Text("📍Manzilimiz"))
async def manzil(message:types.Message):
    await message.answer_location(37.215565, 67.269478)
    await message.answer("<b>Mo'ljal:\nSurxondaryo Viloyat Termiz shaxri ko'p tarmoqli shifoxona yonida</b>")

@dp.message_handler(Text("📍Наш адрес"))
async def manzil(message:types.Message):
    await message.answer_location(37.215565, 67.269478)
    await message.answer("<b>Место назначения:\nРядом с многопрофильной больницей города Термез Сурхандарьинской области</b>")

@dp.message_handler(Text("📍Our address"))
async def manzil(message:types.Message):
    await message.answer_location(37.215565, 67.269478)
    await message.answer("<b>Destination:\nNear the multidisciplinary hospital of the city of Termiz, Surkhandarya Province</b>")



@dp.message_handler(Text("Xizmat narxlari"))
async def manzil(message:types.Message):
    await message.answer_photo("https://t.me/shaxsiy2k/2",caption="<b>Ushbu ro'yxatda markazimizdagi barcha xizmat narxlari haqida bilib olishingiz mumkin</b>")

@dp.message_handler(Text("Цены на услуги"))
async def manzil(message:types.Message):
    await message.answer_photo("https://t.me/shaxsiy2k/2",caption="<b>В этом списке вы можете узнать обо всех ценах на услуги в нашем центре.</b>")

@dp.message_handler(Text("Service prices"))
async def manzil(message:types.Message):
    await message.answer_photo("https://t.me/shaxsiy2k/2",caption="<b>In this list, you can find out about all service prices in our center</b>")




@dp.message_handler(Text("Ish vaqti"))
async def manzil(message:types.Message):
    await message.answer("<b>Shifoxonamizda ish vaqti:\n🌅 Kunduzgi soat 8:00 dan\n🌌Kechqurun soat 17:00 gacha\n🧑‍🍳Tushlik 12:00 dan 13:00 gacha</b>")

@dp.message_handler(Text("Рабочее время"))
async def manzil(message:types.Message):
    await message.answer("<b>График работы в нашей больнице:\n🌅 С 8:00 дня\n🌌Вечером до 17:00\n🧑‍🍳Обед с 12:00 до 13:00.</b>")

@dp.message_handler(Text("Working time"))
async def manzil(message:types.Message):
    await message.answer("<b>Working hours in our hospital:\n🌅 From 8:00 in the afternoon\n🌌Evening until 17:00\n🧑‍🍳Lunch from 12:00 to 13:00</b>")




@dp.message_handler(Text("Operator bilan bog'lanish"))
async def manzil(message:types.Message):
    await message.answer("<b>Operator bilan quyidagi raqam bilan bog'lanishingiz mumkin\n📞+998939778887</b>")

@dp.message_handler(Text("Свяжитесь с оператором"))
async def manzil(message:types.Message):
    await message.answer("<b>Вы можете связаться с оператором по следующему номеру\n📞+998939778887</b>")

@dp.message_handler(Text("Contact the operator"))
async def manzil(message:types.Message):
    await message.answer("<b>You can contact the operator at the following number\n📞+998939778887</b>")



@dp.message_handler(Text("Shifoxonamiz haqida"))
async def manzil(message:types.Message):
    await message.answer_photo("https://t.me/shaxsiy2k/3",caption="<b>Shifoxonamizda turli xildagi tekshiruv apparatlari mavjud:</b>")

@dp.message_handler(Text("О нашей больнице"))
async def manzil(message:types.Message):
    await message.answer_photo("https://t.me/shaxsiy2k/3",caption="<b>В нашей больнице имеются различные виды диагностического оборудования:</b>")

@dp.message_handler(Text("About our hospital"))
async def manzil(message:types.Message):
    await message.answer_photo("https://t.me/shaxsiy2k/3",caption="<b>Our hospital has various types of examination equipment:</b>")




@dp.message_handler(Text("Online qabul"))
async def stas(message:types.Message):
    await message.answer("🇸🇱Familiyangizni kiriting(Lotin harflarda)  \n\n🇷🇺Введите свою фамилию (латинскими буквами)  \n\n🇬🇧Enter your last name (in Latin letters)",reply_markup=ReplyKeyboardRemove())
    await anketa.familiya.set()

@dp.message_handler(Text("Онлайн-прием"))
async def stas(message:types.Message):
    await message.answer("🇸🇱Familiyangizni kiriting(Lotin harflarda)  \n\n🇷🇺Введите свою фамилию (латинскими буквами)  \n\n🇬🇧Enter your last name (in Latin letters)",reply_markup=ReplyKeyboardRemove())
    await anketa.familiya.set()

@dp.message_handler(Text("Online admission"))
async def stas(message:types.Message):
    await message.answer("🇸🇱Familiyangizni kiriting(Lotin harflarda)  \n\n🇷🇺Введите свою фамилию (латинскими буквами)  \n\n🇬🇧Enter your last name (in Latin letters)",reply_markup=ReplyKeyboardRemove())
    await anketa.familiya.set()

@dp.message_handler(state=anketa.familiya)
async def stas1(message:types.Message,state:FSMContext):
    familiya = message.text
    await state.update_data({"familiya": familiya})
    await message.answer("🇸🇱Ismingizni kiriting(Lotin harflarda)  \n\n🇷🇺Введите свое имя (латинскими буквами)   \n\n🇬🇧Enter your name (in Latin letters)")
    await anketa.next()

@dp.message_handler(state=anketa.ism)
async def stas1(message:types.Message,state:FSMContext):
    ism=message.text
    await state.update_data({"ism":ism})
    await message.answer("🇸🇱Tug'ilgan yilingizni kiriting (Masalan 2000-yil 5-yanvarda tug'ilgan bo'lsangiz 05.01.2000 shaklida yozing)\n\n🇷🇺Введите год вашего рождения (Например, если вы родились 5 января 2000 года, напишите его как 05.01.2000)\n\n🇬🇧Enter your year of birth (For example, if you were born on January 5, 2000, write it as 05.01.2000)")
    await anketa.next()

@dp.message_handler(state=anketa.tug_yili)
async def stas1(message:types.Message,state:FSMContext):
    tug_yili=message.text
    await state.update_data({"tug_yili":tug_yili})
    await message.answer("🇸🇱Yashash manzilingizni kiriting (Lotin harflarda)\n\n🇷🇺Введите адрес проживания (латинскими буквами)\n\n🇬🇧Enter your residential address (in Latin letters)")
    await anketa.next()

@dp.message_handler(state=anketa.manzili)
async def stas1(message:types.Message,state:FSMContext):
    manzili=message.text
    await state.update_data({"manzili":manzili})
    await message.answer("🇸🇱Quyidagilardan birini tanlang\n\n🇷🇺Выберите один из следующих\n\n🇬🇧Choose one of the following",reply_markup=xizmatim)
    await anketa.next()

@dp.callback_query_handler(state=anketa.xizmat)
async def stas1(call:types.CallbackQuery,state:FSMContext):
    xizmat=call.data
    await state.update_data({"xizmat":xizmat})
    await call.message.edit_text("🇸🇱Sizning fuqaroligingiz qaysi\n\n🇷🇺Какова ваша национальность?\n\n🇬🇧What is your nationality?",reply_markup=fuqaro)
    await anketa.next()

@dp.callback_query_handler(state=anketa.narxlar)
async def stas1(call:types.CallbackQuery,state:FSMContext):
    narxlar=call.data
    await state.update_data({"narxlar":narxlar})
    await call.message.edit_text("🇸🇱Yuborishni tasdiqlang\n\n🇷🇺Подтвердить отправку\n\n🇬🇧Confirm sending",reply_markup=yubor)
    await anketa.next()


@dp.callback_query_handler(state=anketa.yubor)
async def stas1(call:types.CallbackQuery,state:FSMContext):
    id=call.from_user.id
    yuborish=call.data
    await state.update_data({"yuborish":yuborish})
    data = await state.get_data()
    familiya = data.get("familiya")
    ism = data.get("ism")
    tug = data.get("tug_yili")
    manzili = data.get("manzili")
    xizmat = data.get("xizmat")
    narxlar = data.get("narxlar")
    yuborish = data.get("yuborish")
    if yuborish=="no":
        await call.message.edit_text("<b>So'rovingiz yuborilmadi... \nYana foydalanish uchun /start ni ustiga bosing\n\nВаш запрос не может быть отправлен... \nНажмите /start, чтобы использовать его снова.\n\nYour request could not be sent... \nClick on /start to use it again</b>")
    elif yuborish == "yes":
        n=int(xizmat)
        text=""
        text= f"\n<b>Familiyasi:   {familiya}</b>\n"
        text = text + f"<b>Ismi:   {ism}</b>\n"
        text = text + f"<b>Tug'ilgan yili:   {tug}</b>\n"
        text = text + f"<b>Manzili:   {manzili}</b>\n"
        if narxlar =="uzbek":
            text = text + f"<b>Xizmatni hisoblash turi :  O'zbekiston fuqarosi uchun </b>\n"
        else:
            text = text + f"<b>Xizmatni hisoblash turi :  Chet el fuqarosi uchun </b>\n"


        a = xizmatlar["xizmat"]
        k=0
        for x in a:
            k+=1
            if k == n:
                text = text + f"<b>Xizmat turi:   {x} </b>\n"
        yubor2 = InlineKeyboardMarkup(row_width=2)
        yubor2.add(InlineKeyboardButton(text="Yuborish", callback_data=f"haha_{id}"))
        yubor2.add(InlineKeyboardButton(text="Bekor qilish", callback_data=f"yooq_{id}"))
        await call.message.edit_text("<b>So'rovingiz adminga yuborildi... \nYana foydalanish uchun /start ni ustiga bosing\n\nВаш запрос отправлен администратору... \nНажмите /start, чтобы использовать его снова.\n\nYour request has been sent to admin... \nClick on /start to use it again</b>")
        await bot.send_message(chat_id=ADMINS[0],text=text,reply_markup=yubor2)
    await state.finish()



