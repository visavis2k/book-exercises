# -*- coding: cp949 -*-
# �б�� �Լ�
from sys import exit

def gold_room():
    print "Ȳ������ ���� �� ���Դϴ�. �󸶳� ���������?"
    
    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("�ΰ��̿�, ���� ���� ������ ��켼��.")

    if how_much < 50:
        print "����, ��ɺθ��� �ʴ±���. ����� �̰���ϴ�!"
        exit(0)
    else:
        dead("������� ���� ������!")


def bear_room():
    print "���⿡�� ���� �� ���� �ֽ��ϴ�."
    print "���� ���� �ܶ� ��� �ֽ��ϴ�."
    print "�׶��� ���� �ٸ� �� �� �տ� �ֽ��ϴ�."
    print "��� ���� �����̰ڽ��ϱ�?"
    bear_moved = False
    
    while True:
        next = raw_input("> ")
        
        if next == "�� ����":
            dead("���� ����� �Ĵٺ����� ���� �������� ���͸� �����ϴ�.")
        elif next == "�� ���" and not bear_moved:
            print "���� ������ ���Ѽ����ϴ�. ���� ���� �� �ֽ��ϴ�."
            bear_moved = True
        elif next == "�� ���" and bear_moved:
            dead("���� �Ӹ� ������ ���޾� ����� �ٸ��� �þ�Խ��ϴ�.")
        elif next == "�� ����" and bear_moved:
            gold_room()
        else:
            print "���� ������ �𸣰ڳ׿�."
            
            
def cthulhu_room():
    print "���⿡���� ��Ǹ� ũ���縦 ���ϴ�."
    print "�׺���, �װ���, �ƴ� ������ ���� ����� �Ĵٺ��� ����� ���İ��ϴ�."
    print "����� ���� �޾Ƴ����� �� �Ӹ��� �Ծ�ġ�����?"

    next = raw_input("> ")
    
    if "�޾Ƴ���" in next:
        start()
    elif "�Ա�" in next:
        dead("��, ���� ������!")
    else:
        cthulhu_room()
        
        
def dead(why):
    print why, "�� �߾��!"
    exit(0)
    
def start():
    print "��ο� �濡 �ֽ��ϴ�."
    print "�����ʰ� ���ʿ��� ���� �ֽ��ϴ�."
    print "��� ���� �����?"
    
    next = raw_input("> ")
    
    if next == "����":
        bear_room()
    elif next == "������":
        cthulhu_room()
    else:
        dead("�� �������� �ɵ��⸸ �ϴ� ���� �׾����ϴ�.")

        
start()

