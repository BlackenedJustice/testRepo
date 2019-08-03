import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token='fe8251b32fad3cc0b2425ff1242c1f59b4ab3f86829cb0f868fd77ba9fdf86cc361bf378384ab4d1e2a0f')

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.from_user:
            vk.messages.send(
                user_id=event.user_id,
                random_id=event.random_id,
                message=event.text
            )
