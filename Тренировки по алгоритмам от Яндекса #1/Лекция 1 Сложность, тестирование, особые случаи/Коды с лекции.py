from math import *

# ______________________________
#          ЗАДАЧА 1
# ______________________________
# Дана строка (в кодировке UTF-8).
# Найти самый часто встречающийся в ней символ.
# Если несколько символов встречаются одинаково часто, то можно вывести любой.

# решения:

#1
s = input()
print(max(map(lambda x: (s.count(x), x), s))[1])

#2
s = input()
ans = ''
anscnt = 0
for i in range(len(s)):
    nowcnt = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            nowcnt += 1
    if nowcnt > anscnt:
        ans = s[i]
        anscnt = nowcnt
print(ans)

#3
s = input()
anscnt = 0
symcnt = {}
for now in s:
    if now not in symcnt:
        symcnt[now] = 0
    symcnt[now] += 1
    if symcnt[now] > anscnt:
        ans = now
        anscnt = symcnt[now]
print(ans)

# _______________________________________
#   ЗАДАЧА "Сумма последовательностей"
# _______________________________________

seq = list(map(int, input().split()))
seqsum = 0
for i in range(len(seq)):
    seqsum += seq[i]
print(seqsum)

# _______________________________________
#   ЗАДАЧА "Максимум последовательности"
# _______________________________________

seq = list(map(int, input().split()))
if len(seq) == 0:
    print('-inf')
else:
    seqmax = seq[0]
    for i in range(1, len(seq)):
        if seq[i] > seqmax:
            seqmax = seq[i]
    print(seqmax)

# _______________________________________
#   Покрытие тестами. Задача
# _______________________________________
# Даны три целых числа: a, b, c.
# Найдите все корни уравнения ax**2 + bx + c = 0 и выведите их в порядке возрастания.

a, b, c = int(input()), int(input()), int(input())
if a == 0:
    if b != 0:
        print(-c / b)
        if b == 0 and c == 0:
            print('Infinite number of solutions')
else:
    d = b ** 2 - 4 * a * c
    if d == 0:
        x1 = -b / (2 * a)
        print(x1)
    elif d > 0:
        x2 = (-b + sqrt(d)) / (2 * a)
        x1 = (-b - sqrt(d)) / (2 * a)
        if x1 < x2:
            print(x1, x2)
        else:
            print(x2, x1)






