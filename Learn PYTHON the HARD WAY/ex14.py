# -*- coding: cp949 -*-
# ������Ʈ�� �ѱ��
from sys import argv

script, user_name = argv
prompt = '> '

print "�ȳ� %s, ���� %s ��ũ��Ʈ��." % (user_name, script)
print "�� ���� ������ �Ұ�."
print "%s, ���� ������?" % user_name
likes = raw_input(prompt)

print "%s, ��� ���?" % user_name
lives = raw_input(prompt)

print "���� ������ ��ǻ�͸� ���� �־�?"
computer = raw_input(prompt)
print """
����, ���� �����ϳĴ� �������� '%s'.
'%s'�� ���. ������� �𸣰�����.
�׸��� '%s' ��ǻ�͸� ������. ����.
""" % (likes, lives, computer)

