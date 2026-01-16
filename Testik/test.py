import telebot, os 
from telebot import types

images = os.listdir("images")
bot = telebot.TeleBot("8052440771:AAF-u01sX3U3VM02dJOBfI6yQy5_JXZeDTA")
num = 0
def board():
    buttons = types.InlineKeyboardMarkup() 
    left_button = types.InlineKeyboardButton("<", callback_data="left")
    right_button = types.InlineKeyboardButton(">", callback_data="right")
    exit_button = types.InlineKeyboardButton("Закрыть2", callback_data="exit")
    middle_button =types.InlineKeyboardButton(f"1/{len(images) // 2}", callback_data="exit")
    buttons.add(left_button, middle_button, right_button)
    buttons.add(exit_button)
    return buttons



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['foto'])
def send_welcome(message):
    with open(f"images/{images[0]}", "rb") as file:
        bot.send_photo(message.chat.id, file, reply_markup=board())

@bot.callback_query_handler(func=lambda otvet: True) 
def callback(otvet):
    global num
    if otvet.data == "right":
        num +=1
        bot.delete_message(chat_id=otvet.message.chat.id,message_id=otvet.message.message_id)
        
        with open(f"images/(images[num])", "rb") as file: 
            bot.send_photo(message.chat.id, file, reply_markup=board())


bot.polling(non_stop=True)
