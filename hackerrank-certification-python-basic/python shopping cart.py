#!/bin/python3

import math
import os
import random
import re
import sys


class Item:
    # Implement the Item here
    def __init__(self, name, price):
        self.name=name
        self.price=price
        print('item {} {}'.format(self.name, self.price))

class ShoppingCart:
    # Implement the ShoppingCart here
    def __init__(self):
        self.sumPrice=0
        self.sumItem=0
        pass

    def __len__(self):
        print('returned sumItem {}'.format(self.sumItem))
        return self.sumItem
        
    def add(self, item):
        print('added {} {}'.format(item.name, item.price))
        self.sumPrice += item.price
        self.sumItem += 1
        pass
    
    def total(self):
        print('returned sumPrice {}'.format(self.sumPrice))
        return self.sumPrice

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    items = []
    for _ in range(n):
        name, price = input().split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input())
    for _ in range(q):
        line = input().split()
        command, params = line[0], line[1:]
        if command == "len":
            fptr.write(str(len(cart)) + "\n")
        elif command == "total":
            fptr.write(str(cart.total()) + "\n")
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)
            cart.add(item)
        else:
            raise ValueError("Unknown command %s" % command)
            
    fptr.close()
