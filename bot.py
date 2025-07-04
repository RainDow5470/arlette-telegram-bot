import os
from dotenv import load_dotenv
import telebot
from telebot.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Загружаем переменные из .env
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = telebot.TeleBot(API_TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Сначала отправляем картинку
    photo_url = "https://i.ibb.co/HLWcrL0b/03-ARL-png.png"
    bot.send_photo(chat_id=message.chat.id, photo=photo_url)

    # Затем отправляем текст с HTML-ссылкой
    caption = (
        "Привет! Сейчас ты записываешься на кастинг в Arlette Management 🤍\n\n"
        "Заполни анкету, и мы обязательно рассмотрим твою кандидатуру!\n"
        "Свяжемся с тобой в ближайшее время для уточнения деталей и в случае заинтересованности пригласим тебя в агентство 🫶🏻\n\n"
        "Мы также недавно начали вести <a href=\"https://t.me/arlettelife\">наш телеграм-канал</a>, куда часто публикуем закадровую жизнь моделей, бэки со съёмок, советы для new face.\n"
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

    # Отправка текста и кнопки
    bot.send_message(
        chat_id=message.chat.id,
        text=caption,
        reply_markup=markup,
        parse_mode="HTML"
    )

# Обработка анкеты
@bot.message_handler(content_types=['web_app_data'])
def handle_web_app(message):
    try:
        data = eval(message.web_app_data.data)

        formatted_message = (
            "📥 Новая анкета:\n\n"
            f"👤 Имя и фамилия: {data.get('full_name')}\n"
            f"🎂 Возраст: {data.get('age')}\n"
            f"📞 Телефон: {data.get('phone')}\n"
            f"💬 Telegram: {data.get('telegram')}\n"
            f"📸 Instagram: {data.get('instagram')}\n"
            f"📝 О себе: {data.get('about')}\n"
            f"📏 Рост: {data.get('height')} см\n"
            f"🎯 Грудь: {data.get('bust')} см\n"
            f"🎯 Талия: {data.get('waist')} см\n"
            f"🎯 Бёдра: {data.get('hips')} см\n"
            f"🌆 Город: {data.get('city')}"
        )

        bot.send_message(chat_id=ADMIN_ID, text=formatted_message)

    except Exception as e:
        bot.send_message(chat_id=ADMIN_ID, text=f"❗ Ошибка при обработке анкеты: {e}")

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)
