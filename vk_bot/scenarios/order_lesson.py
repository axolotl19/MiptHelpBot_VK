import keyboards
import backend_calls as backend


def order_lesson(user):
    order = dict()

    answer = 'Какая категория предметов Вас интересует?'
    subjects = backend.subjects(user)

    if not subjects:
        answer = 'Извините, Вы наткнулись на баг. Пожалуйста, опишите ситуацию в обсуждениях группы, и мы попытаемся это исправить. Честно-честно.'
    
    keyboard = keyboards.catalogue(subjects.keys(), per_line=1)
    category = yield answer, keyboard
 
    answer = 'Чтобы запросить бесплатный урок, выберите предмет из списка.'
    keyboard = keyboards.catalogue(subjects[category].keys(), per_line=2)
    subject = yield answer, keyboard
    order['subject_id'] = subjects[category][subject]

    answer = 'Oпишите тему урока, например "Двойные интегралы".'
    keyboard = keyboards.back()
    order['title'] = yield answer, keyboard

    answer = 'Расскажите более подробно, например "Не понимаю вообще ничего", или "Помогите с теорией".'
    order['description'] = yield answer, None

    answer = 'Заказать бесплатный урок по предмету "{}" с подробностями "{}" и "{}"?'.format(subject, order['title'], order['description'])
    keyboard = keyboards.confirmation()
    confirm = yield answer, keyboard

    keyboard = keyboards.back()
    if 'Ok' in confirm:
        if backend.post_lesson_order(user, order):
            answer = 'Запрос на бесплатный урок получен, ждите ответа от преподавателей в системе.'
        else:
            answer = 'Извините, Вы наткнулись на баг. Пожалуйста, опишите ситуацию в обсуждениях группы, и мы попытаемся это исправить. Честно-честно.'
    else:
        answer = 'Запрос отменен'
    yield answer, keyboard
