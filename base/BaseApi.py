import requests


class BaseApi:
    headers = {'content-type': 'application/json;charset=UTF-8',
               'sign': 'c8036e419c856168a4a8ae901c87b855',
               'pp_storeid': 'a3f5582f-7c6f-4c42-8736-72c8f9620656',
               'timestamp': '1632649405688',
               'pp-os': '20',
               'pp-version': '2021042003',
               'Accept-Language': 'zh-Hans-CN;q=1.0',
               'User-Agent': 'Pupumall/2.7.0;iOS 14.8;188AA86D-3DBE-4E30-8E91-2D77FCB62F93',
               'Accept-Encoding': 'gzip;q=1.0, compress;q=0.5',
               'mark-num': '30',
               'Connection': 'keep-alive',
               'Cookie': 'JSESSIONID=3262A7582383C6CEE479506F7733EFAD',
               }
    host1 = 'https://j1.pupuapi.com'

    def base_request_get(self, path, params=None, **kwargs):
        url = self.host1 + path
        return requests.get(url, headers=self.headers, params=params, **kwargs)

    def base_request_post(self, path, data=None, **kwargs):
        url = self.host1 + path
        return requests.post(url, headers=self.headers, data=data, **kwargs)