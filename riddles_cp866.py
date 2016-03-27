# -*- coding: cp866 -*-

import sys

if sys.version_info[0] == 2:
    input_function = raw_input
else:
    input_function = input

riddles = {'�� ������ � Python ���� - ':'��ꥪ�','��� ��室� Python 2.7':'2010','���� �� 横� do-while � Python (��/���)':'���','� �� ������ ����� �⭮���� IP-���� ���� 192.168.1.1 (a/b/c)':'c','������ ��� � �����筮� ��⥬� ��᫥��� ࠢ�� ������ �᫮ � ����筮�: 01001001':'73','��ॡ���騩 ����� � Python':'for','���᫨� ���祭�� ��ࠦ����: 17?5�6:3?2+4:2':'7'}

print ('\n\n����� ��ࠥ� � ⮡�� � ����...')

incorrAnswers = 0
totalCorrAnswers = 0
i=0

while i<3:
	corrAnswers = 0
	i+=1
	print ('\n\n����⪠ %s/3.\n' % (i)) 
	
	for rid in riddles:
		print ('\n'+rid)
		a = input_function('����� �ࠢ���� �⢥�: ').lower()
		if a == riddles[rid]:
			corrAnswers += 1
		else:
			print ('���ࠢ��쭮... \n')
			incorrAnswers += 1
			
	totalCorrAnswers += corrAnswers

	if corrAnswers==len(riddles):
		print ('\n�� �먣ࠫ!\n\n���ࠢ����� �⢥⮢ �� ��� ����: %s' % (incorrAnswers))
		break;
	'''else:
		print ('\n\t�� �ந�ࠫ!')
	'''	
else:
	print('����⮪ ����� �� ��⠫���.\n\n \
	GAME OVER \
	\n\n�ࠢ����� �⢥⮢ �� ��� ����: %s \n���ࠢ����� �⢥⮢ �� ��� ����: %s ' % (totalCorrAnswers, incorrAnswers))
	
input_function('\n\npress any key to exit')