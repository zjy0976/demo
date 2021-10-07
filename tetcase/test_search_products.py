from api.client.search.search_box.search_products import Products

def test_search_product():
    product = Products()
    res = product.get_search_products('火龙果')
    # assert res.status_code==200
    # assert res.json()['data']['count']==8
    print(res.text)



