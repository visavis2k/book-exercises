# -*- coding: cp949 -*-
# ���� �� �ٷ� ����
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "%s���� %s�� �����մϴ�" % (from_file, to_file)

# �� �� ���� �� �ٷε� �� �� �ֽ��ϴ�. ��� �ұ��? => indata = open(from_file).read()
in_file = open(from_file)
indata = in_file.read()

print "�Է� ������ %d����Ʈ�Դϴ�" % len(indata)

print "��� ������ �����ϳ���? %r" % exists(to_file)
print "�غ�Ǿ����ϴ�. ����Ϸ��� ���� Ű��, ����Ϸ��� CTRL-C�� ��������."
raw_input()

out_file = open(to_file, "w")
out_file.write(indata)

print "�����ϴ�. ��� �Ϸ�Ǿ����ϴ�."

out_file.close()
in_file.close()

