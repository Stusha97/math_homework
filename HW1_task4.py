#4 В лотерее 100 билетов. Из них 2 выигрышных.
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

import math
all_tickets = 100
baught_tickets = 2
favorable_outcome = 1
all_outcome = math.factorial(all_tickets)/(math.factorial(baught_tickets)*math.factorial(all_tickets-baught_tickets))
P = favorable_outcome/all_outcome
print(f'Вероятность того, что 2 приобретенных билета окажутся выигрышными равна {P*100 :.2f}%')