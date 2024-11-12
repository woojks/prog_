# задача #A

print("Привет, Яндекс!")

# задача #B

print("Как Вас зовут?")
username = input() 
print(f"Привет, %username%")

# задача #С

info = input()
print(info)
print(info)
print(info)
 
# задача #D
 
nominal = int(input())
cost = 2.5 * 38
change = nominal - cost
print(int(change))

# задача #E

price_per_kg = int(input())
weight = int(input())
money = int(input())
total_cost = price_per_kg * weight
change = money - total_cost
print(change)


# задача #F

product_name = input()
price_per_kg = int(input())
weight = int(input())
money = int(input())
total_cost = price_per_kg * weight
change = money - total_cost
print("Чек")
print(f"{product_name} - {weight}кг - {price_per_kg}руб/кг")
print(f"Итого: {total_cost}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {change}руб")

# задача #G

N = int(input())
for _ in range(N):
    print("Купи слона!")


# задача #H

N = int(input())
punishment = input()
for _ in range(N):
    print(f'Я больше никогда не буду писать "{punishment}"!')


# задача #I

N = int(input())
M = int(input())
kolbasa_pieces = (M * N) // 2
print(kolbasa_pieces)

# задача #J

name = input()
locker_number = input()
group_number = locker_number[0]
bed_number = locker_number[1]
child_number = locker_number[2]
print(f"Группа №{group_number}.")
print(f"{child_number}. {name}.")
print(f"Шкафчик: {locker_number}.")
print(f"Кроватка: {bed_number}.")