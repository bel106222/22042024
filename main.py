"""
Написать функцию с использование python turtle.
Функция получает список или строку на входе и 
рисует черепашкой квадратик со стороной, равной
каждому числу из него подряд через отступ.
"""

import turtle

def square(lst):
    for i in range(len(lst)):
        current_len = int(lst[i])
        for j in range(4):
            turtle.pendown()
            turtle.forward(current_len)
            turtle.right(90)
        turtle.penup()
        turtle.forward(current_len + 10)
    
strn = input('Введите через запятую размеры сторон квадратов:\n>')
square(strn.split(','))
turtle.done()