import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

def main():

    vk_session = vk_api.VkApi(token='82427e0f0fa1d6b0f4d8b38a819e14c25984a418e3dad5b8330b7e948d22afa4134ed0a41a67ad30f80e4')

    vk = vk_session.get_api()

    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            vk.messages.send(
                user_id=event.user_id,
                random_id=get_random_id(),
                message=event.text
            )
            print('ok')

if __name__ == '__main__':
    main()