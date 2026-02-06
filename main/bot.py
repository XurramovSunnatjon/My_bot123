import asyncio
import logging
import aiosqlite
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramBadRequest

# --- SOZLAMALAR ---
API_TOKEN = '8441382946:AAGwDXAy7yQPmR_5k50XUIFsEroGhif1aGE'
ADMIN_ID =  5469329743 # O'zingizni raqamli ID'ingizni yozing

# --- BAZA BILAN ISHLASH ---
DB_PATH = "bot_database.db"

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY)")
        await db.execute("CREATE TABLE IF NOT EXISTS channels (id INTEGER PRIMARY KEY AUTOINCREMENT, ch_id TEXT, url TEXT)")
        await db.commit()

# --- ADMIN HOLATLARI ---
class AdminStates(StatesGroup):
    waiting_for_channel = State()

# --- BOTNI SOZLASH ---
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

# --- FUNKSIYALAR ---
async def check_sub(user_id):
    """Obunani tekshirish: Agar hammasiga a'zo bo'lsa bo'sh ro'yxat qaytaradi"""
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT ch_id, url FROM channels") as cursor:
            channels = await cursor.fetchall()
    
    not_subscribed = []
    for ch_id, url in channels:
        try:
            member = await bot.get_chat_member(chat_id=ch_id, user_id=user_id)
            if member.status not in ["member", "administrator", "creator"]:
                not_subscribed.append(url)
        except Exception:
            not_subscribed.append(url)
    return not_subscribed

# --- HANDLERLAR ---

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # Foydalanuvchini bazaga qo'shish
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (message.from_user.id,))
        await db.commit()
        bttn= ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="Qur'oni Karim"), KeyboardButton(text="Qur'oni Karim audiolari")]
        ], resize_keyboard=True)
    # Obunani tekshirish
    unsub = await check_sub(message.from_user.id)
    if unsub:
        btns = [[InlineKeyboardButton(text=f"Kanal {i+1}", url=url)] for i, url in enumerate(unsub)]
        btns.append([InlineKeyboardButton(text="Tekshirish ✅", callback_data="recheck")])
        kb = InlineKeyboardMarkup(inline_keyboard=btns)
        return await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling:", reply_markup=kb)   
    await message.answer(f"Xush kelibsiz! Bot xizmatlaridan foydalanishingiz mumkin.", reply_markup=bttn)

@dp.callback_query(F.data == "recheck")
async def recheck(call: types.CallbackQuery):
    unsub = await check_sub(call.from_user.id)
    if not unsub:
        await call.message.edit_text("Tabriklaymiz, obuna tasdiqlandi! Endi botdan foydalanishingiz mumkin.")
    else:
        await call.answer("Siz hali hamma kanallarga a'zo bo'lmadingiz ❌\nBotdan foydalanish uchun kanallarga obuna bo'ling!", show_alert=True)

class QuranStates(StatesGroup):
    state_for_sura = State()
    state_for_sura_uz = State()
    state_for_sura_ru = State()
    state_for_sura_oyat = State()
    state_for_sura_oyat_uz = State()
    state_for_sura_oyat_ru = State()
    state_for_juz = State()
    state_for_juz_uz = State()
    state_for_juz_ru = State()

import requests
# --- QUR'ONI KARIM api---

raqam = [7,286,200,176,120,165,206,75,129,109,123,111,43,52,99,
         128,111,110,98,135,112,78,118,64,77,227,93,88,69,60,34,
         30,73,54,45,83,182,88,75,85,54,53,89,59,37,35,38,29,18,
         45,60,49,62,55,78,96,29,22,24,13,14,11,11,18,12,12,30,52,
         52,44,28,28,20,56,40,31,50,40,46,42,29,19,36,25,22,17,19,
         26,30,20,15,21,11,8,8,19,5,8,8,11,11,8,3,9,5,4,7,3,6,3,5,4,5,6]
         
def oyat_uchun_uz(sura,oyat):
  try:
    a=f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/ara-qurandoorinonun/{sura}/{oyat}.json'
    a1=f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/{sura}/{oyat}.json'
    r=requests.get(a)
    r1=requests.get(a1)
    t=str(sura)+':'+str(oyat)+'\n '+r.json()['text']+'\n\n'+str(sura)+':'+str(oyat)+'\n '+r1.json()['text']
    return t
  except:
    text='Xato'
    return text
  
