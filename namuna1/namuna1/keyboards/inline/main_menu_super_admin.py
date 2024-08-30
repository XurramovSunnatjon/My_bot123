from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

xizmatlar= {
    "xizmat":{"MRT bosh miya",
"MRT bosh miya va ko'z olmasi",
"MRT gipofiz bezi",
"MRT bosh miya va gipofez bezi",
"MRT burun yon bo'shliqlari",
"MRT bosh miya kontrastli tekshiruv (kontrastdan tashqari )",
"MRT bosh miya kontartsiz angiografiyasi",
"MRT tashqi Villiziev qon tomirlari",
"MRT bosh miya va ko'z olmasi traktografiyasi",
"MRT bosh miya, burun yon bushliqlari, ko'z olmasi eshitish yo'llari angiografiya",
"MRT bo'yin yumshoq to'qimnalari",
"MRT buyin umurtqalari kontrastli tekshiruv (kontrastdan tashqari)",
"MRT bo'yin qon tomiri",
"MRT ko'krak umurtqalari",
"MRT ko'krak umurtqalari va (kontartdan tashqari)",
"MRT bel umurtqalari",
"MRT yelka bo'g'imlari (o'ng va chap  alohida )",
"MRT qorin bushlig'i organlari",
"MRT qorin bo'shlig'i organlari MP Xolangiografiy",
"MRT buyraklar angiografiyasi (kontrast bilan)",
"MRT urografiyasi (kontrast bilan)",
"MRT kichchik chanoq organlari",
"MRT chanoq son bo'g'imlari",
"MRT tirsak bo'g'imi (o'ng va chap alohida )",
"MRT bilak kaft bo'g'imi ( o'ng va chap  alohida)",
"MRT tizza bo'g'imi (o'ng va chap alohida)",
"MRT boldir tovon bo'g'imi (o'ng va chap alohida)",
"MRT tanlangan organ yumshoq to'qimasi",
"MRT oyoq qon tomirlari angiografiyasi",
"MRT ko'krak bezlari mamalogiyasi",
"MRT buyrak va buyrak usti bezlari",
"MRT qayta plyonka chiqarish",
"MRT  qayta disk yozish",
},
    "uznarx":{ "293 000",
 "318 000",
 "255 000",
 "477 000",
 "255 000",
 "449 000",
 "344 000",
 "267 000",
 "435 000",
 "1 044 000",
 "308 000",
 "293 000",
 "384 000",
 "280 000",
 "409 000",
 "293 000",
 "346 000",
 "409 000",
 "346 000",
 "246 000",
 "396 000",
 "320 000",
 "320 000",
 "320 000",
 "321 000",
 "295 000",
 "320 000",
 "384 000",
 "384 000",
 "384 000",
 "295 000",
 "36 000",
 "16 000" },
    "chetnarx":{ "439 500",
 "477 000",
 "382 000",
 "715 000",
 "382 000",
 "673 000",
 "516 000",
 "400 000",
 "652 000",
 "1 566 000",
 "462 000",
 "439 000",
 "576 000",
 "420 000",
 "613 500",
 "439 500",
 "519 000",
 "613 500",
 "519 000",
 "396 000",
 "594 000",
 "480 000",
 "480 000",
 "480 000",
 "481 500",
 "442 500",
 "480 000",
 "576 000",
 "576 000",
 "576 000",
 "442 000",
 "54 000",
 "24 000" }
}
xizmatim = InlineKeyboardMarkup(row_width=1)
k=1
for i in xizmatlar["xizmat"]:
    xizmatim.add(InlineKeyboardButton(text=i,callback_data=str(k)))
    k=k+1
yubor = InlineKeyboardMarkup(row_width=2)
yubor.add(InlineKeyboardButton(text="Yuborish",callback_data="yes"),
            InlineKeyboardButton(text="Bekor qilish",callback_data="no"),
          InlineKeyboardButton(text="Отправка", callback_data="yes"),
          InlineKeyboardButton(text="Отмена", callback_data="no"),
          InlineKeyboardButton(text="Submit", callback_data="yes"),
          InlineKeyboardButton(text="Cancellation", callback_data="no"),
          )

fuqaro = InlineKeyboardMarkup(row_width=2)
fuqaro.add(InlineKeyboardButton(text="O'zbekiston", callback_data="uzbek"),
            InlineKeyboardButton(text="Chet el fuqarosi",callback_data="chet"),
           InlineKeyboardButton(text="Узбекистан", callback_data="uzbek"),
           InlineKeyboardButton(text="Иностранный гражданин", callback_data="chet"),
           InlineKeyboardButton(text="Uzbekistan", callback_data="uzbek"),
           InlineKeyboardButton(text="Foreign citizen", callback_data="chet"),
           )

tillar = InlineKeyboardMarkup(row_width=2)
tillar.add(InlineKeyboardButton(text="🇸🇱O'zbekcha", callback_data="uzb"),
            InlineKeyboardButton(text="🇷🇺Русский", callback_data="ru"),
            InlineKeyboardButton(text="🇬🇧English", callback_data="eng")
           )

main_menu_for_super_admin = InlineKeyboardMarkup(row_width=2)

main_menu_for_super_admin.add(InlineKeyboardButton(text="➕ Kanal qo'shish", callback_data="add_channel"),
                              InlineKeyboardButton(text="➖ Kanal o'chirish", callback_data="del_channel"),
                              InlineKeyboardButton(text="➕ Admin qo'shish", callback_data="add_admin"),
                              InlineKeyboardButton(text="➖ Admin o'chirish", callback_data="del_admin"),
                              InlineKeyboardButton(text="👤 Adminlar", callback_data="admins"),
                              InlineKeyboardButton(text="📝 Adminlarga Xabar yuborish",callback_data="send_message_to_admins"),
                              InlineKeyboardButton(text="📝 Reklama Jo'natish", callback_data="send_advertisement"),
                              InlineKeyboardButton(text="📊 Statistika", callback_data="statistics"),
                              )

main_menu_for_admin = InlineKeyboardMarkup(row_width=2)

main_menu_for_admin.add(InlineKeyboardButton(text="📊 Statistika", callback_data="stat"),
                              )

back_to_main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️ Orqaga", callback_data="back_to_main_menu")
        ]
    ]
)
