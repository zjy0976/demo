from base.BaseApi import BaseApi

class Products(BaseApi):
    def __init__(self, product_id=None):
        self.product_id = product_id

    def get_search_products(self, search_term):
        path = '/client/search/search_box/products'
        params = {'page': 1, 'search_term': search_term, 'search_term_from': 20, 'size': 20, 'sort': 0,
                  'store_id': 'a3f5582f-7c6f-4c42-8736-72c8f9620656'}
        res = BaseApi().base_request_get(path, params=params)

        return res

    def set_product_id(self, search_term):
        self.product_id = self.get_search_products(search_term).json()['data']['products'][0]['product_id']


    def get_product_id(self):
        return self.product_id
