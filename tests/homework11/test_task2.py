from homework11.task2 import ElderDiscount, MorningDiscount, Order


def test_get_order_price_no_discount():
    """Testing that getting order final price without discount gives original
    price."""
    order = Order(100)
    assert order.get_final_price() == 100


def test_get_morning_order_price():
    """Testing that getting final price for order with morning discount
    reduces original price by 25%."""
    order = Order(100)
    order.set_discount(MorningDiscount)
    assert order.get_final_price() == 75


def test_get_elder_order_price():
    """Testing that getting final price for order with morning discount
    reduces original price by 40%."""
    order = Order(100)
    order.set_discount(ElderDiscount)
    assert order.get_final_price() == 60
