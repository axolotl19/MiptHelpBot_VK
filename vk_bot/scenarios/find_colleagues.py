import keyboards
import backend_calls as backend


def find_colleagues(user):
    request = dict()

    answer = 'Какая категория предметов Вас интересует?'
    subjects = backend.subjects(user, pupil=True)
    if not subjects:
        answer = 'Похоже, что Вы ещё не выбрали интересные Вам предметы. Добавить их Вы можете в личном кабинете на нашем сайте.\nhttps://bot.mipt.ru/student/amigo'
    
    keyboard = keyboards.catalogue(subjects.keys(), per_line=1)
    category = yield answer, keyboard
 
    answer = 'Чтобы найти коллег по интересующей вас теме или предмету, выберите его из списка:'
    keyboard = keyboards.catalogue(subjects[category].keys(), per_line=2)
    subject = yield answer, keyboard
    request['subject_id'] = subjects[category][subject]

    answer = 'Расскажите подробнее, например "Ищу, с кем бы обсудить матан и зарешать задавальник".'
    request['description'] = yield answer, keyboards.back()

    answer = 'Подтвердить запрос?'
    keyboard = keyboards.confirmation()
    confirm = yield answer, keyboard

    keyboard = keyboards.back()
    if 'Ok' in confirm:
        if backend.post_colleague_request(user, request):
            answer = 'Запрос на поиск коллег создан, ждите ответа от других пользователей.'
        else:
            answer = 'Извините, Вы наткнулись на баг. Пожалуйста, опишите ситуацию в обсуждениях группы, и мы попытаемся это исправить. Честно-честно.' 
    else:
        answer = 'Запрос отменен.'

    yield answer, keyboard