def oyat_uchun(sura,oyat):
  try:
    a=f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/ara-qurandoorinonun/{sura}/{oyat}.json'
    r=requests.get(a)
    t=str(sura)+':'+str(oyat)+'\n '+r.json()['text']
    return t
  except:
    text='Xato'
    return text  

def oyat_uchun_ru(sura,oyat):
  try:
    a=f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/ara-qurandoorinonun/{sura}/{oyat}.json'
    r=requests.get(a)
    a1=f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/rus-abuadel/{sura}/{oyat}.json'
    r1=requests.get(a1)
    t= str(sura)+':'+str(oyat)+'\n '+r.json()['text']+'\n\n'+str(sura)+':'+str(oyat)+'\n '+r1.json()['text']
    return t
  except:
    text='Xato'
    return text
    
def sura_uchun_uz(sura):
  n=raqam[sura-1]
  try:
    text=''
    a=f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/ara-qurandoorinonun/{sura}.json'
    a1=f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/{sura}.json'
    r=requests.get(a)
    r1=requests.get(a1)
    for i in range(n):
      text=text+str(i+1)+'. '+r.json()['chapter'][i]['text']+'\n\n'+str(i+1)+'. '+r1.json()['chapter'][i]['text']+'\n\n'
    return text  
  except:
    text='Xato'
    return text  
def sura_uchun(sura):
  n=raqam[sura-1]
  try:
    text=''
    a=f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/ara-qurandoorinonun/{sura}.json'
    r=requests.get(a)
    for i in range(n):
      text=text+str(i+1)+'. '+r.json()['chapter'][i]['text']+'\n\n'
    return text  
  except:
    text='Xato'
    return text

def sura_uchun_ru(sura):
    n=raqam[sura-1]
    try:
        text=''
        a=f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/ara-qurandoorinonun/{sura}.json"
        a1=f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/rus-abuadel/{sura}.json'
        r=requests.get(a)
        r1=requests.get(a1)
        for i in range(n):
            text=text+str(i+1)+'. '+r.json()['chapter'][i]['text']+'\n\n'+str(i+1)+'. '+r1.json()['chapter'][i]['text']+'\n\n'
        return text  
    except:
        text='Xato'
        return text
    


def juz_uchun_uz(juz):
  try:
    a1=f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/juzs/{juz}.json'  
    a=f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/ara-qurandoorinonun/juzs/{juz}.json'
    r=requests.get(a)
    r1=requests.get(a1)
    text=''
    for i,j in zip(r.json()['juzs'],r1.json()['juzs']):
      text=text+str(i['chapter'])+':'+str(i['verse'])+'\n '+i['text']+'\n\n'+str(j['chapter'])+':'+str(j['verse'])+'\n '+j['text']+'\n\n'
    return text  
  except:
    text='Xato'
    return text  
def juz_uchun(juz):
  try:
    a=f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/ara-qurandoorinonun/juzs/{juz}.json'
    r=requests.get(a)
    text=''
    for i in r.json()['juzs']:
      text=text+str(i['chapter'])+':'+str(i['verse'])+'\n '+i['text']+'\n\n'
    return text  
  except:
    text='Xato'
    return text
def juz_uchun_ru(juz):
    try:
        a=f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/ara-qurandoorinonun/juzs/{juz}.json'
        a1=f'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/rus-abuadel/juzs/{juz}.json'
        r=requests.get(a)
        r1=requests.get(a1)
        text=''
        for i,j in zip(r.json()['juzs'],r1.json()['juzs']):
            text=text+str(i['chapter'])+':'+str(i['verse'])+'\n '+i['text']+'\n\n'+str(j['chapter'])+':'+str(j['verse'])+'\n '+j['text']+'\n\n'
        return text  
    except:
        text='Xato'
        return text    
  
