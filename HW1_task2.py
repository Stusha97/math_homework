#2 На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. 
# Код содержит три цифры, которые нужно нажать одновременно. 
# Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?

numbers = 10
code = 3
combinations = numbers **code
P = (1/combinations)*100
print(f'Вероятность того, что человек, не знающий код, откроет дверь с первой попытки равна {P} %')