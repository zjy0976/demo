from api.client.search.search_box.products_details import ProductsDetail

def test_product_details():
    product_details = ProductsDetail()
    res = product_details.get_product_details('火龙果')
    print(res.text)
    assert res.json()['errcode']==0
    assert res.status_code==200
