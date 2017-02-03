# coding: Shift_JIS
AIname = 'at'
print("%s>"%"???", end='')
print("こんにちは、私の名前は%sです。"%AIname)
print("%s >"%AIname, end='')
print("あなたの名前を教えてください。")
print("user>", end='')
username = input()
print("%s >"%AIname, end='')
print("初めまして、%sさん"%username)
print("%s >"%username, end='')
talk = input()
while talk != '':
	print("%s >"%AIname, end='')
	print("%sって何ですか？"%talk)
	print("%s >"%username, end='')
	talk = input()
print("%s >"%AIname, end='')
print("さようなら、%sさん"%username)
