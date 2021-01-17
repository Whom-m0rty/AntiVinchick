import vk_api
from django.core.management import BaseCommand
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from django.conf import settings

from .updater import updater


def start_longpoll():
    vk_session = vk_api.VkApi(token=settings.VK_BOT_TOKEN)
    Vk = vk_session.get_api()

    longpoll = VkBotLongPoll(vk_session, settings.VK_GROUP_ID)

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            updater.process_event_new_message(event, Vk)


class Command(BaseCommand):

    def handle(self, *args, **options):
        start_longpoll()