def split_text(text, limit=4096):
    chunks = []
    if len(text) <= limit:
        return [text]
    paragraphs = text.split('\n\n')
    current_chunk = ""
    for paragraph in paragraphs:
        if len(paragraph) > limit:
            if current_chunk:
                chunks.append(current_chunk.strip())
            for i in range(0, len(paragraph), limit):
                chunks.append(paragraph[i:i+limit])
            current_chunk = ""
            continue
        if len(current_chunk) + len(paragraph) + 2 <= limit:
            current_chunk += (paragraph + '\n\n')
        else:
            chunks.append(current_chunk.strip())
            current_chunk = paragraph + '\n\n'   
    if current_chunk:
        chunks.append(current_chunk.strip())   
    return chunks  

# --- QUR'ONI KARIM AUDIOLARI ---
qorilar = [
    "Abdulbosit Abdussomad (Murattal)", "Abdulbosit Abdussomad (Mujavvad)",
    "Mahmud Halil Husoriy (Muallim)", "Mahmud Halil Husoriy (Murattal) 01",
    "Mahmud Halil Husoriy (Murattal)", "Mahmud Halil Husoriy (Mujavvad)",
    "Muhammad Siddiq Minshaviy", "Muhammad Siddiq Minshaviy (Mujavvad)",
    "Muhammad Siddiq Minshaviy Shogirdi bilan", "Doktor Ayman Rushdiy Suvayd",
    "Mishariy Roshid al-Afasiy", "Abdulbosit Qori Qobilov",
    "Abu Bakr Ash-Shatriy", "Nosir Al-Qatamiy", "Ahmad Al-Ajmiy",
    "Maher Al-Muaiqli", "Hani Ar-Rifai", "Khalifa al-Tunaiji",
    "Abdurrohman As-Sudays", "Saad al-G‘omidiy", "Hasanxon va Husayinxon",
    "Saud Ash-Shuraim", "Muhammad al-Luhaidan", "Muhammad al-Kurdiy",
    "Muhammad al-Kurdiy 2", "Yaser al-Dossari", "Muhammad Hodiy Turiy",
    "Abdurrohman al-Usiy", "Abdurroshid al-Sufi", "Idris Abkar",
    "Abdurrohman al-Huzayfiy", "Muhammad Jibril", "Gassan al-Shorbajiy",
    "Wadee al-Yamani", "Afzal Rafiqov"
]
quron_buttons = [[InlineKeyboardButton(text=name, callback_data=f"quran{i}")] for i, name in enumerate(qorilar, start=1)]
quron_button = InlineKeyboardMarkup(inline_keyboard=quron_buttons)
   
qorilar_dict = {"quran1": range(413, 527), "quran2": range(3233, 3347), "quran3": range(4312, 4426), "quran4": range(4430, 4544),
                "quran5": range(873, 987), "quran6": range(988, 1102), "quran7": range(643, 757), "quran8": range(758, 872),
                "quran9": range(2470, 2584), "quran10": range(3351, 3465), "quran11": range(1104, 1219), "quran12": range(3001, 3115),
                "quran13": range(1510, 1624), "quran14": range(1625, 1739), "quran15": range(1740, 1854), "quran16": range(1856, 1970),
                "quran17": range(2125, 2239), "quran18": range(2240, 2354), "quran19": range(2355, 2469), "quran20": range(3466, 3580),
                "quran21": range(2585, 2699), "quran22": range(2700, 2814), "quran23": range(2815, 2929), "quran24": range(4067, 4180),
                "quran25": range(4790, 4895), "quran26": range(3825, 3939), "quran27": range(4930, 5044), "quran28": range(5045, 5159),
                "quran29": range(5160, 5274), "quran30": range(5275, 5391), "quran31": range(5392, 5506), "quran32": range(3709, 3823),
                "quran33": range(3116, 3230), "quran34": range(3941, 4055), "quran35": range(3594, 3708)}

bbtn= ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="sura"), KeyboardButton(text="oyat")], [KeyboardButton(text="juz"), KeyboardButton(text="Orqaga")]  
        ], resize_keyboard=True)
bsura= ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="sura-arab"), KeyboardButton(text="sura-uz")], [KeyboardButton(text="sura-ru"), KeyboardButton(text="Orqaga")]], resize_keyboard=True)
boyat= ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="oyat-arab"), KeyboardButton(text="oyat-uz")], [KeyboardButton(text="oyat-ru"), KeyboardButton(text="Orqaga")]], resize_keyboard=True)    
bjuz= ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="juz-arab"), KeyboardButton(text="juz-uz")], [KeyboardButton(text="juz-ru"), KeyboardButton(text="Orqaga")]], resize_keyboard=True)

