# 1 Из колоды в 52 карты извлекаются случайным образом 4 карты.
#  a) Найти вероятность того, что все карты – крести. 
#  б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

import math

all_cards = 52
cards_taken = 4
cross_cards = 13

favorable_outcome1 = math.factorial(cross_cards) / (math.factorial(cards_taken)* math.factorial(cross_cards - cards_taken))
all_outcomes = math.factorial(all_cards)/ (math.factorial(cards_taken)* math.factorial(all_cards-cards_taken))
result1 = favorable_outcome1/all_outcomes
print (f'Вероятность того, что все извлекаемые карты - крести = {result1*100 :.2f} %')

C1 = (math.factorial (cards_taken) / (math.factorial(1)* math.factorial(cards_taken-1)))*(math.factorial(all_cards-cards_taken)/(math.factorial(cards_taken-1)*math.factorial(all_cards-cards_taken-3)))
C2 = (math.factorial (cards_taken) / (math.factorial(2)* math.factorial(cards_taken-2)))*(math.factorial(all_cards-cards_taken)/(math.factorial(cards_taken-2)*math.factorial(all_cards-cards_taken-2)))
C3 = (math.factorial (cards_taken) / (math.factorial(3)* math.factorial(cards_taken-3)))*(math.factorial(all_cards-cards_taken)/(math.factorial(cards_taken-3)*math.factorial(all_cards-cards_taken-1)))
C4 = (math.factorial (cards_taken) / (math.factorial(4)* math.factorial(cards_taken-4)))*(math.factorial(all_cards-cards_taken)/(math.factorial(cards_taken-4)*math.factorial(all_cards-cards_taken)))
favorable_outcome2 = C1+C2+C3+C4
result2= favorable_outcome2/all_outcomes
print(f'Вероятность, что среди 4-х карт окажется хотя бы один туз = {result2*100 :.2f} %')
