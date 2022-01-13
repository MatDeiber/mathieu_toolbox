from mathieu_toolbox.coin_price import coin_price


def test_price():

    df = coin_price(2021,7,3)
    assert df['price'][0] == '34668.55'
