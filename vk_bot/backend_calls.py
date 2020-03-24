from authorisation.backend import *
import requests, json
from collections import defaultdict


def check_user(user):
    r = requests.get('http://bot.mipt.ru/api/categories', auth=(user, password))
    if r.status_code == 200:
        return True
    else:
        return False


def subjects(user, pupil=False):
    which_subjects = 'subjects'
    if pupil:
        which_subjects = 'pupil_subjects'

    r = requests.get('http://bot.mipt.ru/api/{}/'.format(which_subjects), auth=(user, password))
    subjects = defaultdict(dict)
    for item in r.json():
        if pupil:
            item = item['subject']
        title = item['title']
        subject_id = item['id']
        category = item['category']
        subjects[category][title] = subject_id

    r = requests.get('http://bot.mipt.ru/api/categories', auth=(user, password))
    for item in r.json():
        cat_id = item['id']
        title = item['title']
        if cat_id in subjects.keys():
            subjects[item['title']] = subjects.pop(cat_id)
            
    return subjects


def post_lesson_order(user, order):
    r = requests.post('http://bot.mipt.ru/api/lessons/pupil/', data=order, auth=(user, password))
    if r.status_code == 201:
        return True
    else:
        return False


def post_colleague_request(user, request):
    r = requests.post('http://bot.mipt.ru/api/colleague_requests/my/', data=request, auth=(user, password))
    if r.status_code == 201:
        return True
    else:
        return False


def lesson_offers(user):
    r = requests.get('http://bot.mipt.ru/api/applications/', auth=(user, password))
    offers = dict()
    for item in r.json():
        subject = item['subject']['title']
        title = item['title']
        description = item['description']
        head = subject  + ': ' + title
        if len(head) > 40:
            head = head[:37] + '...'
        offer_id = item['id']

        pupil = item['pupils'][0]
        contact = contact_str(pupil['vk_url'], pupil['telegram'])
        offers[head] = [offer_id, title, description, contact]

    return offers 


def colleague_offers(user):
    r = requests.get('http://bot.mipt.ru/api/colleague_requests/interesting/', auth=(user, password))
    offers = dict()
    for item in r.json():
        subject = item['subject']['title']
        description = item['description']
        head = subject  + ': ' + description
        if len(head) > 40:
            head = head[:37] + '...'
        offer_id = item['id']

        participants = ''
        for user in item['participants']:
            participants += contact_str(user['vk_url'], user['telegram']) + '\n'

        user = item['user']
        user = contact_str(user['vk_url'], user['telegram'])
        offers[head] = [offer_id, description, user, participants]
    

    return offers


def accept_lesson_offer(user, offer_id):
    r = requests.put('http://bot.mipt.ru/api/applications/{}/confirm/'.format(offer_id), auth=(user, password))
    if r.status_code == 200:
        return True
    else:
        return False


def accept_colleague_request(user, offer_id):
    r = requests.post('http://bot.mipt.ru/api/colleague_requests/interesting/{}/join/'.format(offer_id), auth=(user, password))
    if r.status_code == 200:
        return True
    else:
        return False


def contact_str(vk_url, telegram):
    if vk_url:
        contact = vk_url
        if telegram:
            contact += ' (tg: @' + telegram + ')'
    elif telegram:
        contact = 'tg: @' + telegram
    else:
        return None

    return contact
 