@dp.message(F.text=="Qur'oni Karim")
async def echo_all(message: types.Message):
    await message.answer("Assalomu alaykum! Siz Qur'oni Karim bo'limidasiz. Quyidagilardan birini tanlang",reply_markup=bbtn)

@dp.message(F.text=="sura")
async def echo_all(message: types.Message, state: FSMContext):
    await message.answer("Quyidagilardan birini tanlang", reply_markup=bsura)

@dp.message(F.text=="sura-arab")
async def echo_all(message: types.Message, state: FSMContext):
    await message.answer("Sura raqamini kiriting (1 dan 114 gacha): \nMasalan: 2 (Al-Baqara)")
    await state.set_state(QuranStates.state_for_sura)

@dp.message(F.text=="sura-uz")
async def echo_all(message: types.Message, state: FSMContext):
    await message.answer("Sura raqamini kiriting (1 dan 114 gacha): \nMasalan: 2 (Al-Baqara)")
    await state.set_state(QuranStates.state_for_sura_uz)

@dp.message(F.text=="sura-ru")
async def echo_all(message: types.Message, state: FSMContext):
    await message.answer("Sura raqamini kiriting (1 dan 114 gacha): \nMasalan: 2 (Al-Baqara)")
    await state.set_state(QuranStates.state_for_sura_ru)

@dp.message(QuranStates.state_for_sura)
async def process_sura(message: types.Message, state: FSMContext):
    try:
        sura_num = int(message.text)
        if 1 <= sura_num <= 114:
            text = sura_uchun(sura_num)
            text_chunks = split_text(text)
            for chunk in text_chunks:
                if chunk:
                    await message.answer(chunk)
        else:
            await message.answer("Iltimos, 1 dan 114 gacha bo'lgan son kiriting.")
    except ValueError:
        await message.answer("Iltimos, to'g'ri son kiriting.")
    await state.clear()

@dp.message(QuranStates.state_for_sura_uz)
async def process_sura_uz(message: types.Message, state: FSMContext):
    try:
        sura_num = int(message.text)
        if 1 <= sura_num <= 114:
            text = sura_uchun_uz(sura_num)
            text_chunks = split_text(text)
            for chunk in text_chunks:
                if chunk:
                    await message.answer(chunk)
        else:
            await message.answer("Iltimos, 1 dan 114 gacha bo'lgan son kiriting.")
    except ValueError:
        await message.answer("Iltimos, to'g'ri son kiriting.")
    await state.clear()

@dp.message(QuranStates.state_for_sura_ru)
async def process_sura_ru(message: types.Message, state: FSMContext):
    try:
        sura_num = int(message.text)
        if 1 <= sura_num <= 114:
            text = sura_uchun_ru(sura_num)
            text_chunks = split_text(text)
            for chunk in text_chunks:
                if chunk:
                    await message.answer(chunk)
        else:
            await message.answer("Iltimos, 1 dan 114 gacha bo'lgan son kiriting.")
    except ValueError:
        await message.answer("Iltimos, to'g'ri son kiriting.")
    await state.clear()


@dp.message(F.text=="juz")
async def echo_all(message: types.Message, state: FSMContext):
    await message.answer("Quyidagilardan birini tanlang", reply_markup=bjuz)

@dp.message(F.text=="juz-arab")
async def echo_all(message: types.Message, state: FSMContext):
    await message.answer("Juz raqamini kiriting (1 dan 30 gacha): \nMasalan: 1")
    await state.set_state(QuranStates.state_for_juz)
@dp.message(F.text=="juz-uz")
async def echo_all(message: types.Message, state: FSMContext):
    await message.answer("Juz raqamini kiriting (1 dan 30 gacha): \nMasalan: 1")
    await state.set_state(QuranStates.state_for_juz_uz)
@dp.message(F.text=="juz-ru")
async def echo_all(message: types.Message, state: FSMContext):
    await message.answer("Juz raqamini kiriting (1 dan 30 gacha): \nMasalan: 1")
    await state.set_state(QuranStates.state_for_juz_ru)

