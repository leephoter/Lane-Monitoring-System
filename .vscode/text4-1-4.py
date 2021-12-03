#  -*- coding: utf-8 -*-

array = raw_input("문자열 입력! : ");
less = []
equal = []
greater = []

if len(array) > 1:
    pivot = array[0]
    for x in array:
        if x < pivot:
            less.append(x)
        if x == pivot:
            equal.append(x)
        if x > pivot:
            greater.append(x)
        # print(less+equal+greater)
    else:
        print(array)