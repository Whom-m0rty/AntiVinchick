from vk_api.keyboard import VkKeyboard, VkKeyboardColor



def add_questionnaire():
    keyboard = VkKeyboard(one_time=True)
    keyboard.add_button('Добавть анкету', color=VkKeyboardColor.POSITIVE)
    return keyboard.get_keyboard()
