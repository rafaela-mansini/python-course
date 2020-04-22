# -*- coding: utf-8 -*-

#Lesson: while structure
x = 1
y = 5

def compare_values(x, y):

    if x > y:
        #print("x is higher than y")
        return "x is higher than y"
    else:
        if x == y:
            #print ("x is the same than y")
            return "x is the same than y"
        else:
            #print("x is less than y")
            return "x is less than y"

while x < 10:
    print x,": ",compare_values(x, y)
    compare_values(x, y)
    x += 1

print("\n")
#Lesson: for structure
list_of_king_books = ["It", "The Stand", "The Shining", "The Institute", "The Outsider", "Doctor Sleep", "November 63", "Joyland"]

for book in list_of_king_books:
    print(book)