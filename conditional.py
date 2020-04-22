# -*- coding: utf-8 -*-
x = 1
y = 5

def compare_values(x, y):

    if x > y:
        print("x is higher than y")
    else:
        if x == y:
            print ("x is the same than y")
        else:
            print("x is less than y")

while x < 10:
    print(x)
    compare_values(x, y)
    x += 1
