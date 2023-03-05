# 3.2 В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых. 
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. 
# Какова вероятность того, что 3 мяча белые?

from math import factorial as f

all_outcomes_box1 = f(8)/ (f(2)*f(6))
print(f'Все исходы по мячам из первого ящика {all_outcomes_box1}')

all_outcomes_box2 = f(12)/ (f(4)*f(8))
print(f'Все исходы по мячам из второго ящика {all_outcomes_box2}')

case_1 = round(((f(5)/f(5)*(f(3)/f(2)))/ all_outcomes_box1) * (((f(5)/(f(3)*f(2)))*(f(7)/f(6)))/all_outcomes_box2),3)
print (f'Вариант первый {case_1}')

case_2 = round (((f(5)/f(4)*(f(3)/f(2)))/ all_outcomes_box1) * (((f(5)/(f(2)*f(3)))*(f(7)/(f(2)*f(5))))/all_outcomes_box2),3)
print (f'Вариант второй {case_2}')

case_3 = round (((f(5)/(f(2)*f(3))*(f(3)/f(3)))/ all_outcomes_box1) * (((f(5)/f(4))*(f(7)/(f(3)*f(4))))/all_outcomes_box2),3)
print (f'Вариант третий {case_3}')

P = case_1 + case_2 + case_3
print (f'Вероятность того, что 3 мяча из извлеченных белые равна {P} или {P*100 :.2f}% ')