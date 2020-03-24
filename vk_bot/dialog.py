import keyboards
from scenarios.order_lesson import order_lesson
from scenarios.find_colleagues import find_colleagues
from scenarios.current_offers import current_offers

def dialog(user):
    answer = 'Здравствуйте! Вы написали боту MiptHelpBot. Выберите действие:'
    keyboard = keyboards.main_menu()
    action = yield answer, keyboard
    if action == 'Запросить урок':
        yield from order_lesson(user)
    elif action == 'Найти коллег':
        yield from find_colleagues(user)
    elif action == 'Посмотреть актуальные предложения':
        yield from current_offers(user)
    elif action == 'На сайт':
        link = 'bot.mipt.ru'
        yield link, keyboards.back()