@dp.message(QuranStates.state_for_juz)
async def process_juz(message: types.Message, state: FSMContext):
    try:
        juz_num = int(message.text)
        if 1 <= juz_num <= 30:
            text = juz_uchun(juz_num)
            text_chunks = split_text(text)
            for chunk in text_chunks:
                if chunk:
                    await message.answer(chunk)
        else:
            await message.answer("Iltimos, 1 dan 30 gacha bo'lgan son kiriting.")
    except ValueError:
        await message.answer("Iltimos, to'g'ri son kiriting.")
    await state.clear()
@dp.message(QuranStates.state_for_juz_uz)
async def process_juz_uz(message: types.Message, state: FSMContext):
    try:
        juz_num = int(message.text)
        if 1 <= juz_num <= 30:
            text = juz_uchun_uz(juz_num)
            text_chunks = split_text(text)
            for chunk in text_chunks:
                if chunk:
                    await message.answer(chunk)
        else:
            await message.answer("Iltimos, 1 dan 30 gacha bo'lgan son kiriting.")
    except ValueError:
        await message.answer("Iltimos, to'g'ri son kiriting.")
    await state.clear()
@dp.message(QuranStates.state_for_juz_ru)
async def process_juz_ru(message: types.Message, state: FSMContext):
    try:
        juz_num = int(message.text)
        if 1 <= juz_num <= 30:
            text = juz_uchun_ru(juz_num)
            text_chunks = split_text(text)
            for chunk in text_chunks:
                if chunk:
                    await message.answer(chunk)
        else:
            await message.answer("Iltimos, 1 dan 30 gacha bo'lgan son kiriting.")
    except ValueError:
        await message.answer("Iltimos, to'g'ri son kiriting.")
    await state.clear()            

@dp.message(F.text=="oyat")
async def echo_all(message: types.Message, state: FSMContext):
    await message.answer("Quyidagilardan birini tanlang", reply_markup=boyat)

@dp.message(F.text=="oyat-arab")
async def echo_all(message: types.Message, state: FSMContext):
    await message.answer("Sura va oyat raqamlarini kiriting (masalan: 2 255):")
    await state.set_state(QuranStates.state_for_sura_oyat)
@dp.message(F.text=="oyat-uz")
async def echo_all(message: types.Message, state: FSMContext):
    await message.answer("Sura va oyat raqamlarini kiriting (masalan: 2 255):")
    await state.set_state(QuranStates.state_for_sura_oyat_uz)
@dp.message(F.text=="oyat-ru")
async def echo_all(message: types.Message, state: FSMContext):
    await message.answer("Sura va oyat raqamlarini kiriting (masalan: 2 255):")
    await state.set_state(QuranStates.state_for_sura_oyat_ru)


@dp.message(QuranStates.state_for_sura_oyat)
async def process_sura_oyat(message: types.Message, state: FSMContext):
    try:
        parts = message.text.split()
        if len(parts) != 2:
            raise ValueError("Iltimos, faqat ikkita son kiriting.")
        sura_num = int(parts[0])
        oyat_num = int(parts[1])
        if 1 <= sura_num <= 114 and 1 <= oyat_num <= raqam[sura_num - 1]:
            text = oyat_uchun(sura_num, oyat_num)
            await message.answer(text)
        else:
            await message.answer("Iltimos, to'g'ri sura va oyat raqamlarini kiriting.")
    except ValueError:
        await message.answer("Iltimos, to'g'ri sonlarni kiriting.")
    await state.clear()
@dp.message(QuranStates.state_for_sura_oyat_uz)
async def process_sura_oyat_uz(message: types.Message, state: FSMContext):
    try:
        parts = message.text.split()
        if len(parts) != 2:
            raise ValueError("Iltimos, faqat ikkita son kiriting.")
        sura_num = int(parts[0])
        oyat_num = int(parts[1])
        if 1 <= sura_num <= 114 and 1 <= oyat_num <= raqam[sura_num - 1]:
            text = oyat_uchun_uz(sura_num, oyat_num)
            await message.answer(text)
        else:
            await message.answer("Iltimos, to'g'ri sura va oyat raqamlarini kiriting.")
    except ValueError:
        await message.answer("Iltimos, to'g'ri sonlarni kiriting.")
    await state.clear()
