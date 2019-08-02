import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


session = vk_api.VkApi(token="bc79895eff83b593c20d6e26f1aa5476259684fbade1fc225fd3d19303e456fc446a0a3478a340c674ed2")
longpoll = VkLongPoll(session)
vk = session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.from_user:
            vk.messages.send(
                user_id = event.user_id,
                random_id = event.random_id,
                message = event.text
            )
