# import requests
import requests

class BaseApi:
    headers = {'mark-num': '88',
               'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIiLCJhdWQiOiJodHRwczovL3VjLnB1cHVhcGkuY29tIiwiaXNfbm90X25vdmljZSI6IjEiLCJpc3MiOiJodHRwczovL3VjLnB1cHVhcGkuY29tIiwiZ2l2ZW5fbmFtZSI6IuWTiOWTiOWTiOWTiCIsImV4cCI6MTYzMjg0NjA2OCwidmVyc2lvbiI6IjIuMCIsImp0aSI6IjZkOTZmYzBiLTNjMjMtNGFiOC04ODE0LTg3YjQ2M2I0YmE1ZCJ9.OMAruq1nkX67_PsG2sYtZTXCySmQsEFpUWTVSIsTREc',
               'Accept': '*/*',
               'pp-userid': '6d96fc0b-3c23-4ab8-8814-87b463b4ba5d',
               'pp-version': '2021042003',
               'Accept-Encoding': 'gzip;q=1.0, compress;q=0.5',
               'pp-os': '20',
               'Accept-Language': 'zh-Hans-CN;q=1.0',
               'Content-Type': 'application/json',
               'pp_storeid': 'a3f5582f-7c6f-4c42-8736-72c8f9620656',
               'Content-Length': '24',
               'User-Agent': 'Pupumall/2.7.0;iOS 14.8;188AA86D-3DBE-4E30-8E91-2D77FCB62F93',
               'Connection': 'keep-alive',
               'Cookie': 'JSESSIONID=3262A7582383C6CEE479506F7733EFAD'
               }
    host = 'https://cauth.pupuapi.com'

    def get_request_put(self, path, data=None, **kwargs):
        url = self.host + path
        return requests.put(url, headers=self.headers, data=data, **kwargs)
