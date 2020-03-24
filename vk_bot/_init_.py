#!/usr/bin/python3

from flask import Flask, request, json
from authorisation.vk import *
import message_handler

app = Flask(__name__)

@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if data['secret'] != secret:
        return 'You shall not pass!'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        message_handler.send_answer(data['object'], token)
        return 'ok'
    else:
        return 'ok'

@app.route('/mailout',  methods=['POST'])
def mailout():
    data = json.loads(request.data)
    message_handler.send_mailout(data, token)
    return 'Ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
