# 5) На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, равный 190 см,
#  от математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?

from math import sqrt
X=190
M=178
D=25
Z = (X-M)/sqrt(D)
print (f'Количество сигм равно {Z}')