# -*- coding: cp949 -*-
# �̸�, ����, �ڵ�, �Լ�
# argv�� �� ��ũ��Ʈ�� ����� �Լ�
def print_two(*args):
    arg1, arg2 = args
    print "��������1: %r, ��������2: %r" % (arg1, arg2)
    
# ���ƿ�. ��� *args�� �ʿ䰡 �����ϴ�. �׳� �̷��� ����.
def print_two_again(arg1, arg2):
    print "��������1: %r, ��������2: %r" % (arg1, arg2)
    
# �� �Լ��� �������ڸ� �ϳ��� �޽��ϴ�
def print_one(arg1):
    print "��������1: %r" % arg1

# �� �Լ��� �������ڸ� �ϳ��� ���� �ʽ��ϴ�.
def print_none():
    print "�ƹ��͵� ���� ����."
    

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

