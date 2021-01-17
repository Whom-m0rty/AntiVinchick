class Message():
    def __init__(self, event, Vk):
        self.peer_id = event.message.from_id
        self.text = event.message.text
        self.is_registered = bool
        self.vk = Vk
        self.have_fwd_message = False
        self.questionnaire_is_mutual_sympathy = False
        self.questionnaire_is_liked = False
        self.questionnaire_is_profile_url = False

        if event.object.message['fwd_messages']:
            if event.object.message['fwd_messages'][0]['from_id'] == -91050183:
                self.have_fwd_message = True
                self.fwd_message_text = event.object.message['fwd_messages'][0]['text']
                if event.object.message['fwd_messages'][0]['attachments']:
                    self.questionnaire_photo_url = event.object.message['fwd_messages'][0]['attachments'][0]['photo']['sizes'][-1][
                        'url'].split('?')[0]

                if 'Есть взаимная симпатия! Добавляй в друзья -' in self.fwd_message_text:
                    self.questionnaire_is_mutual_sympathy = True
                    self.profile_url = self.fwd_message_text.split('\n\n')[0].split(' ')[-1]

                if 'Кому-то понравилась твоя анкета' in self.fwd_message_text:
                    self.questionnaire_is_liked = True

                if 'Отлично! Надеюсь хорошо проведете время ;) добавляй в друзья -' in self.fwd_message_text:
                    self.questionnaire_is_profile_url = True
                    print(self.fwd_message_text.split('-')[1].replace('\n\nКому', ''))
                    self.questionnaire_profile_url = self.fwd_message_text.split('-')[1].replace('\n\nКому', '')

                self.questionnaire_text = self.fwd_message_text.split('\n\n')
                if len(self.questionnaire_text) != 1 and '1. Оценить еще кого-то.' not in self.questionnaire_text[1]:
                    del self.questionnaire_text[0]
                    if self.questionnaire_is_profile_url:
                        del self.questionnaire_text[0]
                    self.questionnaire_text = ''.join(self.questionnaire_text)
                    self.questionnaire_name = self.questionnaire_text.split(',')[0].strip()
                    self.questionnaire_city = self.questionnaire_text.split(',')[2].split('\n')[0].strip()
                    self.questionnaire_age = self.questionnaire_text.split(',')[1].strip()


