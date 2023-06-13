import telebot
from secrets import TOKEN
from kinopoisk_api import movie_search
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
    response = []
    # answer = "[Описание изображения](https://upload.wikimedia.org/wikipedia/commons/8/83/Iris_germanica_160505.jpg)"
    answer = movie_search(message.text)
    bot.send_message(message.chat.id, answer, parse_mode='Markdown')
    # bot.reply_to(message, response)


def bot_main():
    # Запуск бота
    bot.polling()
    print('main')

bot_main()