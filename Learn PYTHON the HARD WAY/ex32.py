# -*- coding: cp949 -*-
# ��ȯ���� ����Ʈ
the_count = [1, 2, 3, 4, 5]
fruits = ["���", "��", "��", "�챸"]
change = [1, "�ʿ�", 2, "���", 3, "�����"]

# ù ��° for���� list�� ���� ���ϴ�.
for number in the_count:
    print "�� ���� %d" % number
    
# ���� ���ƿ�.
for fruit in fruits:
    print "���� ����: %s" % fruit
    
# ���� ���� list�� �� �� �־��.
for i in change:
    print "���� �ܵ� %s" % i
    
# list�� ���� ���� �ִµ�, ���� �� ������ �����սô�.
elements = []

# �׸��� 0���� 5���� ���� range �Լ��� ���.
for i in range(0, 5):
    print "list�� %d ���ڸ� ���մϴ�." % i
    # append�� list�� �˾Ƶ�� �Լ��Դϴ�.
    elements.append(i)
    
# �̰͵� ����� �� �ֽ��ϴ�.
for i in elements:
    print "���Ҵ� %d" % i
    
