import telebot
import os, random

bot = telebot.TeleBot('7004522075:AAGSnG-I-cRRkSsgsi4-SfL-V5LvhOxtwm8')

@bot.message_handler(commands=['plastic_art'])
def send_mem(message):
    img_name = random.choice(os.listdir('images'))  # Случайным образом выбираем изображение
    with open(f'images/{img_name}', 'rb') as f:
        # Отправляем фото, выбранное случайным образом
        bot.send_photo(message.chat.id, f, caption='желаемая поделка')

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет! Используй команду /plastic_art, чтобы получить поделку из пластика!")

bot.polling()