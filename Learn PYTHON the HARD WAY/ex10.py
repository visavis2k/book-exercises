# -*- coding: cp949 -*-
# �װ� ������?
tabby_cat = "\t�� ���� ��."
persian_cat = "����\n�и���."
backslash_cat = "���� \\ �� \\ ����."

fat_cat = """
�� �� ���:
\t* ����� ��
\t* �����
\t* ������\n\t* ������
  """

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i,
