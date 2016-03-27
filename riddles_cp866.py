# -*- coding: cp866 -*-

import sys

if sys.version_info[0] == 2:
    input_function = raw_input
else:
    input_function = input

riddles = {'Все элементы в Python есть - ':'объект','Год выхода Python 2.7':'2010','Есть ли цикл do-while в Python (да/нет)':'нет','К сети какого класса относится IP-адрес вида 192.168.1.1 (a/b/c)':'c','Какому числу в десятичной системе счисления равно данное число в двоичной: 01001001':'73','Перебирающий итератор в Python':'for','Вычислите значение выражения: 17?5·6:3?2+4:2':'7'}

print ('\n\nДавай сыграем с тобой в игру...')

incorrAnswers = 0
totalCorrAnswers = 0
i=0

while i<3:
	corrAnswers = 0
	i+=1
	print ('\n\nПопытка %s/3.\n' % (i)) 
	
	for rid in riddles:
		print ('\n'+rid)
		a = input_function('Введи правильный ответ: ').lower()
		if a == riddles[rid]:
			corrAnswers += 1
		else:
			print ('Неправильно... \n')
			incorrAnswers += 1
			
	totalCorrAnswers += corrAnswers

	if corrAnswers==len(riddles):
		print ('\nТы выиграл!\n\nНеправильных ответов за всю игру: %s' % (incorrAnswers))
		break;
	'''else:
		print ('\n\tТы проиграл!')
	'''	
else:
	print('Попыток больше не осталось.\n\n \
	GAME OVER \
	\n\nПравильных ответов за всю игру: %s \nНеправильных ответов за всю игру: %s ' % (totalCorrAnswers, incorrAnswers))
	
input_function('\n\npress any key to exit')