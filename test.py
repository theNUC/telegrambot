import telebot
from telebot import types
import random
TOKEN = '6710160469:AAFp-La-8NuhEWiun4DpGbMY-9a0ESo4jYk'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup =  types.ReplyKeyboardMarkup(resize_keyboard= True)
    item1 = types.KeyboardButton('🎲random son')
    item2 = types.KeyboardButton('💰pul kursi')
    item3 = types.KeyboardButton('📉informatsiya')
    item4 = types.KeyboardButton('💾boshqa')

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'salom, {0.first_name}!' .format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '🎲random son':
            bot.send_message(message.chat.id, 'sizni soningiz: ' +str(random.randint(0,1000)))
        elif message.text == '💰pul kursi':
            markup =  types.ReplyKeyboardMarkup(resize_keyboard= True)
            item1 = types.KeyboardButton('eu kursi')
            item2 = types.KeyboardButton('uzs kursi')
            back = types.KeyboardButton('⬅️ ortga')
            markup.add(item1, item2, back)


            bot.send_message(message.chat.id, '💰pul kursi',  reply_markup=markup)


        elif message.text == '📉informatsiya':
            markup =  types.ReplyKeyboardMarkup(resize_keyboard= True)
            item1 = types.KeyboardButton('bot haqida')
            item2 = types.KeyboardButton('quti ichida nma bor?')
            back = types.KeyboardButton('⬅️ ortga')
            markup.add(item1, item2, back)


            bot.send_message(message.chat.id, '📉informatsiya',  reply_markup=markup)


        elif message.text == '💾boshqa':
            markup =  types.ReplyKeyboardMarkup(resize_keyboard= True)
            item1 = types.KeyboardButton('⚙️sozlama')
            item2 = types.KeyboardButton('🧩stikerlar')
            item3 = types.KeyboardButton('🖋obuna')
            back = types.KeyboardButton('⬅️ ortga')
            markup.add(item1, item2, item3, back)


            bot.send_message(message.chat.id, '💾boshqa',  reply_markup=markup)

        elif message.text == '⬅️ ortga':
            markup =  types.ReplyKeyboardMarkup(resize_keyboard= True)
            item1 = types.KeyboardButton('🎲random son')
            item2 = types.KeyboardButton('💰pul kursi')
            item3 = types.KeyboardButton('📉informatsiya')
            item4 = types.KeyboardButton('💾boshqa')

            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, '⬅️ ortga' , reply_markup=markup)

        elif message.text == 'sticker':
            stick = open('static/sticker.webp', 'rb')
            bot.send_sticker(message.chat.id, stick)


bot.polling(non_stop=True)