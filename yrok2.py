#Счёт
#Посмотреть счёт
#Снимать со счёта
#Прибавка к счёту

''''Счёт'''
name_score = 'card MIR'
total_score = 1487
''''Просмотр Счёта'''
def print_my_score(name_score : str, total_score : int) -> str:
    return f'Счёт - {name_score} \nСумма на счету - {total_score}'

''''Списывание со счёта'''
def sub_score(total_score, total_sub):
    total_score = total_score - total_sub
    return total_score


while True:
    q = input()
    if q == 'p':
        print(print_my_score(name_score, total_score))
    elif q == 's':
        print('Напишите сколько хотите вычесть: ')
        sub = int(input())
        total_score = sub_score(total_score, sub)
