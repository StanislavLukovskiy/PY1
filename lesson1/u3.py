# Написать программу, которая проверяет счастливость шестизначного билета.
# 385916

ticket = input('Введите номер билета: ')
firsThird = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
lastThird = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
if firsThird == lastThird:
    print('Yes')
else:
    print('NO')