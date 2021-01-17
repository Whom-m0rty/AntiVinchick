from bot.management.commands.types import types
from vk_api.utils import get_random_id
from bot.management.commands.keyboards import questionnaire_keyboard
from bot.management.commands import text_messages
from bot.management.commands.utils import questionnaire, user


def start_message(message: types.Message):
    message.vk.messages.send(
        user_id=message.peer_id,
        random_id=get_random_id(),
        message=text_messages.START_MESSAGE,
        keyboard=questionnaire_keyboard.add_questionnaire()
    )


def help_add_questionnaire(message: types.Message):
    message.vk.messages.send(
        user_id=message.peer_id,
        random_id=get_random_id(),
        message=text_messages.HELP_MESSAGE,
        keyboard=questionnaire_keyboard.add_questionnaire()
    )


def add_questionnaire_profile_url(message: types.Message):
    if not questionnaire.check_questionnaire_exist(message, profile_url=message.questionnaire_profile_url):
        questionnaire.add_questionnaire_profile_url(message)

        text = text_messages.QUESTIONNAIRE_ADDED_PROFILE_URL.format(
            count_added_questionnaire=user.get_count_added_questionnaire(message)
        )
        message.vk.messages.send(
            user_id=message.peer_id,
            random_id=get_random_id(),
            message=text,
        )
    else:
        user.nullify_user(peer_id=message.peer_id)
        message.vk.messages.send(
            user_id=message.peer_id,
            random_id=get_random_id(),
            message=text_messages.QUESTIONNAIRE_ALREADY_IS_EXIST,
        )


def add_questionnaire(message: types.Message):
    if questionnaire.check_questionnaire_exist(message):
        message.vk.messages.send(
            user_id=message.peer_id,
            random_id=get_random_id(),
            message=text_messages.QUESTIONNAIRE_ALREADY_IS_EXIST,
        )
    else:
        if message.questionnaire_is_mutual_sympathy:
            questionnaire.add_questionnaire(message)
            text = text_messages.QUESTIONNAIRE_ADDED.format(
                name=message.questionnaire_name,
                count_added_questionnaire=user.get_count_added_questionnaire(message)
            )
            message.vk.messages.send(
                user_id=message.peer_id,
                random_id=get_random_id(),
                message=text,
            )
        elif message.questionnaire_is_liked:
            added_questionnaire = questionnaire.add_questionnaire(message, is_liked=True)
            user.mark_user_as_input_profile_url(peer_id=message.peer_id, questionnaire=added_questionnaire)
            message.vk.messages.send(
                user_id=message.peer_id,
                random_id=get_random_id(),
                message=text_messages.QUESTIONNAIRE_NEED_PROFILE_URL
            )


def check_questionnaire(message: types.Message):
    found_questionnaire = questionnaire.check_questionnaire_exist(message)
    if found_questionnaire:
        text = text_messages.QUESTIONNAIRE_FOUND.format(
            city=found_questionnaire.city,
            age=found_questionnaire.age,
            questionnaire_text=found_questionnaire.text,
            name=found_questionnaire.name,
            profile_link=found_questionnaire.profile_url
        )
        message.vk.messages.send(
            user_id=message.peer_id,
            random_id=get_random_id(),
            message=text,
        )
    else:
        message.vk.messages.send(
            user_id=message.peer_id,
            random_id=get_random_id(),
            message=text_messages.QUESTIONNAIRE_NOT_FOUND,
        )


def you_not_have_access(message):
    message.vk.messages.send(
        user_id=message.peer_id,
        random_id=get_random_id(),
        message=text_messages.YOU_NOT_HAVE_ACCESS,
    )
