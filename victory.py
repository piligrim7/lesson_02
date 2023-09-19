import random as rnd
by = {'Пушкин':'1799', 'Лермонтов':'1814', 'Ломоносов':'1711', 'Циолковский':'1857', 'Путин':'1952'}
# Правильные ответы 'Пушкин'- 1799, 'Лермонтов' - 1814, 'Ломоносов' - 1711, 'Циолковский' - 1857, 'Путин' - 1952
cnt = len(by)
repeat = True
while repeat:
	ar = rnd.sample(range(cnt),cnt)
	correct = 0
	keys = list(by)
	for i in ar:
		g = input('В каком году родился {}? '.format(keys[i]))
		correct += g == by[keys[i]]
	print('Количество правильных ответов:', correct)
	print('Количество ошибок:', cnt - correct)
	print('Процент правильных ответов:', correct/cnt*100)
	print('Процент неправильных ответов:', (1-correct/cnt)*100)
	repeat = input('Начать игру сначала (да/нет?) ') == 'да'
