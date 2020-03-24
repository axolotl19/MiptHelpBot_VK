import vk

session = vk.Session()
api = vk.API(session, v=5.101)


def send_message(user_id, token, message, keyboard=''):
    api.messages.send(access_token=token, user_id=str(user_id), random_id=0, message=message, keyboard=keyboard)


def link_to_id(link, token):
    screen_name = link.split('/')[-1] 
    user_id = api.users.get(access_token=token, user_ids=screen_name)[0]['id']
    return user_id


def id_to_link(user_id, token):
    screen_name = api.users.get(access_token=token, user_ids=user_id, fields='screen_name')[0]['screen_name']
    link = 'vk.com/' + screen_name
    return link
