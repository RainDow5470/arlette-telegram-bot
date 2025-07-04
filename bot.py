@bot.message_handler(commands=['start'])
def send_welcome(message):
    photo_url = "https://i.ibb.co/HLWcrL0b/03-ARL-png.png"
    caption = (
        "Привет! Сейчас ты записываешься на кастинг в Arlette Management 🤍\n\n"
        "Заполни анкету, и мы обязательно рассмотрим твою кандидатуру!\n"
        "Свяжемся с тобой в ближайшее время для уточнения деталей и в случае заинтересованности пригласим тебя в агентство 🫶🏻\n\n"
        "Мы также недавно начали вести <a href=\"https://t.me/arlettelife\">наш телеграм-канал</a>, куда часто публикуем закадровую жизнь моделей, бэки со съемок, советы для new face. \n"
        "Будем рады, если ты подпишешься и останешься с нами ❣️\n\n"
        "Не жди «идеального момента» — он уже здесь! 💋"
    )

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(
            "Заполнить анкету 🤍",
            web_app=WebAppInfo(url="https://raindow5470.github.io/bot-new/")
        )
    )

    bot.send_photo(
        chat_id=message.chat.id,
        photo=photo_url,
        caption=caption,
        reply_markup=markup,
        parse_mode="HTML"
    )
