# coding: Shift_JIS
import random
f = open('greeting.txt')
lines = f.readlines() 
f.close()
def responce():
	print(random.choice(lines), end='')
AIname = 'at'
print("%s>"%"???", end='')
print("����ɂ��́A���̖��O��%s�ł��B"%AIname)
print("%s >"%AIname, end='')

print("���Ȃ��̖��O�������Ă��������B")
print("user>", end='')
username = input()
print("%s >"%AIname, end='')
print("���߂܂��āA%s����"%username)
print("%s >"%username, end='')
talk = input()
while talk != '':
	print("%s >"%AIname, end='')
	#print("%s���ĉ��ł����H"%talk)
	responce()
	print("%s >"%username, end='')
	talk = input()
print("%s >"%AIname, end='')
print("���悤�Ȃ�A%s����"%username)


