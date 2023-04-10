# Найдите сумму цифр трехзначного числа
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


number = int(input())
hundreds = number // 100
dozens = (number % 100)//10
units = number % 10
sum = hundreds + dozens + units
print(sum)
