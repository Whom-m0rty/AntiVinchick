
from bot.management.commands.hundlers import questionnaire
from bot.management.commands.utils.user import *
from bot.management.commands.types.types import Message



def process_event_new_message(event, Vk):
    message = Message(event, Vk)

    if check_is_registered(peer_id=message.peer_id):
        message.is_registered = True

        have_access = have_access_bd(peer_id=message.peer_id)

        if message.text == 'Начать':
            questionnaire.help_add_questionnaire(message)
        elif message.have_fwd_message:
            if message.questionnaire_is_profile_url:
                questionnaire.add_questionnaire_profile_url(message)
            if message.questionnaire_is_mutual_sympathy or message.questionnaire_is_liked:
                questionnaire.add_questionnaire(message)
            if not message.questionnaire_is_profile_url and not message.questionnaire_is_mutual_sympathy and\
                    not message.questionnaire_is_liked:
                if have_access:
                    questionnaire.check_questionnaire(message)
                else:
                    questionnaire.you_not_have_access(message)


    else:
        register_user(peer_id=message.peer_id)
        process_event_new_message(event, Vk)
