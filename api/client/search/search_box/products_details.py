from base.BaseApi import BaseApi
from api.client.search.search_box.search_products import Products


class ProductsDetail:
    def get_product_details(self,search_term):
        product=Products()
        product.set_product_id(search_term)
        path = '/client/product/storeproduct/detail/a3f5582f-7c6f-4c42-8736-72c8f9620656/'+product.product_id
        res = BaseApi().base_request_get(path)
        return res
