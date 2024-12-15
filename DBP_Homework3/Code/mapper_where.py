#!/usr/bin/env python
# coding: utf-8

import sys

for line in sys.stdin:
    line = line.strip()
    tuple_list = line.split(",")

    if len(tuple_list) == 11:
        ename = tuple_list[1] + ' ' + tuple_list[2]
        salary = tuple_list[-4]
        deptno = tuple_list[-1]
	if float(salary) >= 5000:
	        value = ','.join(['emp', ename, salary])
        	print('{0}\t{1}'.format(deptno, value))
    else:
        dname = tuple_list[1]
        deptno = tuple_list[0]
        value = ','.join(['dept', dname])
        print('{0}\t{1}'.format(deptno, value))
