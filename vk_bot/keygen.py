# -*- coding: utf-8 -*-

import base64, hashlib

password = ''
salt = ''
digest = hashlib.sha256
iterations = 
hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), iterations)
hash = base64.b64encode(hash).decode('ascii').strip()

with open('vk_settings.py', 'a') as key:
        key.write("secret = '{}'".format(hash))
