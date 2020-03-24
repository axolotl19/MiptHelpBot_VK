from vk_api import keyboard
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

def main_menu():
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button('Запросить урок', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('Найти коллег', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Посмотреть актуальные предложения', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('На сайт', color=VkKeyboardColor.PRIMARY)
    
    keyboard = keyboard.get_keyboard()
    
    return keyboard


def catalogue(item_list, per_line=1, more=False):
    keyboard = VkKeyboard(one_time=True)

    i=0
    for item in item_list:
        keyboard.add_button(item, color=VkKeyboardColor.POSITIVE)
        i += 1
        if i % per_line == 0:
            keyboard.add_line()
    if i % per_line != 0:
        keyboard.add_line()

    if more:
        keyboard.add_button('Далее', color=VkKeyboardColor.PRIMARY)

    keyboard.add_button('Меню', color=VkKeyboardColor.PRIMARY)
    keyboard = keyboard.get_keyboard()
    
    return keyboard


def confirmation():
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Ok', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('Отмена', color=VkKeyboardColor.NEGATIVE)
    keyboard = keyboard.get_keyboard()
    
    return keyboard


def back():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Меню', color=VkKeyboardColor.PRIMARY)
    keyboard = keyboard.get_keyboard()

    return keyboard


def which_offers():
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button('Уроки', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('Коллеги', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Меню', color=VkKeyboardColor.PRIMARY)
    
    keyboard = keyboard.get_keyboard()
    
    return keyboard


def accept():
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button('Принять', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Меню', color=VkKeyboardColor.PRIMARY)
    
    keyboard = keyboard.get_keyboard()
    
    return keyboard


def mailout():
    keyboard = VkKeyboard(one_time=False)

    keyboard.add_button('Откликнуться', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Меню', color=VkKeyboardColor.PRIMARY)
    
    keyboard = keyboard.get_keyboard()
    
    return keyboard
