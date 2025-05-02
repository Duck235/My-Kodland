import telebot
import os, random
from model import *
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

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    if not message.photo:
        return bot.send_message(message.chat.id, "Вы забыли загрузить картинку")
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    result = get_class(model_path='keras_model.h5', labels_path='labels.txt', image_path=file_name)
    bot.send_message(message.chat.id, result)


bot.polling()