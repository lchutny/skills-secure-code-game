import code as c

tv_item = c.Item(type='product', description='tv', amount=1000.00, quantity=1)
payment = c.Item(type='payment', description='invoice_4', amount=1e19, quantity=1)
payback = c.Item(type='payment', description='payback_4', amount=-1e19, quantity=1)
order_4 = c.Order(id='4', items=[payment, tv_item, payback])

tt = c.validorder(order_4)

print(tt)