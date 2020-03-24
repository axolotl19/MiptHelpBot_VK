# -*- coding: utf-8 -*-

import vkapi
from dialog import dialog
from backend_calls import check_user
import mailout

sessions = dict()

def make_answer(user, message):
    if message == 'Меню':
        try:
            del sessions[user]
        except KeyError:
            pass

    if message == 'Откликнуться':
        answer, keyboard = mailout.accepted(user, sessions[user])
        del sessions[user]
        return answer, keyboard

    if user in sessions:
        try:
            answer, keyboard = sessions[user].send(message)
            return answer, keyboard
        except StopIteration:
            del sessions[user]

    if check_user(user):
        sessions[user] = dialog(user)
        answer, keyboard = next(sessions[user])
        return answer, keyboard

    answer = 'Здравствуйте! Чтобы пользоваться ботом, подключите, пожалуйста, ваш адрес вк к аккаунту на Mipt Help Bot. Это можно сделать тут:\nhttps://bot.mipt.ru/user/edit'
    keyboard = ''

    return answer, keyboard


def send_answer(data, token):
    user_id = data['from_id']
    message = data['text']
    user = vkapi.id_to_link(user_id, token)
    answer, keyboard = make_answer(user, message)
    vkapi.send_message(user_id, token, answer, keyboard)


def send_mailout(data, token):
    message, keyboard = mailout.offer(data['offer']['type'], data['offer']['info'])
    for user in data['users']:
        sessions[user] = data['offer']
        user_id = vkapi.link_to_id(user, token)
        vkapi.send_message(user_id, token, message, keyboard)
