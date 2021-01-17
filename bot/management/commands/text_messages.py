from django.conf import settings

START_MESSAGE = \
    """Добро пожаловать в бота!

Что умеет этот бот? 
- Пришли ему анкету из бота дайвинчика и получи ссылку на на владельца анкеты!

Как получить доступ к базе данных анкет?
- Просто пришли боту 5 анкет с вазимной симпатией. Бот распозанет все виды взаимных симпатий.

Можно пример?
- Да, конечно! Тут есть небольшое руководство: https://telegra.ph/Kak-polzovatsya-botom-01-17"""

QUESTIONNAIRE_ALREADY_IS_EXIST = \
    """Анкета уже существует, попробуйте другую."""

QUESTIONNAIRE_ADDED = \
    """Анкета "{name}" добавлена, спасибо. \n\nВы уже добавили {count_added_questionnaire} анкет"""

QUESTIONNAIRE_ADDED_PROFILE_URL = \
    """Анкета добавлена, спасибо. \n\nВы уже добавили {count_added_questionnaire} анкет"""


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
