from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from YukkiMusic import app as Client
from YukkiMusic import app


@Client.on_callback_query(filters.regex("arbic"))
async def arbic(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"""**- مرحبا عـزيـزي**   [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) ! \n
**- في قسم تشغيل الأغاني والفيديو في المكالمات**\n
**- استخدم الازرار لـ تصفـح اوامـر الميـوزك** """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اضف البوت لـ مجموعتك ",
                        url=f"https://t.me/{app.username}?startgroup=true",
                    )
                ],
                [                   InlineKeyboardButton("طريقة التشغيل", callback_data="bcmds"),
                    InlineKeyboardButton("طريقة التفعيل", callback_data="bhowtouse"),
                ],
            ]
        ),
        disable_web_page_preview=True,
    )

@Client.on_callback_query(filters.regex("english"))
async def english(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f" [※A Telegram Music Bot Based Mongodb](https://t.me/mvhmed) \n ※[These Features AI Based](https://t.me/mvhmed)",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Add me to your Group ",
                        url=f"https://t.me/{app.username}?startgroup=true",
                    )
                ],
                [                
                    InlineKeyboardButton(" Commands", callback_data="cbcmds"),
                    InlineKeyboardButton(" Donate", url=f"https://t.me/Mvhmed"),
                ],
                [
                    InlineKeyboardButton(
                        "˹  𝙈𝙪𝙝𝙖𝙢𝙢𝙚𝙙 𝙆𝙝𝙖𝙡𝙞𝙙 ⁦. 𓌗", url="https://t.me/Mvhmed"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )

@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f"""📚 **Basic Guide for using this bot:**
1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**
📌 **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**
💎 **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="english")]]
        ),
    )

@Client.on_callback_query(filters.regex("Q_XUQ"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f""" **※Welcome \n
※Show members keyboard Send /JA \n\n
※Show entertainment keyboard send /JA**
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="english")]]
        ),
    )
    
    
@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""🥹♥ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**
» **press the button below to read the explanation and see the list of available commands !**
√ __Powered by ˹  𝙈𝙪𝙝𝙖𝙢𝙢𝙚𝙙 𝙆𝙝𝙖𝙡𝙞𝙙 ⁦. 𓌗 """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("Sudo Cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("Basic Cmd", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("Go Back ", callback_data="english")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("basic commands")
    await query.edit_message_text(
        f""" here is the basic commands:
» /play (song name/link) - play music on video chat
» /vplay (video name/link) - play video on video chat
» /vstream - play live video from yt live/m3u8
» /playlist - show you the playlist
» /video (query) - download video from youtube
» /song (query) - download song from youtube
» /lyric (query) - scrap the song lyric
» /search (query) - search a youtube video link
» /ping - show the bot ping status
» /speedtest - run the bot server speedtest
» /uptime - show the bot uptime status
» /alive - show the bot alive info (in group)
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.answer("admin commands")
    await query.edit_message_text(
        f""" here is the admin commands:
» /pause - pause the stream
» /resume - resume the stream
» /skip - switch to next stream
» /stop - stop the streaming
» /vmute - mute the userbot on voice chat
» /vunmute - unmute the userbot on voice chat
» /volume `1-200` - adjust the volume of music (userbot must be admin)
» /reload - reload bot and refresh the admin data
» /userbotjoin - invite the userbot to join group
» /userbotleave - order userbot to leave from group
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.answer("sudo commands")
    await query.edit_message_text(
        f""" here is the sudo commands:
» /rmw - clean all raw files
» /rmd - clean all downloaded files
» /sysinfo - show the system information
» /update - update your bot to latest version
» /restart - restart your bot
» /leaveall - order userbot to leave from all group
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("bhowtouse"))
async def acbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**⦿ طريقة تفعيل البوت في مجموعتك :**
ٴ⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆
**1- اضف البوت الى مجموعتك**
**2- ترقية البوت مشرف كامل الصلاحيه**
**3- لـ تحديث قائمة الادمن ارسـل** `ريلود`
**3- اضف الحساب المساعد الى مجموعتك (يوزر المساعد ع نبذة البوت)**
**4- تأكد من تشغيل المحادثة الصوتية**
**5- اذا واجهت خطأ قم بكتابة الامر** `ريلود`
**- ملاحظـه هامـه :**
**في حال لم يستطع الحساب المساعد الانضمام الى المحادثة الصوتية قم بطرد الحساب المساعد بالأمر** `/غادر` \n**ودعوته من جديد عبر الامر** `/انضم`
\n™""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("العودة", callback_data="arbic")]]
        ),
    )


@Client.on_callback_query(filters.regex("bcmds"))
async def acbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**- عـزيـزي  [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**
**- استخـدم الازرار بالاسفل لمعرفة طريقة التشغيل**
\n™""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("اوامر التشغيل", callback_data="bbasic"),
                    InlineKeyboardButton("اوامر الادمن", callback_data="badmin"),
                ],[
                    InlineKeyboardButton("اوامر المطورين", callback_data="bsudo")
                ],[
                    InlineKeyboardButton("العودة", callback_data="arbic")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("bbasic"))
async def acbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**⦿ اوامــر التشغيــل :**
ٴ⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆
» شغل/تشغيل (اسم الموسيقى/رابـط )
لـ تشغيل الموسيقى في المحادثة الصوتية 
» لايف ( بالرد على ملف/رابـط)
لـ تشغيل مقطع فيديو موجود في الدردشـه
» شغل/تشغيل (اسم الفيديو/رابـط)
لـ تشغيل مقطع فيديو 
» /vstream
لـ تشغيل بث مباشر
» القائمه
لـ عرض قائمة التشغيل
» فيديو
لـ تحميل مقطع فيديو
» بحث/اغنيه
لـ تحميل ملف صوتي 
» ابحث
لـ البحث عن روابط يوتيوب
» بنج
لـ عرض سرعة الاستجابة
» /uptime
لـ عرض وقت تشغيل البوت
» /alive
لـ عرض معلومات البوت 
\n™""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("العودة", callback_data="bcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("badmin"))
async def acbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**⦿ اوامـر التحكم الخاصـه بـ الادمنيـة :**
ٴ⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆
» قف/قفي - ايقاف التشغيل موقتأ
» كمل/استمر - لاستكمال التشغيل
» تخطي/التالي - لتخطي تشغيل الحالي
» ايقاف/انهاء - لايقاف تشغيل الحالي
» اسكت/اسكتي - لكتم البوت في المحادثة
» اتكلم/تكلمي - الغاء كتم الحساب المساعد
» الصوت `1-200` - لتحكم في درجة الصوت
» ريلود - لتحديث قائمة الادمن للتحكم في البوت
» /المتصلين - لـ جلب قائمـة ب اسماء المتواجدين ع المكالمـه
» مين في الكول - لـ جلب قائمـة ب اسماء المتواجدين ع المكالمـه
\n™""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("العودة", callback_data="bcmds")]]
        ),
    )
    
@Client.on_callback_query(filters.regex("afyona"))
async def acbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""™""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("العودة", callback_data="bcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("bsudo"))
async def acbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**⦿ اوامــر المطـوريـن :**
ٴ⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆
» `/rmw` - لمسح جميع الملفات المتخزنة
» `/rmd` - تنظيف التخزين المؤقت
» `/sysinfo` - لعرض قدرات التشغيل
» `/update` - لتحديث اصدار السورس
» `/restart` - إعادة تشغيل البوت
» `/leaveall` - خروج الحساب المساعد من جميع المحادثات
\n™""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("العودة", callback_data="bcmds")]]
        ),
    )
