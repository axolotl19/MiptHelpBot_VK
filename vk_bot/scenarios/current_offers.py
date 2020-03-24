import keyboards
import backend_calls as backend


def current_offers(user):
    answer = 'Какие предложения Вас интересуют?'
    keyboard = keyboards.which_offers()
    section = yield answer, keyboard

    if section == 'Уроки':
        yield from lessons(user)
    if section == 'Коллеги':
        yield from colleagues(user)


def lessons(user):
    offers = backend.lesson_offers(user)
    heads = list(offers.keys())

    while True:
        choice = yield from scroll_keyboard(heads)
        offer = offers[choice]

        answer = 'Нужна помощь по теме "{}".\nОписание: "{}".\nНажмите "Принять", чтобы откликнуться.'.format(offer[1], offer[2])
        keyboard = keyboards.accept()
        decision = yield answer, keyboards.accept()

        if decision == 'Принять':
            answer = 'Извините, Вы наткнулись на баг. Пожалуйста, опишите ситуацию в обсуждениях группы, и мы попытаемся это исправить. Честно-честно.'

            if backend.accept_lesson_offer(user, offer[0]):
                answer = 'Вы приняли урок. Напишите, пожалуйста, этому человеку: {}, он ждет Вашего ответа.'.format(offer[3])

            yield answer, keyboards.back()


def colleagues(user):
    offers = backend.colleague_offers(user)
    heads = list(offers.keys())

    while True:
        choice = yield from scroll_keyboard(heads)
        offer = offers[choice]

        answer = offer[1]
        keyboard = keyboards.accept()
        decision = yield answer, keyboards.accept()

        if decision == 'Принять':
            answer = 'Извините, Вы наткнулись на баг. Пожалуйста, опишите ситуацию в обсуждениях группы, и мы попытаемся это исправить. Честно-честно.'

            if backend.accept_colleague_request(user, offer[0]):
                answer = 'Напишите, пожалуйста, {}.\n'.format(offer[2])

            if offer[3]:
                answer += 'Также этой темой заинтересовались:\n{}Вы можете написать им тоже.'.format(offer[3])

            yield answer, keyboards.back()


def scroll_keyboard(heads):
    answer = 'Выберите заявку из списка.'
    k, n = 0, 4
    need_more = n < len(heads)
    keyboard = keyboards.catalogue(heads[k:n], more=need_more)
    choice = yield answer, keyboard 

    while choice == 'Далее':
        k, n = k+4, n+4
        if n >= len(heads):
            need_more = False
        keyboard = keyboards.catalogue(heads[k:n], more=need_more)
        choice = yield '(далее)', keyboard

    return choice
