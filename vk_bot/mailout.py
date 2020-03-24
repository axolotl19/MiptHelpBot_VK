import keyboards
import backend_calls as backend


def offer(offer_type, info):
    if offer_type == 'lesson':
        message = 'Предлагаем урок по предмету "{}", тема: "{}",\nописание:"{}".\nНажмите "Откликнуться", чтобы помочь человеку с учебой.'.format(info[0], info[1], info[2])

    elif offer_type == 'colleague':
        message = 'Ищут коллег по теме: "{}",\nописание: {}.\nНажмите "Откликнуться", чтобы разобраться в вопросе вместе.'.format(info[0], info[1])

    keyboard = keyboards.mailout()

    return message, keyboard


def accepted(user, offer):
    answer = 'Извините, Вы наткнулись на баг. Пожалуйста, опишите ситуацию в обсуждениях группы, и мы попытаемся это исправить. Честно-честно.'

    if offer['type'] == 'lesson':
        if backend.accept_lesson_offer(user, offer['id']):
            applicant = backend.contact_str(offer['applicant'][0], offer['applicant'][1])
            answer = 'Вы приняли урок. Напишите, пожалуйста, этому человеку: {}, он ждет Вашего ответа.'.format(applicant)

    elif offer['type'] == 'colleague':
            if backend.accept_colleague_request(user, offer['id']):
                pass

            applicant = backend.contact_str(offer['applicant'][0], offer['applicant'][1])
            answer = 'Напишите, пожалуйста, {}.\n'.format(applicant)

            if offer['participants']:
                participants = ''
                for user in offer['participants']:
                    participants += backend.contact_str(user[0], user[1]) + '\n'
                
                answer += 'Также этой темой заинтересовались:\n{}Вы можете написать им тоже.'.format(participants)

    return answer, keyboards.back()
