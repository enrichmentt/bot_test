import telebot

TOKEN = open('conf.txt', 'r').read().split('\n')[0]

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['ip'])
def send_ip(message):
    msg = bot.reply_to(message, "Enter IP")
    bot.register_next_step_handler(msg, getIp)


@bot.message_handler(commands=['mac'])
def send_mac(message):
    msg = bot.send_message(message, "Enter mac")
    bot.register_next_step_handler(msg, getMac)


def getIp(message):
    if(message.text == "ip"):
        bot.reply_to(message, "Yeap!")
        bot.register_next_step_handler(message, getIp)
    elif(message.text == "/c"):
        bot.clear_step_handler(message)
    else:
        bot.reply_to(message, "Ooooops!")
        bot.register_next_step_handler(message, getIp)


def getMac(message):
    if(message.text == "mac"):
        bot.reply_to(message, "Yeap!")
        bot.register_next_step_handler(message, getMac)
    elif(message.text == "/c"):
        bot.clear_step_handler(message)
    else:
        bot.reply_to(message, "Ooops!")
        bot.register_next_step_handler(message, getMac)


bot.infinity_polling()
