#!/usr/bin/python
# coding: UTF-8
from collections import namedtuple
# Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
# sub = Subscriber('jonesy@example.com', '2012-10-19')
# print sub
# Subscriber(addr='jonesy@example.com', joined='2012-10-19')
# print sub.addr
# print sub.joined

Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
    total += s.shares * s.price
    return total


s = Stock('ACME', 100, 123.45)



Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)


# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

print stock_prototype
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print dict_to_stock(a)