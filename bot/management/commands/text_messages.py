from django.conf import settings

START_MESSAGE = \
    """Просто перешли мне анкету, я сам все сделаю за тебя!"""

QUESTIONNAIRE_ALREADY_IS_EXIST = \
    """Анкета уже существует, попробуйте другую."""

QUESTIONNAIRE_ADDED = \
    """Анкета "{name}" добавлена, спасибо. \n\nВы уже добавили {count_added_questionnaire} анкет"""



QUESTIONNAIRE_NEED_PROFILE_URL = \
    """Отлично! Теперь перешлите мне сообщение с ссылкой на страницу"""

QUESTIONNAIRE_FOUND = \
    """Анкета найдена:
Город: {city}
Имя: {name}
Возраст: {age}

{questionnaire_text}

Ссылка на профиль: {profile_link}
"""
QUESTIONNAIRE_NOT_FOUND = 'К сожалению, анкета не найдена.'

YOU_NOT_HAVE_ACCESS = f'Вам необходимо дбавить {settings.NEED_TO_ACCESS} анкет для того, что бы получить доступ к поиску.'
