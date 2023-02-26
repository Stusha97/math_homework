# 3 В ящике имеется 15 деталей, из которых 9 окрашены. 
# Рабочий случайным образом извлекает 3 детали. 
# Какова вероятность того, что все извлеченные детали окрашены?

import math
all_details = 15
details_taken = 3
painted_details = 9
favorable_outcome = math.factorial(painted_details) / (math.factorial(details_taken)*math.factorial(painted_details-details_taken))
all_outcomes = math.factorial(all_details) / (math.factorial(details_taken)*math.factorial(all_details-details_taken))
P= favorable_outcome/all_outcomes
print (f'Вероятность того, что все извлеченные детали окрашены равна {P*100 :.2f}%')
