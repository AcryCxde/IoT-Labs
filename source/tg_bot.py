import json

import telebot
import server


def main():
    bot = telebot.TeleBot('')

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text == "/data":
            data = server.data
            data_str = "Данные:\n"
            if data:
                for k, v in data.items():
                    data_str += k + ": " + str(v) + "\n"
                bot.send_message(message.from_user.id, data_str)
            else:
                bot.send_message(message.from_user.id, "Данные ещё не сгенерировались, подождите")

        elif message.text == "/help" or message.text == "/start":
            bot.send_message(message.from_user.id,
                             "Команды:\n/data - отображение данных\n/manual - установить ручной режим\n"
                             "/auto - установить автоматический режим\n"
                             "/actuator - включить актуатор (доступно только в ручном режиме)")

        elif message.text == "/manual":
            server.set_manual_mode(1)
            bot.send_message(message.from_user.id, "Ручной режим включен")

        elif message.text == "/auto":
            server.set_manual_mode(0)
            bot.send_message(message.from_user.id,"Автоматический режим включен")

        elif message.text == "/actuator":
            if server.manual_mode:
                bot.send_message(message.from_user.id,"Актуатор активирован по команде от сервера")
                server.set_actuator_mode(True)
            else:
                bot.send_message(message.from_user.id,'Невозможно включить актуатор, включен автоматический режим')

        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

    bot.polling(non_stop=True, interval=0)
