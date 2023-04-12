# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите ширину шоколадки в дольках: '))
m = int(input('Введите длинну шоколадки в дольках: '))
k = int(input('Введите количество долек которое хотите отломить от шоколадки: '))

if (k % n == 0 and k//n <= m) or (k % m == 0 and k//m <= n):
    print('Возьми свой кусочек')
else:
    print('Разломить шоколадку неудалось, радуйся, ведь скоро лето, и ты будеш самым красивым котиком на пляже')