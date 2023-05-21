# Написать программу, которая проверяет счастливость шестизначного билета.
# 385916

ticket = input('Введите номер билета: ')
firsThird = int(t[0]) + int(t[1]) + int(t[2])
lastThird = int(t[3]) + int(t[4]) + int(t[5])
if firsThird == lastThird:
    print('Yes')
else:
    print('NO')