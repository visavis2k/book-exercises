# -*- coding: cp949 -*-
# ���� �а� ����
from sys import argv

script, filename = argv

print "%r ������ ����� �մϴ�." % filename
print "����Ϸ��� CTRL-C(^C)�� ��������."
print "�����Ϸ��� ������ ��������."

raw_input("? ")

print "������ ���� ��..."
target = open(filename, "w")

print "���� ������ ����ϴ�. �ȳ���!"
# ���� ���('w')�� ������ �� ��쿡�� �ڵ����� truncate�Ǳ� ������ ��� �ʿ� ����...
target.truncate()

print "���� �� �ٿ� �� ������ ���ڽ��ϴ�."

line1 = raw_input("1��: ")
line2 = raw_input("2��: ")
line3 = raw_input("3��: ")

print "�� ������ ���Ͽ� ���ϴ�."

target.write("%s%s%s%s%s%s" % (line1, "\n", line2, "\n", line3, "\n"))
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "���������� �ݽ��ϴ�."
target.close()

# �������� �������� �� �ٹٲ� ���ڰ� ���� ����(\r\n)���� ���� ������ ����

