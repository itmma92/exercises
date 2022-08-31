"""
Задача - "Счастливый билет"
Напишите функицю is_lucky_ticket, которая принимает на вход число от пользователя и проверяет, счастливый ли билет

*Счастливые билет - это билет, у которого сумма левой части равна правой, например:

123123 - (1+2+3) = (1+2+3) > True
123122 - (1+2+3) != (1+2+2) > False
"""

number_lucky_ticket=(input('Введите номер билета-'))
def is_lucky_ticket(number_lucky_ticket):
    list_lucky_ticket=(list(map(int,number_lucky_ticket)))
    lucky_ticket=bool(sum(list_lucky_ticket[0:int(len(list_lucky_ticket)/2)])==sum(list_lucky_ticket[int(len(list_lucky_ticket) / 2):]))
    return (list_lucky_ticket)
is_lucky_ticket(number_lucky_ticket)
