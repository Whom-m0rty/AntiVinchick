from typing import Union
from bot.management.commands.utils.user import *
from bot.models import Questionnaire, User


def check_questionnaire_exist(message, profile_url=False) -> Union[Questionnaire, bool]:
    if profile_url:
        questionnaire = Questionnaire.objects.filter(
            profile_url=profile_url
        )
        if questionnaire:
            if questionnaire.last().profile_url != 'null':
                return questionnaire.last()
    else:
        questionnaire = Questionnaire.objects.filter(
            photo_url=message.questionnaire_photo_url
        )
        if questionnaire:
            if questionnaire.last().profile_url != 'null':
                return questionnaire.last()

        questionnaire = Questionnaire.objects.filter(
            text=message.questionnaire_text
        )
        if questionnaire:
            if questionnaire.last().profile_url != 'null':
                return questionnaire.last()

    return False


def add_questionnaire(message, is_liked=False):
    if not is_liked:
        profile_url = message.profile_url
        add_questionnaire_added_by_user(peer_id=message.peer_id)
    else:
        profile_url = 'null'

    return Questionnaire.objects.create(
        photo_url=message.questionnaire_photo_url,
        name=message.questionnaire_name,
        text=message.questionnaire_text,
        city=message.questionnaire_city,
        age=message.questionnaire_age,
        profile_url=profile_url,
    )


def add_questionnaire_profile_url(message):
    user = User.objects.get(peer_id=message.peer_id)
    if user.is_input_profile_url:
        questionnaire = user.profile_url_for
        questionnaire.profile_url = message.questionnaire_profile_url.strip()
        questionnaire.save()
        user.profile_url_for_id = None
        user.is_input_profile_url = False
        user.save()
        add_questionnaire_added_by_user(peer_id=message.peer_id)
