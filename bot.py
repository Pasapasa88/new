# -*- coding: utf-8 -*-
import telebot, time, monitoring

def get_text_messages(rr, chat_id, stat):

    if rr == "Stop":
        bot.send_message(chat_id, "Остановка оповещений")
        return -1
    elif rr == "Start":
        bot.send_message(chat_id, "Оповещение работает в стандартном режиме")
        return 0
    elif rr == "Pause":
        bot.send_message(chat_id, "Остановка сообщений на 30 мин")
        return round((30 * 60)/10)
    elif rr == "Status":
        status, ttg, online = monitoring.export_data()
        text = 'Онлайн - ' + str(online) + '\n Температура = ' + str(ttg) + ', ' + state_dict[status]
        bot.send_message(chat_id, text)
        return stat
    elif rr == "Bot_status":
        if stat == 0:
            bot.send_message(chat_id, "Оповещение работает в стандартном режиме")
        elif stat == -1:
            bot.send_message(chat_id, "Бот не запущен")
        elif stat > 0:
            bot.send_message(chat_id, "Бот в режиме ожидания, автоматически запустится через - {} минут".
                             format(round(stat*10/60)))
        return stat
    elif rr == "/start":
        keybord()
        return stat
    else:
        try:
            bot.send_photo(chat_id,'https://risovach.ru/upload/2013/08/mem/chego_26642012_orig_.jpeg')
        except:
            bot.send_message(chat_id, "Чиииивооо бл...?")
        return stat

def warning(aaa,chat_id):
    bot.send_message(chat_id, aaa)

def keybord():
    keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard1.row('Start', 'Stop', 'Pause')
    keyboard1.row('Status')
    keyboard1.row('Bot_status')
    bot.send_message(chat_id, 'Чо надо?', reply_markup=keyboard1)

def counter(i):
    print('counter ' + str(i))
    if i > 0:
        i = i-1
    return i

if __name__ == '__main__':
    state_dict = {0: "Ожидание",
                  1: "Розжиг",
                  2: "Работа",
                  3: "Поддержка",
                  4: "Гашение"}
    bot = telebot.TeleBot('1399037172:AAE-vyA0tnXIMDBfctf3QLkTc4-lphdpkhU')
    chat_id = -1001442101581
    keybord()
    start = 0
    while True:
        try:
            start = counter(start)
            if start == 0:
                status, ttg, online = monitoring.export_data()
                print(status, ttg)
                if (ttg < 80 and status not in (2, 3)) or online is False:
                    text = 'Онлайн - ' + str(online) + '\n Температура = ' + str(ttg) + ', ' + state_dict[status]
                    print(text)
                    warning(text,chat_id)
            print(1)
            if bot.get_webhook_info().pending_update_count > 0:
                id = bot.get_me()
                gg = bot.get_updates()[0].message.id
                print(2)
                ff = bot.get_updates()[0].message.text
                print(3)
                start = get_text_messages(ff,chat_id,start)
                print(4)
                bot.delete_webhook(True)
            time.sleep(10)
        except:
            pass

