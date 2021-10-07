from base.BaseApi2 import BaseApi
import json

class EditNickname:
    def edit_nickname(self, nickname):
        path = '/clientauth/user/info/nickname'
        nickname = {"nickname": nickname}
        data=json.dumps(nickname)
        res = BaseApi().get_request_put(path, data=data)
        return res


if __name__ == '__main__':
    print(EditNickname().edit_nickname('白胖').json())
