# Найдите сумму цифр трехзначного числа.

# n = input("Введите трехзначное число: ")
# n = int(n)
 
# d1 = n % 10
# n = n // 10
# d2 = n % 10
# n = n // 10
 
# print("Сумма цифр числа:", n + d1 + d2)


#Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# s = int(input())
# print((s//6), ((s//6)*4), (s//6))


#Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
#n = input().strip()
#print(['Обычный', 'Счастливый билет'][sum(list(map(int, n[:3])))==sum(list(map(int, n[3:])))])

#Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# print ("Введеите размер 1-й дольку шоколадки:\n")
# n = int(input())
# print ("Введите размер 2-ой дольки:\n")
# m = int(input())
# print ("Введите размер 3-й дольки:\n")
# k = int(input())
# if k < n * m and ((k % n == 0) or (k % m == 0)):
#      print('YES')
# else:
#      print('NO')