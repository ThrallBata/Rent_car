from django.core.management.base import BaseCommand
from django.conf import settings
import telebot
from telebot import types

from ...models import Cars, Client

bot = telebot.TeleBot('6252439193:AAFiZbZUtjqX7xNEwSSEmXd7K7K6OMJCCow', threaded=False)


selected_car = ""
list_name_car = []
list_number_car = []

cars = Cars.objects.all()

for element in cars:
    list_name_car.append(element.name_car)
    list_number_car.append(element.id)

list_name_car.insert(0, " ")

buttons = {
    'main_menu': types.KeyboardButton('🔙 Главное меню'),
    'about': types.KeyboardButton("🔎 О компании"),
    'car_catalog': types.KeyboardButton('🚗 Каталог автомобилей'),
    'back': types.KeyboardButton("⬅Назад"),
}
class Command(BaseCommand):
    @bot.message_handler(commands=['start'])  # стартовая команда
    def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(buttons['about'], buttons['car_catalog'])
        bot.send_message(message.from_user.id, "🔎 Вы хотите перейти на сайт и узнать о компании / 🚗 хотите знакомится с каталогом автомобилей и оставить заявку", reply_markup=markup)

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text == '🔎 О компании':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(buttons['main_menu'])
            bot.send_message(message.from_user.id, 'Чтобы подробнее уpнать о компании переходите на сайт:\n 📲 Перейти по' + ' [ссылке](https://www.landrover.ru/vehicles/new-range-rover/index.html)', reply_markup=markup, parse_mode='Markdown')

        elif message.text == '🔙 Главное меню':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(buttons['about'], buttons['car_catalog'])
            bot.send_message(message.from_user.id, "🔎 Вы хотите перейти на сайт и узнать о компании / 🚗 хотите ознакомится с каталогом автомобилей и оставить заявку", reply_markup=markup)
            #
            # поискать ещё способ вызова функции старт или прописать заново меню
            #

        elif message.text == '🚗 Каталог автомобилей':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            list_name_car_buttons = []
            for i in list_name_car:  # len(объекты машин(с названием)
                list_name_car_buttons.append(types.KeyboardButton(f"{i}"))

            markup.add(list_name_car_buttons[1], list_name_car_buttons[11],
                       list_name_car_buttons[2], list_name_car_buttons[3],
                       list_name_car_buttons[4], list_name_car_buttons[5],
                       list_name_car_buttons[6], list_name_car_buttons[7],
                       list_name_car_buttons[8], list_name_car_buttons[9],
                       list_name_car_buttons[10], buttons['main_menu'])
            for i in range(1, 12):
                bot.send_message(message.from_user.id, f"машина песня {list_name_car[i]} 👇", reply_markup=markup)
                photo = open(f'car/static/car/images/{list_number_car[i-1]}.png', 'rb')
                bot.send_photo(message.from_user.id, photo)

            bot.send_message(message.from_user.id, 'Выберите интересующую вас модель автомобиля.', reply_markup=markup)

        elif True in [message.text == name for name in list_name_car]:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(buttons['main_menu'])
            global selected_car
            selected_car = ""
            selected_car = int(list_name_car.index(message.text))
            bot.send_message(message.from_user.id, f"Отличный выбор 👍, чтобы оставить заявку на {message.text}, укажите следующие данные: \n Ваш номер телефона.", reply_markup=markup)

        elif (message.text[0] == "+" and message.text[1] == '7') or (message.text[0] == "8" and message.text[1] == '9'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(buttons['main_menu'], buttons['back'])
            phone_num = message.text
            client_name = bot.send_message(message.from_user.id, 'Пожалуйста, укажите как мы к вам можем обращаться: ', reply_markup=markup)
            bot.register_next_step_handler(client_name, Command.client_data, phone_num)  # 1 аргумент сообщения Имени. 2 Вызов Функции. 3 Сообщения пришедшее с номером
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(buttons['main_menu'])
            bot.send_message(message.from_user.id, 'Я вас не понял!', reply_markup=markup)
    def client_data(message, phone_num):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(buttons['main_menu'])
        client_name = message.text
        print(client_name, phone_num)  # сохранение данных
        client = Client()
        client.name = client_name
        client.phone_number = phone_num
        client.car_id = list_number_car[selected_car]#настроить логичку работы, чтобы нормально отображались машины в БД
        client.save()
        bot.send_message(message.from_user.id, '📲 Спасибо за заявку, оператор свяжется с вами в ближайшее время! ', reply_markup=markup)

    def handle(self, *args, **kwargs):							# Загрузка обработчиков
        bot.enable_save_next_step_handlers(delay=2)  # Сохранение обработчиков
        bot.load_next_step_handlers()  # Загрузка обработчиков
        bot.infinity_polling()
