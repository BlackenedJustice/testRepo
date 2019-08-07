from vk_api.longpoll import VkLongPoll, VkEventType


import vk_api

tokenn='d0a27ef71602aca5d4ab459fdf5b3b9e969f6c7f3c39a936949774ef086c87d375f087b8b2aecc51a582f'
vk_session = vk_api.VkApi(token=tokenn)
from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.text and not(event.from_me):
            print('lett')
            vk_session.method('messages.send', {'user_id': event.user_id, 'message': event.text, 'random_id': 0})

