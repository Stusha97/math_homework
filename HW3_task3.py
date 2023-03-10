# 3.3 На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень. 
# Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6. 
# Найти вероятность того, что выстрел произведен: a). первым спортсменом б). вторым спортсменом в). третьим спортсменом.

Pb1 = 0.9
Pb2 = 0.8
Pb3 = 0.6
Pa = 1/3 * Pb1 + 1/3 * Pb2 + 1/3*Pb3

# a). первым спортсменом
P1= (1/3*Pb1)/Pa
print (f'Вероятность того, что выстрел произведен первым стрелком равна {P1*100 :.2f} %')

# б). вторым спортсменом
P2= (1/3*Pb2)/Pa
print (f'Вероятность того, что выстрел произведен вторым стрелком равна {P2*100 :.2f} %')

# в). третьим спортсменом.
P3= (1/3*Pb3)/Pa
print (f'Вероятность того, что выстрел произведен третьим стрелком равна {P3*100 :.2f} %')
