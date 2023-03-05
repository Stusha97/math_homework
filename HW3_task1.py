# 3.1 Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean)
# среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.


from math import sqrt
list = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
average = sum(list) / len(list)
print (f'Среднее арифметическое равно {average}')

list_2 =[]
for i in range (len(list)):
    list_2.append(round((list[i]-average)**2,3)) 
print(list_2)
dispersion_shifted = sum(list_2)/len(list)
dispersion_notshifted = sum(list_2)/(len(list)-1)
print(f'Смещенная дисперсия равна {round(dispersion_shifted,2)}')
print(f'Несмещенаая дисперсия равна {round(dispersion_notshifted,2)}')

standard_deviation_1 = sqrt(dispersion_shifted)
standard_deviation_2 = sqrt(dispersion_notshifted)
print(f'Среднее квадратичное отклонение для смещенной дисперсии равно {round(standard_deviation_1,2)}')
print(f'Среднее квадратичное отклонение для несмещенной дисперсии равно {round(standard_deviation_2,2)}')