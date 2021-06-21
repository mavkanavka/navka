#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#pip install pytelegrambotapi


# In[ ]:


import telebot
from telebot import types
import requests
import matplotlib.pyplot as plt

import PIL
from PIL import Image
from skimage.io import imread # imread нужен для закачки\получения именно картинок 


token = '1807060008:AAEB2H5OmkzmQC2GfwOBhGbDbP3Onc2UxIU'
bot = telebot.TeleBot(token)


# In[ ]:


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')


# In[ ]:


@bot.message_handler(content_types=["photo"])
def handle_docs_image(message):
    #Чтобы получить ID получателя  
    chat_id = message.chat.id
    #id пользователя
    idphoto = message.photo[0].file_id
    #посылаем его же пользователю
    bot.send_photo(message.chat.id, idphoto)
    
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)    
    
    url = f'http://api.telegram.org/file/bot{token}/{file_info.file_path}'
    bot.reply_to(message, "Я возьму")


# In[ ]:


bot.polling(none_stop=True)


# In[ ]:





# In[ ]:




