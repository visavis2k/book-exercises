# -*- coding: cp949 -*-
# ������ ����, ����
# �� �̸����� ���ڷ��� ����(mapping)�� ����ϴ�
states = {
    '��û�ϵ�': '���',
    '���ϵ�': '���',
    '���󳲵�': '����',
    '��⵵': '���',
    '������': '����'
}

# �⺻���� ���� ���� ������ ����ϴ�.
cities = {
    '����': '����',
    '����': '����',
    '���': '�뱸'
}

# ���� �� ���� �� ���ϴ�
cities['���'] = '����'
cities['���'] = '����'

# ���ø� ����մϴ�
print '-' * 10
print "��⵵����", cities['���']
print "��û�ϵ�����", cities['���']

# ���� ����մϴ�
print '-' * 10
print "�������� ���ڴ�", states['������']
print "���ϵ��� ���ڴ�", states['���ϵ�']

# �� �̸� ������ ���� ������ ���ʷ� �� ���ϴ�
print '-' * 10
print "����������", cities[states['������']]
print "���ϵ��� ���ڴ�", cities[states['���ϵ�']]

# �� �̸� ���ڸ� ��� ����� ���ϴ�
print '-' * 10
for state, abbrev in states.items():
    print "%s�� ���Ӹ��� %s�Դϴ�" % (state, abbrev)
    
# ���� �ִ� ���ø� ��� ����� ���ϴ�
print '-' * 10
for abbrev, city in cities.items():
    print "%s���� %s�ð� �ֽ��ϴ�" % (abbrev, city)
    
# ���� �� ���� �غ��ϴ�
print '-' * 10
for state, abbrev in states.items():
    print "%s�� ���Ӹ��� %s�̰� %s�ð� �ֽ��ϴ�" % (
        state, abbrev, cities[abbrev])
    
print '-' * 10
# ���� ���� �ִ� �� �̸� ���ڸ� �����ϰ� �޾� �ɴϴ�
state = states.get('���ֵ�', None)

if not state:
    print "���ֵ��� �����ϴ�."
    
# ���ø� �⺻���� �ְ� ���� �ɴϴ�
city = cities.get('����', '�����ϴ�')
print "'����'�� �ô� %s" % city

