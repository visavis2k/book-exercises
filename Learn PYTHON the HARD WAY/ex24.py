# -*- coding: cp949 -*-
# �� �����ϱ�
print "��� ���� ������ ���ô�."
print "\\�� �̿��� \n �� ���̳� \t ���� �ϴ� Ż��������� ���� '�˾ƾ߸�' �մϴ�."

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"


five = 10 - 2 + 3 - 6
print "�� ���� �ټ��̾�� �մϴ�: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 1000
    return jelly_beans, jars, crates
    

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "������: %d" % start_point
print "%d��, %d����, %d���ڰ� �ֽ��ϴ�." % (beans, jars, crates)

start_point = start_point / 10

print "�̷��� �� ���� �ֽ��ϴ�."
print "%d��, %d����, %d���ڰ� �ֽ��ϴ�." % secret_formula(start_point)

