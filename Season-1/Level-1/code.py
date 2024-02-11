'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    # net = 0
    net_payment = 0
    net_product = 0

    for item in order.items:
        if item.type == 'payment':
            net_payment += item.amount
        elif item.type == 'product':
            net_product -= item.amount * item.quantity
        else:
            return "Invalid item type: %s" % item.type

    net = round(net_payment,2) + round(net_product,2) 
    if net_product <-99999 or net_payment > 99999:
            print(f"Order ID: {order.id} - Total amount payable for an order exceeded")
            return "Total amount payable for an order exceeded"
    else:    
        if net != 0:
            print("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net))
            return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
        else:
            print("Order ID: %s - Full payment received!" % order.id)
            return "Order ID: %s - Full payment received!" % order.id