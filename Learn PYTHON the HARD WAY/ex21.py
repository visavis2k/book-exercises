# -*- coding: cp949 -*-
# ��ȯ�ϴ� �Լ�
def add(a, b):
    print "���� %d + %d" % (a, b)
    return a + b
    
def subtract(a, b):
    print "���� %d - %d" % (a, b)
    return a - b
    
def multiply(a, b):
    print "���� %d * %d" % (a, b)
    return a * b
    
def divide(a, b):
    print "������ %d / %d" % (a, b)
    return a / b


print "�Լ������� ����� ���ô�!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "����: %d, Ű: %d, ������: %d, IQ: %d" % (age, height, weight, iq)


# �߰� ���� ����. �ϴ� �� ������.
print "������ �־��."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "���:", what, "������ ����� �� �ֳ���?"

