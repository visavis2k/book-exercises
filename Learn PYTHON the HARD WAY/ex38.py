# -*- coding: cp949 -*-
# ����Ʈ �ٷ��
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "��� ���� ��Ͽ� 10���� ��� ���� ������ �� �� ���� ���ô�."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "�߰�: ", next_one
    stuff.append(next_one)
    print "���� %d �׸��� �ֽ��ϴ�." % len(stuff)
    
print "�� �� �����! ", stuff

print "�̰ɷ� ���� �� ���ô�."

print stuff[1]
print stuff[-1] # ����! ������
print stuff.pop()
print ' '.join(stuff) # ��? ����!
print '#'.join(stuff[3:5]) # ��û������!

