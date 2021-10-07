from api.client.user.info.edit_nickname import EditNickname
import random


def edit_nickname():
    res = EditNickname.edit_nickname(random.randint(0, 9))
    print(res.text)
