from django.conf import settings

from bot.models import User, Questionnaire


def check_is_registered(peer_id: int) -> bool:
    if User.objects.filter(peer_id=peer_id):
        return True
    else:
        return False


def register_user(peer_id: int):
    User.objects.create(peer_id=peer_id)


def mark_user_as_input_profile_url(peer_id: int, questionnaire: Questionnaire):
    user = User.objects.get(peer_id=peer_id)
    user.is_input_profile_url = True
    user.profile_url_for = questionnaire
    user.save()


def nullify_user(peer_id: int):
    user = User.objects.get(peer_id=peer_id)
    user.is_input_profile_url = False
    user.profile_url_for = None
    user.save()


def have_access_bd(peer_id: int):
    user = User.objects.get(peer_id=peer_id)
    return user.have_access


def add_questionnaire_added_by_user(peer_id: int):
    user = User.objects.get(peer_id=peer_id)
    user.number_of_added += 1
    if not user.have_access:
        if user.number_of_added >= settings.NEED_TO_ACCESS:

            user.have_access = True
    user.save()


def get_count_added_questionnaire(message):
    return User.objects.get(peer_id=message.peer_id).number_of_added
