# -*- coding: cp949 -*-

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "�ڵ���", cars, "�밡 �ֽ��ϴ�."
print "�����ڴ�", drivers, "�� ���Դϴ�."
print "������ �� ����", cars_not_driven, "���� ���Դϴ�."
print "������", carpool_capacity, "���� �¿� �� �ֽ��ϴ�."
print "�Բ� Ż �����", passengers, "�� �ֽ��ϴ�."
print "������", average_passengers_per_car, "�� ������ Ÿ�� �մϴ�."
