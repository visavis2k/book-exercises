# -*- coding: cp949 -*-
#
from sys import argv

script, filename = argv

txt = open(filename)

print "���� %r�� ����:" % filename
print txt.read()

txt.close()

print "���� �̸��� �ٽ� �Է��� �ּ���."
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()

