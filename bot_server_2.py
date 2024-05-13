import telebot
from config import *
print("бот запущен")

bot = telebot.TeleBot(TOKEN)
# Начало работы
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Идет запись в журнал')

gurnal={}
@bot.message_handler(content_types=["text"])
def message_handler(message):
    # делит получаемое сообщение в виде списка  на номер и дату в виде элементов листа
    namber_date=message.text.split()
    namber_g = namber_date[0]
    date_g = namber_date[1]
    bot.send_message(message.chat.id, message.text)
    #словарь куда добавляются значения номера и даты в виде ключа и значения
    gurnal[namber_g]=date_g

    from datetime import datetime
    from datetime import date
    from datetime import timedelta


    # формат для ввода даты data_g = '11.17.2020'
    # дата регистрации документа
    data_g_for_pyt = datetime.strptime(date_g, '%d.%m.%Y') #перевод даты в формат кода
    print(data_g_for_pyt)
    import datetime
    #control_date = data_g_for_pyt + datetime.timedelta(days=1)
    for n,d in gurnal.items():
        d = datetime.datetime.strptime(d, '%d.%m.%Y')
        control_date = d + datetime.timedelta(days=1)
        segodnya = datetime.datetime.today()
        if segodnya == control_date:
            bot.send_message(message.chat.id, "пришло время написать письмо о сроках по эксп. №" +n)
        elif segodnya > control_date:
            bot.send_message(message.chat.id, "пришло время написать письмо о сроках по эксп. №" + n)
        else:
            bot.send_message(message.chat.id, "Еще пока рано писать письмо о сроках по эксп. №" + n)

        print(segodnya)
        print(control_date)
        print(d)

if __name__== "__main__":
    bot.polling(True)