@dp.message(QuranStates.state_for_sura_oyat_ru)
async def process_sura_oyat_ru(message: types.Message, state: FSMContext):
    try:
        parts = message.text.split()
        if len(parts) != 2:
            raise ValueError("Iltimos, faqat ikkita son kiriting.")
        sura_num = int(parts[0])
        oyat_num = int(parts[1])
        if 1 <= sura_num <= 114 and 1 <= oyat_num <= raqam[sura_num - 1]:
            text = oyat_uchun_ru(sura_num, oyat_num)
            await message.answer(text)
        else:
            await message.answer("Iltimos, to'g'ri sura va oyat raqamlarini kiriting.")
    except ValueError:
        await message.answer("Iltimos, to'g'ri sonlarni kiriting.")
    await state.clear()        

@dp.message(F.text=="Orqaga")
async def echo_all(message: types.Message):
    bttn= ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="Qur'oni Karim"), KeyboardButton(text="Qur'oni Karim audiolari")] 
        ], resize_keyboard=True)
    await message.answer("Asosiy menyuga qaytildi.", reply_markup=bttn)


@dp.message(F.text=="Qur'oni Karim audiolari")
async def echo_all(message: types.Message):
    await message.answer("Assalomu alaykum! Siz Qur'oni Karim audiolari bo'limidasiz.", reply_markup=quron_button) 

@dp.callback_query(F.data.startswith("quran"))
async def send_quran(call: types.CallbackQuery):
    sura_range = qorilar_dict.get(call.data)
    await call.message.edit_text("Qur'on audiolari yuklanmoqda...")
    if sura_range:
        for sura_num in sura_range:
            tg_file = f"https://t.me/Quranic_30/{sura_num}" 
            try:
                await call.message.answer_audio(tg_file, caption="@eynafsim1")
                await asyncio.sleep(0.3) 
            except TelegramBadRequest:
                await call.message.answer("Sura topilmadi.")
    await call.answer()  
    


# --- ADMIN PANEL ---

@dp.message(Command("admin"), F.from_user.id == ADMIN_ID)
async def admin_main(message: types.Message):
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="➕ Kanal qo'shish"), KeyboardButton(text="📜 Ro'yxat")],
        [KeyboardButton(text="🗑 Tozalash")]
    ], resize_keyboard=True)
    await message.answer("Admin panelga xush kelibsiz", reply_markup=kb)

@dp.message(F.text == "➕ Kanal qo'shish", F.from_user.id == ADMIN_ID)
async def add_ch_cmd(message: types.Message, state: FSMContext):
    await message.answer("Kanal ID va Linkini yuboring.\nMasalan:\n`-100123456789 https://t.me/kanalim` ")
    await state.set_state(AdminStates.waiting_for_channel)

@dp.message(AdminStates.waiting_for_channel, F.from_user.id == ADMIN_ID)
async def process_add(message: types.Message, state: FSMContext):
    try:
        data = message.text.split()
        ch_id = data[0]
        url = data[1]
        
        # Bot adminligini tekshirish
        chat = await bot.get_chat(ch_id)
        
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute("INSERT INTO channels (ch_id, url) VALUES (?, ?)", (str(chat.id), url))
            await db.commit()
        
        await message.answer(f"✅ Qo'shildi: {chat.title}")
        await state.clear()
    except Exception as e:
        await message.answer(f"❌ Xato! Bot kanalda admin ekanligini va ID to'g'riligini tekshiring.\n\n{e}")


@dp.message(F.text == "📜 Ro'yxat", F.from_user.id == ADMIN_ID)
async def list_ch(message: types.Message):
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute("SELECT ch_id, url FROM channels") as cursor:
            channels = await cursor.fetchall()
    
    if not channels: return await message.answer("Kanallar yo'q")
    
    msg = "Kanallar ro'yxati:\n"
    for c_id, url in channels:
        msg += f"ID: `{c_id}` | [Link]({url})\n"
    await message.answer(msg, parse_mode="Markdown")

@dp.message(F.text == "🗑 Tozalash", F.from_user.id == ADMIN_ID)
async def clear_ch(message: types.Message):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("DELETE FROM channels")
        await db.commit()
    await message.answer("Barcha kanallar o'chirildi.")

# --- ISHGA TUSHIRISH ---
async def main():
    await init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    