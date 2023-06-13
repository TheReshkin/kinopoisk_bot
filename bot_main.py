import telebot
from secrets import TOKEN

# Создание объекта бота
bot = telebot.TeleBot(TOKEN)


# Обработка команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 "Привет! Я бот для поиска фильмов на Кинопоиске. "
                 "Напиши мне название фильма и я попробую отправить тебе ссылку для просмотра.")


# Обработка текстовых сообщений
@bot.message_handler(func=lambda message: True)
def generate_response(message):
    # Отправка ответа пользователю
    bot.reply_to(message, response)


def main():
    # Запуск бота
    bot.polling()
