import telebot

from telebot import types
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from .models import Tguser,Ariza
#from category.models import category

bot = telebot.TeleBot(settings.BOT_TOKEN)

@csrf_exempt
def web_hook_view(request):
    if request.method == 'POST':
        bot.process_new_updates([telebot.types.Update.de_json(request.body.decode('utf-8'))])
    return HttpResponse('OK')



def start_message_buttons():
    reply_markup = telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    reply_markup.add(*[
        telebot.types.KeyboardButton(text) for text in ['🇺🇿 uz','🇷🇺 ru']
    ])
    return reply_markup


def contact_message_buttons():
    reply_markup = telebot.types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    reply_markup.add(*[
        telebot.types.KeyboardButton('contactni yuborish',request_contact=True)
    ])
    return reply_markup


def headr_message_buttons():
    reply_markup = telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    reply_markup.add(*[
        telebot.types.KeyboardButton(text) for text in ['Bosh sahifa','count','ariza berish']
    ])
    return reply_markup


@bot.message_handler(commands=['start'])
def start_message(message):
    if Tguser.objects.filter(user_id=message.from_user.id).count() == 0:
        user = Tguser(user_id=message.from_user.id,first_name=message.from_user.first_name)
        bot.send_message(message.from_user.id,f"salom {message.from_user.first_name} Tilni tanlang",reply_markup=start_message_buttons())
        user.save()
    else:
        bot.send_message(message.from_user.id,'siz bosh sahifadfasiz',reply_markup=headr_message_buttons())
        #print(message.chat.id)


@bot.message_handler(content_types=['contact'])
def contact(message):
    if message.contact is not None:
        user = Tguser.objects.get(user_id=message.from_user.id)
        user.phon_number = message.contact.phone_number
        user.save()
        text = f"phon: +{user.phon_number}\nfirst_name:{user.first_name}\nlanguage: {user.language}"
        #print(message.contact.phone_number)
        bot.send_message(message.from_user.id, f"{message.from_user.first_name} Botdan ro'yhattan o'tti\nolingan malumotlar\n{text}", reply_markup=headr_message_buttons())
        bot.send_message(chat_id=1363350178,text=text)


# @bot.message_handler(content_types=['text'])
# def ariza_message(message):
#     if message.text == 'ariza berish':
#         bot.send_message(message.from_user.id, f"{message.from_user.first_name} ariza qoldirishingiz mumkun")
#     if message.text == 'count':
#         count = Tguser.objects.count()
#         bot.send_message(message.from_user.id,f"Botda {count} ta foydalanuvchi bor")




@bot.message_handler(func=lambda m: True)
def all_message(message):
    for x in ['🇺🇿 uz','🇷🇺 ru']:
        if message.text == x:
            user = Tguser.objects.get(user_id=message.from_user.id)
            user.language = x
            user.save()
            #print(message.text)
            bot.send_message(message.from_user.id, 'Tel nomeringizni yuboring',reply_markup=contact_message_buttons())


    if message.text == 'count':
        count = Tguser.objects.count()
        bot.send_message(message.from_user.id,f"Botda {count} ta foydalanuvchi bor")


    print(message.text)

    # if message.text == 'ariza berish':
    #     bot.send_message(message.from_user.id,f"{message.from_user.first_name} ariza qoldirishingiz mumkun")

