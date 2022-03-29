import telebot
from telebot import types
from parser import get_second_news, get_first_news

load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text = "Да", callback_data = 'yes')
    item_no = types.InlineKeyboardButton(text = "Нет", callback_data = 'no')
    markup_inline.add(item_yes, item_no)
    bot.send_message(message.chat.id, "Привет! Хочешь получить свежую новость?)", reply_markup = markup_inline)


@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard= True)
        last_news = types.KeyboardButton('Последняя новость')
        penultimate_news = types.KeyboardButton("Предпоследняя новость")
        
        markup_reply.add(last_news, penultimate_news)
        bot.send_message(call.message.chat.id, "Выберите какую новость вы бы хотели получить?" ,
        reply_markup = markup_reply )
    elif call.data == 'no':
        pass


@bot.message_handler(content_types=["text"])
def n_n(message):
    text_1 = get_first_news()
    text_2 = get_second_news()
    if message.text == 'Последняя новость':
        bot.send_message(message.from_user.id, text_1)
    elif message.text == 'Предпоследняя новость':
        bot.send_message(message.from_user.id, text_2)

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)

