#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys
prev_deptno = None
dname = None
enames = []

for key_value in sys.stdin:
    key_value = key_value.strip()
    deptno, table_value = key_value.split("\t")
    table, value = table_value.split(",",maxsplit=1)

    if prev_deptno == deptno:
        if table == 'emp':
            enames.append(value)
        else:
            dname = value

    else:
        if prev_deptno and dname!='Finance' and enames:
            for ename in enames:
                print("%s, %s"%(ename, dname))

        dname = None
        enames = []

        if table == 'emp':
            enames = [value]
        else:
            dname = value
        prev_deptno = deptno

if prev_deptno and dname!='Finance' and enames:
    for ename in enames:
        print("%s, %s"%(ename, dname))
