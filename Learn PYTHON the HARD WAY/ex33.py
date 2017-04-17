# -*- coding: cp949 -*-
# while문
i = 0
numbers = []

while i < 6:
    print ""
    numbers.append(i)
    
    i = i + 1
    print "숫자는 이제: ", numbers
    print "바닥에서 i는 %d" % i
    
    
print "숫자: "

for num in numbers:
    print num
