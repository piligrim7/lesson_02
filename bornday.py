byp = '1799'
bdp = '6 июня'
if input('Какой год рождения А.С. Пушкина? ') == byp:
    if input('А когда у него день рождения? (формат ввода по примеру: "9 сентября"): ') == bdp:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
	print('Неверный год рождения')