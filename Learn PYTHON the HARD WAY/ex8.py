# -*- coding: cp949 -*-
# ����ϰ� �� ����ϱ�
formatter = "%s %s %s %s"

print formatter % (1, 2, 3, 4)
print formatter % ("�ϳ�", "��", "��", "��")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"�� �̰� ����.",
	"���� �� �� �ֽ� �װ�.",
	"������ '�뷡'���� �ʾƿ�.",
	"�׷��ϱ� ���ڿ�."
)

formatter2 = "%r %r %r %r"
print formatter2 % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
