from vk_api.keyboard import VkKeyboard, VkKeyboardColor



def add_questionnaire():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Добавить анкету', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('Поиск анкеты', color=VkKeyboardColor.SECONDARY)
    return keyboard.get_keyboard()
