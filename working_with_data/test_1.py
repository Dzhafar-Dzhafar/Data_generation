from itertools import groupby
import random
import csv
# 75 141 вопросы.

# Импортируем нужные библиотеки
# Далее вытаскиваем данные из CSV (5 столбцов, 10 строк) и поэлементово пихаем их в переменные
with open('data.csv') as f:
    reader = csv.reader(f)
    arc = (list(reader))
z1 = (arc[1][0])
s1 = (arc[2][0])
v1 = (arc[3][0])
x1 = (arc[4][0])
o1 = (arc[5][0])
z2 = (arc[1][1])
s2 = (arc[2][1])
v2 = (arc[3][1])
x2 = (arc[4][1])
o2 = (arc[5][1])
z3 = (arc[1][2])
s3 = (arc[2][2])
v3 = (arc[3][2])
x3 = (arc[4][2])
o3 = (arc[5][2])
z4 = (arc[1][3])
s4 = (arc[2][3])
v4 = (arc[3][3])
x4 = (arc[4][3])
o4 = (arc[5][3])
z5 = (arc[1][4])
s5 = (arc[2][4])
v5 = (arc[3][4])
x5 = (arc[4][4])
o5 = (arc[5][4])
m1 = (arc[6][0])
t1 = (arc[7][0])
y1 = (arc[8][0])
q1 = (arc[9][0])
p1 = (arc[10][0])
m2 = (arc[6][1])
t2 = (arc[7][1])
y2 = (arc[8][1])
q2 = (arc[9][1])
p2 = (arc[10][1])
m3 = (arc[6][2])
t3 = (arc[7][2])
y3 = (arc[8][2])
q3 = (arc[9][2])
p3 = (arc[10][2])
m4 = (arc[6][3])
t4 = (arc[7][3])
y4 = (arc[8][3])
q4 = (arc[9][3])
p4 = (arc[10][3])
m5 = (arc[6][4])
t5 = (arc[7][4])
y5 = (arc[8][4])
q5 = (arc[9][4])
p5 = (arc[10][4])
# Создаем переменные с нужным форматом вывода
Z1 = (z1 + ',' + z2 + ',' + z3 + ',' + z4 + ',' + z5 + ',' + '\n')
S1 = (s1 + ',' + s2 + ',' + s3 + ',' + s4 + ',' + s5 + ',' + '\n')
V1 = (v1 + ',' + v2 + ',' + v3 + ',' + v4 + ',' + v5 + ',' + '\n')
X1 = (x1 + ',' + x2 + ',' + x3 + ',' + x4 + ',' + x5 + ',' + '\n')
O1 = (o1 + ',' + o2 + ',' + o3 + ',' + o4 + ',' + o5 + ',' + '\n')
M1 = (m1 + ',' + m2 + ',' + m3 + ',' + m4 + ',' + m5 + ',' + '\n')
T1 = (t1 + ',' + t2 + ',' + t3 + ',' + t4 + ',' + t5 + ',' + '\n')
Y1 = (y1 + ',' + y2 + ',' + y3 + ',' + y4 + ',' + y5 + ',' + '\n')
Q1 = (q1 + ',' + q2 + ',' + q3 + ',' + q4 + ',' + q5 + ',' + '\n')
P1 = (p1 + ',' + p2 + ',' + p3 + ',' + p4 + ',' + p5 + ',' + '\n')
# Запихиваем их в одну переменную и записываем в txt файл
MANASDFE = Z1+S1+V1+X1+O1+M1+T1+Y1+Q1+P1
file_111 = open('111.txt', 'w', encoding="utf8")
file_111.write(MANASDFE)
file_111.close()
#     С этим пока не знаю как бороться   -----------------------------------------------------------------------
# Тут мы вытаскиваем через разграниуитель "," значения и вносим их в переменные
# Разиваем 1-ю строку из файла на 5-ть элементов
a1 = open('111.txt', 'r', encoding="utf8").read().split(',')[0]
a2 = open('111.txt', 'r', encoding="utf8").read().split(',')[1]
a3 = open('111.txt', 'r', encoding="utf8").read().split(',')[2]
a4 = open('111.txt', 'r', encoding="utf8").read().split(',')[3]
a5 = open('111.txt', 'r', encoding="utf8").read().split(',')[4]
# Разиваем 2-ю строку из файла на 5-ть элементов
b1 = open('111.txt', 'r', encoding="utf8").read().split(',')[5]
b2 = open('111.txt', 'r', encoding="utf8").read().split(',')[6]
b3 = open('111.txt', 'r', encoding="utf8").read().split(',')[7]
b4 = open('111.txt', 'r', encoding="utf8").read().split(',')[8]
b5 = open('111.txt', 'r', encoding="utf8").read().split(',')[9]
# Разиваем 3-ю строку из файла на 5-ть элементов
c1 = open('111.txt', 'r', encoding="utf8").read().split(',')[10]
c2 = open('111.txt', 'r', encoding="utf8").read().split(',')[11]
c3 = open('111.txt', 'r', encoding="utf8").read().split(',')[12]
c4 = open('111.txt', 'r', encoding="utf8").read().split(',')[13]
c5 = open('111.txt', 'r', encoding="utf8").read().split(',')[14]
# Разиваем 4-ю строку из файла на 5-ть элементов
d1 = open('111.txt', 'r', encoding="utf8").read().split(',')[15]
d2 = open('111.txt', 'r', encoding="utf8").read().split(',')[16]
d3 = open('111.txt', 'r', encoding="utf8").read().split(',')[17]
d4 = open('111.txt', 'r', encoding="utf8").read().split(',')[18]
d5 = open('111.txt', 'r', encoding="utf8").read().split(',')[19]
# Разиваем 5-ю строку из файла на 5-ть элементов
e1 = open('111.txt', 'r', encoding="utf8").read().split(',')[20]
e2 = open('111.txt', 'r', encoding="utf8").read().split(',')[21]
e3 = open('111.txt', 'r', encoding="utf8").read().split(',')[22]
e4 = open('111.txt', 'r', encoding="utf8").read().split(',')[23]
e5 = open('111.txt', 'r', encoding="utf8").read().split(',')[24]
# Разиваем 6-ю строку из файла на 5-ть элементов
f1 = open('111.txt', 'r', encoding="utf8").read().split(',')[25]
f2 = open('111.txt', 'r', encoding="utf8").read().split(',')[26]
f3 = open('111.txt', 'r', encoding="utf8").read().split(',')[27]
f4 = open('111.txt', 'r', encoding="utf8").read().split(',')[28]
f5 = open('111.txt', 'r', encoding="utf8").read().split(',')[29]
# Разиваем 7-ю строку из файла на 5-ть элементов
g1 = open('111.txt', 'r', encoding="utf8").read().split(',')[30]
g2 = open('111.txt', 'r', encoding="utf8").read().split(',')[31]
g3 = open('111.txt', 'r', encoding="utf8").read().split(',')[32]
g4 = open('111.txt', 'r', encoding="utf8").read().split(',')[33]
g5 = open('111.txt', 'r', encoding="utf8").read().split(',')[34]
# Разиваем 8-ю строку из файла на 5-ть элементов
h1 = open('111.txt', 'r', encoding="utf8").read().split(',')[35]
h2 = open('111.txt', 'r', encoding="utf8").read().split(',')[36]
h3 = open('111.txt', 'r', encoding="utf8").read().split(',')[37]
h4 = open('111.txt', 'r', encoding="utf8").read().split(',')[38]
h5 = open('111.txt', 'r', encoding="utf8").read().split(',')[39]
# Разиваем 9-ю строку из файла на 5-ть элементов
i1 = open('111.txt', 'r', encoding="utf8").read().split(',')[40]
i2 = open('111.txt', 'r', encoding="utf8").read().split(',')[41]
i3 = open('111.txt', 'r', encoding="utf8").read().split(',')[42]
i4 = open('111.txt', 'r', encoding="utf8").read().split(',')[43]
i5 = open('111.txt', 'r', encoding="utf8").read().split(',')[44]
# Разиваем 10-ю строку из файла на 5-ть элементов
j1 = open('111.txt', 'r', encoding="utf8").read().split(',')[45]
j2 = open('111.txt', 'r', encoding="utf8").read().split(',')[46]
j3 = open('111.txt', 'r', encoding="utf8").read().split(',')[47]
j4 = open('111.txt', 'r', encoding="utf8").read().split(',')[48]
j5 = open('111.txt', 'r', encoding="utf8").read().split(',')[49]
# Выполняем перебор элемента 1-ого порядка каждой строки в сочитании с каждой строкой
# Заносим результаты с подпиской элементов в переменные
# Перебор элемента a1
# Тут при выводе данные проходят корректно, но не дальше. Смещение 'Fullname' идет ---------------------------------
gener_1 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_2 = 'Fullname: ' + a1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_3 = 'Fullname: ' + a1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_4 = 'Fullname: ' + a1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_5 = 'Fullname: ' + a1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_6 = 'Fullname: ' + a1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_7 = 'Fullname: ' + a1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_8 = 'Fullname: ' + a1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_9 = 'Fullname: ' + a1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_10 = 'Fullname: ' + a1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента b1
gener_11 = 'Fullname: ' + b1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_12 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_13 = 'Fullname: ' + b1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_14 = 'Fullname: ' + b1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_15 = 'Fullname: ' + b1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_16 = 'Fullname: ' + b1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_17 = 'Fullname: ' + b1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_18 = 'Fullname: ' + b1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_19 = 'Fullname: ' + b1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_20 = 'Fullname: ' + b1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента c1
gener_21 = 'Fullname: ' + c1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_22 = 'Fullname: ' + c1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_23 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_24 = 'Fullname: ' + c1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_25 = 'Fullname: ' + c1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_26 = 'Fullname: ' + c1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_27 = 'Fullname: ' + c1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_28 = 'Fullname: ' + c1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_29 = 'Fullname: ' + c1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_30 = 'Fullname: ' + c1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента d1
gener_31 = 'Fullname: ' + d1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_32 = 'Fullname: ' + d1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_33 = 'Fullname: ' + d1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_34 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_35 = 'Fullname: ' + d1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_36 = 'Fullname: ' + d1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_37 = 'Fullname: ' + d1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_38 = 'Fullname: ' + d1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_39 = 'Fullname: ' + d1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_40 = 'Fullname: ' + d1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента e1
gener_41 = 'Fullname: ' + e1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_42 = 'Fullname: ' + e1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_43 = 'Fullname: ' + e1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_44 = 'Fullname: ' + e1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_45 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_46 = 'Fullname: ' + e1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_47 = 'Fullname: ' + e1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_48 = 'Fullname: ' + e1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_49 = 'Fullname: ' + e1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_50 = 'Fullname: ' + e1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента f1
gener_51 = 'Fullname: ' + f1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_52 = 'Fullname: ' + f1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_53 = 'Fullname: ' + f1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_54 = 'Fullname: ' + f1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_55 = 'Fullname: ' + f1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_56 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_57 = 'Fullname: ' + f1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_58 = 'Fullname: ' + f1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_59 = 'Fullname: ' + f1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_60 = 'Fullname: ' + f1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента g1
gener_61 = 'Fullname: ' + g1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_62 = 'Fullname: ' + g1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_63 = 'Fullname: ' + g1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_64 = 'Fullname: ' + g1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_65 = 'Fullname: ' + g1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_66 = 'Fullname: ' + g1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_67 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_68 = 'Fullname: ' + g1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_69 = 'Fullname: ' + g1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_70 = 'Fullname: ' + g1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента h1
gener_71 = 'Fullname: ' + h1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_72 = 'Fullname: ' + h1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_73 = 'Fullname: ' + h1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_74 = 'Fullname: ' + h1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_75 = 'Fullname: ' + h1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_76 = 'Fullname: ' + h1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_77 = 'Fullname: ' + h1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_78 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_79 = 'Fullname: ' + h1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_80 = 'Fullname: ' + h1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента i1
gener_81 = 'Fullname: ' + i1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_82 = 'Fullname: ' + i1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_83 = 'Fullname: ' + i1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_84 = 'Fullname: ' + i1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_85 = 'Fullname: ' + i1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_86 = 'Fullname: ' + i1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_87 = 'Fullname: ' + i1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_88 = 'Fullname: ' + i1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_89 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_90 = 'Fullname: ' + i1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента j1
gener_91 = 'Fullname: ' + j1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_92 = 'Fullname: ' + j1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_93 = 'Fullname: ' + j1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_94 = 'Fullname: ' + j1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_95 = 'Fullname: ' + j1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_96 = 'Fullname: ' + j1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_97 = 'Fullname: ' + j1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_98 = 'Fullname: ' + j1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_99 = 'Fullname: ' + j1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_100 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Выполняем перебор элемента 2-ого порядка каждой строки в сочитании с каждой строкой
# Заносим результаты с подпиской элементов в переменные
# Перебор элемента a2
gener_101 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_102 = 'Fullname: ' + b1 + ' cities: ' + a2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_103 = 'Fullname: ' + c1 + ' cities: ' + a2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_104 = 'Fullname: ' + d1 + ' cities: ' + a2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_105 = 'Fullname: ' + e1 + ' cities: ' + a2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_106 = 'Fullname: ' + f1 + ' cities: ' + a2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_107 = 'Fullname: ' + g1 + ' cities: ' + a2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_108 = 'Fullname: ' + h1 + ' cities: ' + a2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_109 = 'Fullname: ' + i1 + ' cities: ' + a2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_110 = 'Fullname: ' + j1 + ' cities: ' + a2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента b2
gener_111 = 'Fullname: ' + a1 + ' cities: ' + b2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_112 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_113 = 'Fullname: ' + c1 + ' cities: ' + b2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_114 = 'Fullname: ' + d1 + ' cities: ' + b2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_115 = 'Fullname: ' + e1 + ' cities: ' + b2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_116 = 'Fullname: ' + f1 + ' cities: ' + b2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_117 = 'Fullname: ' + g1 + ' cities: ' + b2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_118 = 'Fullname: ' + h1 + ' cities: ' + b2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_119 = 'Fullname: ' + i1 + ' cities: ' + b2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_120 = 'Fullname: ' + j1 + ' cities: ' + b2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента c2
gener_121 = 'Fullname: ' + a1 + ' cities: ' + c2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_122 = 'Fullname: ' + b1 + ' cities: ' + c2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_123 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_124 = 'Fullname: ' + d1 + ' cities: ' + c2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_125 = 'Fullname: ' + e1 + ' cities: ' + c2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_126 = 'Fullname: ' + f1 + ' cities: ' + c2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_127 = 'Fullname: ' + g1 + ' cities: ' + c2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_128 = 'Fullname: ' + h1 + ' cities: ' + c2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_129 = 'Fullname: ' + i1 + ' cities: ' + c2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_130 = 'Fullname: ' + j1 + ' cities: ' + c2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента d2
gener_131 = 'Fullname: ' + a1 + ' cities: ' + d2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_132 = 'Fullname: ' + b1 + ' cities: ' + d2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_133 = 'Fullname: ' + c1 + ' cities: ' + d2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_134 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_135 = 'Fullname: ' + e1 + ' cities: ' + d2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_136 = 'Fullname: ' + f1 + ' cities: ' + d2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_137 = 'Fullname: ' + g1 + ' cities: ' + d2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_138 = 'Fullname: ' + h1 + ' cities: ' + d2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_139 = 'Fullname: ' + i1 + ' cities: ' + d2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_140 = 'Fullname: ' + j1 + ' cities: ' + d2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента e2
gener_141 = 'Fullname: ' + a1 + ' cities: ' + e2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_142 = 'Fullname: ' + b1 + ' cities: ' + e2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_143 = 'Fullname: ' + c1 + ' cities: ' + e2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_144 = 'Fullname: ' + d1 + ' cities: ' + e2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_145 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_146 = 'Fullname: ' + f1 + ' cities: ' + e2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_147 = 'Fullname: ' + g1 + ' cities: ' + e2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_148 = 'Fullname: ' + h1 + ' cities: ' + e2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_149 = 'Fullname: ' + i1 + ' cities: ' + e2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_150 = 'Fullname: ' + j1 + ' cities: ' + e2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента f2
gener_151 = 'Fullname: ' + a1 + ' cities: ' + f2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_152 = 'Fullname: ' + b1 + ' cities: ' + f2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_153 = 'Fullname: ' + c1 + ' cities: ' + f2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_154 = 'Fullname: ' + d1 + ' cities: ' + f2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_155 = 'Fullname: ' + e1 + ' cities: ' + f2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_156 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_157 = 'Fullname: ' + g1 + ' cities: ' + f2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_158 = 'Fullname: ' + h1 + ' cities: ' + f2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_159 = 'Fullname: ' + i1 + ' cities: ' + f2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_160 = 'Fullname: ' + j1 + ' cities: ' + f2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента g2
gener_161 = 'Fullname: ' + a1 + ' cities: ' + g2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_162 = 'Fullname: ' + b1 + ' cities: ' + g2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_163 = 'Fullname: ' + c1 + ' cities: ' + g2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_164 = 'Fullname: ' + d1 + ' cities: ' + g2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_165 = 'Fullname: ' + e1 + ' cities: ' + g2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_166 = 'Fullname: ' + f1 + ' cities: ' + g2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_167 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_168 = 'Fullname: ' + h1 + ' cities: ' + g2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_169 = 'Fullname: ' + i1 + ' cities: ' + g2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_170 = 'Fullname: ' + j1 + ' cities: ' + g2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента h2
gener_171 = 'Fullname: ' + a1 + ' cities: ' + h2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_172 = 'Fullname: ' + b1 + ' cities: ' + h2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_173 = 'Fullname: ' + c1 + ' cities: ' + h2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_174 = 'Fullname: ' + d1 + ' cities: ' + h2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_175 = 'Fullname: ' + e1 + ' cities: ' + h2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_176 = 'Fullname: ' + f1 + ' cities: ' + h2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_177 = 'Fullname: ' + g1 + ' cities: ' + h2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_178 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_179 = 'Fullname: ' + i1 + ' cities: ' + h2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_180 = 'Fullname: ' + j1 + ' cities: ' + h2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента i2
gener_181 = 'Fullname: ' + a1 + ' cities: ' + i2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_182 = 'Fullname: ' + b1 + ' cities: ' + i2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_183 = 'Fullname: ' + c1 + ' cities: ' + i2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_184 = 'Fullname: ' + d1 + ' cities: ' + i2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_185 = 'Fullname: ' + e1 + ' cities: ' + i2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_186 = 'Fullname: ' + f1 + ' cities: ' + i2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_187 = 'Fullname: ' + g1 + ' cities: ' + i2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_188 = 'Fullname: ' + h1 + ' cities: ' + i2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_189 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_190 = 'Fullname: ' + j1 + ' cities: ' + i2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента j2
gener_191 = 'Fullname: ' + a1 + ' cities: ' + j2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_192 = 'Fullname: ' + b1 + ' cities: ' + j2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_193 = 'Fullname: ' + c1 + ' cities: ' + j2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_194 = 'Fullname: ' + d1 + ' cities: ' + j2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_195 = 'Fullname: ' + e1 + ' cities: ' + j2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_196 = 'Fullname: ' + f1 + ' cities: ' + j2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_197 = 'Fullname: ' + g1 + ' cities: ' + j2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_198 = 'Fullname: ' + h1 + ' cities: ' + j2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_199 = 'Fullname: ' + i1 + ' cities: ' + j2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_200 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Выполняем перебор элемента 3-ого порядка каждой строки в сочитании с каждой строкой
# Заносим результаты с подпиской элементов в переменные
# Перебор элемента a3
gener_201 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_202 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + a3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_203 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + a3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_204 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + a3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_205 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + a3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_206 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + a3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_207 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + a3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_208 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + a3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_209 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + a3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_210 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + a3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента b3
gener_211 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + b3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_212 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_213 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + b3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_214 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + b3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_215 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + b3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_216 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + b3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_217 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + b3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_218 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + b3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_219 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + b3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_220 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + b3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента c3
gener_221 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + c3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_222 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + c3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_223 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_224 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + c3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_225 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + c3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_226 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + c3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_227 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + c3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_228 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + c3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_229 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + c3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_230 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + c3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента d3
gener_231 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + d3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_232 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + d3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_233 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + d3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_234 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_235 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + d3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_236 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + d3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_237 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + d3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_238 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + d3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_239 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + d3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_240 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + d3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента e3
gener_241 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + e3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_242 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + e3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_243 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + e3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_244 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + e3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_245 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_246 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + e3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_247 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + e3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_248 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + e3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_249 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + e3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_250 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + e3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента f3
gener_251 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + f3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_252 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + f3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_253 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + f3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_254 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + f3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_255 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + f3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_256 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_257 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + f3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_258 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + f3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_259 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + f3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_260 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + f3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента g3
gener_261 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + g3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_262 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + g3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_263 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + g3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_264 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + g3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_265 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + g3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_266 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + g3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_267 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_268 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + g3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_269 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + g3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_270 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + g3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента h3
gener_271 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + h3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_272 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + h3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_273 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + h3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_274 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + h3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_275 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + h3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_276 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + h3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_277 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + h3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_278 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_279 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + h3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_280 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + h3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента i3
gener_281 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + i3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_282 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + i3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_283 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + i3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_284 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + i3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_285 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + i3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_286 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + i3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_287 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + i3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_288 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + i3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_289 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_290 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + i3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Перебор элемента j3
gener_291 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + j3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_292 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + j3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_293 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + j3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_294 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + j3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_295 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + j3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_296 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + j3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_297 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + j3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_298 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + j3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_299 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + j3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_300 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Выполняем перебор элемента 4-ого порядка каждой строки в сочитании с каждой строкой
# Заносим результаты с подпиской элементов в переменные
# Перебор элемента a4
gener_301 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_302 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + a4 + ' Mortgage: ' + b5
gener_303 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + a4 + ' Mortgage: ' + c5
gener_304 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + a4 + ' Mortgage: ' + d5
gener_305 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + a4 + ' Mortgage: ' + e5
gener_306 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + a4 + ' Mortgage: ' + f5
gener_307 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + a4 + ' Mortgage: ' + g5
gener_308 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + a4 + ' Mortgage: ' + h5
gener_309 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + a4 + ' Mortgage: ' + i5
gener_310 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + a4 + ' Mortgage: ' + j5
# Перебор элемента b4
gener_311 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + b4 + ' Mortgage: ' + a5
gener_312 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_313 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + b4 + ' Mortgage: ' + c5
gener_314 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + b4 + ' Mortgage: ' + d5
gener_315 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + b4 + ' Mortgage: ' + e5
gener_316 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + b4 + ' Mortgage: ' + f5
gener_317 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + b4 + ' Mortgage: ' + g5
gener_318 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + b4 + ' Mortgage: ' + h5
gener_319 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + b4 + ' Mortgage: ' + i5
gener_320 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + b4 + ' Mortgage: ' + j5
# Перебор элемента c4
gener_321 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + c4 + ' Mortgage: ' + a5
gener_322 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + c4 + ' Mortgage: ' + b5
gener_323 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_324 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + c4 + ' Mortgage: ' + d5
gener_325 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + c4 + ' Mortgage: ' + e5
gener_326 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + c4 + ' Mortgage: ' + f5
gener_327 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + c4 + ' Mortgage: ' + g5
gener_328 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + c4 + ' Mortgage: ' + h5
gener_329 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + c4 + ' Mortgage: ' + i5
gener_330 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + c4 + ' Mortgage: ' + j5
# Перебор элемента d4
gener_331 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + d4 + ' Mortgage: ' + a5
gener_332 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + d4 + ' Mortgage: ' + b5
gener_333 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + d4 + ' Mortgage: ' + c5
gener_334 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_335 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + d4 + ' Mortgage: ' + e5
gener_336 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + d4 + ' Mortgage: ' + f5
gener_337 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + d4 + ' Mortgage: ' + g5
gener_338 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + d4 + ' Mortgage: ' + h5
gener_339 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + d4 + ' Mortgage: ' + i5
gener_340 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + d4 + ' Mortgage: ' + j5
# Перебор элемента e4
gener_341 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + e4 + ' Mortgage: ' + a5
gener_342 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + e4 + ' Mortgage: ' + b5
gener_343 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + e4 + ' Mortgage: ' + c5
gener_344 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + e4 + ' Mortgage: ' + d5
gener_345 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_346 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + e4 + ' Mortgage: ' + f5
gener_347 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + e4 + ' Mortgage: ' + g5
gener_348 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + e4 + ' Mortgage: ' + h5
gener_349 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + e4 + ' Mortgage: ' + i5
gener_350 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + e4 + ' Mortgage: ' + j5
# Перебор элемента f4
gener_351 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + f4 + ' Mortgage: ' + a5
gener_352 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + f4 + ' Mortgage: ' + b5
gener_353 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + f4 + ' Mortgage: ' + c5
gener_354 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + f4 + ' Mortgage: ' + d5
gener_355 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + f4 + ' Mortgage: ' + e5
gener_356 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_357 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + f4 + ' Mortgage: ' + g5
gener_358 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + f4 + ' Mortgage: ' + h5
gener_359 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + f4 + ' Mortgage: ' + i5
gener_360 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + f4 + ' Mortgage: ' + j5
# Перебор элемента g4
gener_361 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + g4 + ' Mortgage: ' + a5
gener_362 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + g4 + ' Mortgage: ' + b5
gener_363 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + g4 + ' Mortgage: ' + c5
gener_364 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + g4 + ' Mortgage: ' + d5
gener_365 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + g4 + ' Mortgage: ' + e5
gener_366 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + g4 + ' Mortgage: ' + f5
gener_367 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_368 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + g4 + ' Mortgage: ' + h5
gener_369 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + g4 + ' Mortgage: ' + i5
gener_370 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + g4 + ' Mortgage: ' + j5
# Перебор элемента h4
gener_371 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + h4 + ' Mortgage: ' + a5
gener_372 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + h4 + ' Mortgage: ' + b5
gener_373 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + h4 + ' Mortgage: ' + c5
gener_374 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + h4 + ' Mortgage: ' + d5
gener_375 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + h4 + ' Mortgage: ' + e5
gener_376 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + h4 + ' Mortgage: ' + f5
gener_377 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + h4 + ' Mortgage: ' + g5
gener_378 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_379 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + h4 + ' Mortgage: ' + i5
gener_380 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + h4 + ' Mortgage: ' + j5
# Перебор элемента i4
gener_381 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + i4 + ' Mortgage: ' + a5
gener_382 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + i4 + ' Mortgage: ' + b5
gener_383 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + i4 + ' Mortgage: ' + c5
gener_384 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + i4 + ' Mortgage: ' + d5
gener_385 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + i4 + ' Mortgage: ' + e5
gener_386 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + i4 + ' Mortgage: ' + f5
gener_387 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + i4 + ' Mortgage: ' + g5
gener_388 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + i4 + ' Mortgage: ' + h5
gener_389 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_390 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + i4 + ' Mortgage: ' + j5
# Перебор элемента j4
gener_391 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + j4 + ' Mortgage: ' + a5
gener_392 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + j4 + ' Mortgage: ' + b5
gener_393 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + j4 + ' Mortgage: ' + c5
gener_394 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + j4 + ' Mortgage: ' + d5
gener_395 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + j4 + ' Mortgage: ' + e5
gener_396 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + j4 + ' Mortgage: ' + f5
gener_397 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + j4 + ' Mortgage: ' + g5
gener_398 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + j4 + ' Mortgage: ' + h5
gener_399 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + j4 + ' Mortgage: ' + i5
gener_400 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
# Выполняем перебор элемента 5-ого порядка каждой строки в сочитании с каждой строкой
# Заносим результаты с подпиской элементов в переменные
# Перебор элемента a5
gener_401 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + a5
gener_402 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + a5
gener_403 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + a5
gener_404 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + a5
gener_405 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + a5
gener_406 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + a5
gener_407 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + a5
gener_408 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + a5
gener_409 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + a5
gener_410 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + a5
# Перебор элемента b5
gener_411 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + b5
gener_412 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + b5
gener_413 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + b5
gener_414 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + b5
gener_415 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + b5
gener_416 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + b5
gener_417 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + b5
gener_418 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + b5
gener_419 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + b5
gener_420 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + b5
# Перебор элемента c5
gener_421 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + c5
gener_422 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + c5
gener_423 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + c5
gener_424 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + c5
gener_425 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + c5
gener_426 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + c5
gener_427 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + c5
gener_428 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + c5
gener_429 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + c5
gener_430 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + c5
# Перебор элемента d5
gener_431 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + d5
gener_432 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + d5
gener_433 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + d5
gener_434 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + d5
gener_435 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + d5
gener_436 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + d5
gener_437 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + d5
gener_438 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + d5
gener_439 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + d5
gener_440 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + d5
# Перебор элемента e5
gener_441 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + e5
gener_442 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + e5
gener_443 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + e5
gener_444 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + e5
gener_445 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + e5
gener_446 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + e5
gener_447 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + e5
gener_448 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + e5
gener_449 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + e5
gener_450 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + e5
# Перебор элемента f5
gener_451 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + f5
gener_452 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + f5
gener_453 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + f5
gener_454 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + f5
gener_455 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + f5
gener_456 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + f5
gener_457 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + f5
gener_458 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + f5
gener_459 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + f5
gener_460 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + f5
# Перебор элемента g5
gener_461 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + g5
gener_462 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + g5
gener_463 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + g5
gener_464 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + g5
gener_465 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + g5
gener_466 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + g5
gener_467 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + g5
gener_468 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + g5
gener_469 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + g5
gener_470 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + g5
# Перебор элемента h5
gener_471 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + h5
gener_472 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + h5
gener_473 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + h5
gener_474 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + h5
gener_475 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + h5
gener_476 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + h5
gener_477 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + h5
gener_478 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + h5
gener_479 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + h5
gener_480 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + h5
# Перебор элемента i5
gener_481 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + i5
gener_482 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + i5
gener_483 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + i5
gener_484 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + i5
gener_485 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + i5
gener_486 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + i5
gener_487 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + i5
gener_488 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + i5
gener_489 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + i5
gener_490 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + i5
# Перебор элемента j5
gener_491 = 'Fullname: ' + a1 + ' cities: ' + a2 + ' Credit-card: ' + a3 + ' Deposit: ' + a4 + ' Mortgage: ' + j5
gener_492 = 'Fullname: ' + b1 + ' cities: ' + b2 + ' Credit-card: ' + b3 + ' Deposit: ' + b4 + ' Mortgage: ' + j5
gener_493 = 'Fullname: ' + c1 + ' cities: ' + c2 + ' Credit-card: ' + c3 + ' Deposit: ' + c4 + ' Mortgage: ' + j5
gener_494 = 'Fullname: ' + d1 + ' cities: ' + d2 + ' Credit-card: ' + d3 + ' Deposit: ' + d4 + ' Mortgage: ' + j5
gener_495 = 'Fullname: ' + e1 + ' cities: ' + e2 + ' Credit-card: ' + e3 + ' Deposit: ' + e4 + ' Mortgage: ' + j5
gener_496 = 'Fullname: ' + f1 + ' cities: ' + f2 + ' Credit-card: ' + f3 + ' Deposit: ' + f4 + ' Mortgage: ' + j5
gener_497 = 'Fullname: ' + g1 + ' cities: ' + g2 + ' Credit-card: ' + g3 + ' Deposit: ' + g4 + ' Mortgage: ' + j5
gener_498 = 'Fullname: ' + h1 + ' cities: ' + h2 + ' Credit-card: ' + h3 + ' Deposit: ' + h4 + ' Mortgage: ' + j5
gener_499 = 'Fullname: ' + i1 + ' cities: ' + i2 + ' Credit-card: ' + i3 + ' Deposit: ' + i4 + ' Mortgage: ' + j5
gener_500 = 'Fullname: ' + j1 + ' cities: ' + j2 + ' Credit-card: ' + j3 + ' Deposit: ' + j4 + ' Mortgage: ' + j5
#Создаем общий список для сортировки и последующего исключения дубликатов
GeneralGener = [gener_1, gener_2, gener_3, gener_4, gener_5, gener_6, gener_7, gener_8, gener_9, gener_10,
                gener_11, gener_12, gener_13, gener_14, gener_15, gener_16, gener_17, gener_18, gener_19, gener_20,
                gener_21, gener_22, gener_23, gener_24, gener_25, gener_26, gener_27, gener_28, gener_29, gener_30,
                gener_31, gener_32, gener_33, gener_34, gener_35, gener_36, gener_37, gener_38, gener_39, gener_40,
                gener_41, gener_42, gener_43, gener_44, gener_45, gener_46, gener_47, gener_48, gener_49, gener_50,
                gener_51, gener_52, gener_53, gener_54, gener_55, gener_56, gener_57, gener_58, gener_59, gener_60,
                gener_61, gener_62, gener_63, gener_64, gener_65, gener_66, gener_67, gener_68, gener_69, gener_70,
                gener_71, gener_72, gener_73, gener_74, gener_75, gener_76, gener_77, gener_78, gener_79, gener_80,
                gener_81, gener_82, gener_83, gener_84, gener_85, gener_86, gener_87, gener_88, gener_89, gener_90,
                gener_91, gener_92, gener_93, gener_94, gener_95, gener_96, gener_97, gener_98, gener_99, gener_100,
                gener_101, gener_102, gener_103, gener_104, gener_105, gener_106, gener_107, gener_108, gener_109, gener_110,
                gener_111, gener_112, gener_113, gener_114, gener_115, gener_116, gener_117, gener_118, gener_119, gener_120,
                gener_121, gener_122, gener_123, gener_124, gener_125, gener_126, gener_127, gener_128, gener_129, gener_130,
                gener_131, gener_132, gener_133, gener_134, gener_135, gener_136, gener_137, gener_138, gener_139, gener_140,
                gener_141, gener_142, gener_143, gener_144, gener_145, gener_146, gener_147, gener_148, gener_149, gener_150,
                gener_151, gener_152, gener_153, gener_154, gener_155, gener_156, gener_157, gener_158, gener_159, gener_160,
                gener_161, gener_162, gener_163, gener_164, gener_165, gener_166, gener_167, gener_168, gener_169, gener_170,
                gener_171, gener_172, gener_173, gener_174, gener_175, gener_176, gener_177, gener_178, gener_179, gener_180,
                gener_181, gener_182, gener_183, gener_184, gener_185, gener_186, gener_187, gener_188, gener_189, gener_190,
                gener_191, gener_192, gener_193, gener_194, gener_195, gener_196, gener_197, gener_198, gener_199, gener_200,
                gener_201, gener_202, gener_203, gener_204, gener_205, gener_206, gener_207, gener_208, gener_209, gener_210,
                gener_211, gener_212, gener_213, gener_214, gener_215, gener_216, gener_217, gener_218, gener_219, gener_220,
                gener_221, gener_222, gener_223, gener_224, gener_225, gener_226, gener_227, gener_228, gener_229, gener_230,
                gener_231, gener_232, gener_233, gener_234, gener_235, gener_236, gener_237, gener_238, gener_239, gener_240,
                gener_241, gener_242, gener_243, gener_244, gener_245, gener_246, gener_247, gener_248, gener_249, gener_250,
                gener_251, gener_252, gener_253, gener_254, gener_255, gener_256, gener_257, gener_258, gener_259, gener_260,
                gener_261, gener_262, gener_263, gener_264, gener_265, gener_266, gener_267, gener_268, gener_269, gener_270,
                gener_271, gener_272, gener_273, gener_274, gener_275, gener_276, gener_277, gener_278, gener_279, gener_280,
                gener_281, gener_282, gener_283, gener_284, gener_285, gener_286, gener_287, gener_288, gener_289, gener_290,
                gener_291, gener_292, gener_293, gener_294, gener_295, gener_296, gener_297, gener_298, gener_299, gener_300,
                gener_301, gener_302, gener_303, gener_304, gener_305, gener_306, gener_307, gener_308, gener_309, gener_310,
                gener_311, gener_312, gener_313, gener_314, gener_315, gener_316, gener_317, gener_318, gener_319, gener_320,
                gener_321, gener_322, gener_323, gener_324, gener_325, gener_326, gener_327, gener_328, gener_329, gener_330,
                gener_331, gener_332, gener_333, gener_334, gener_335, gener_336, gener_337, gener_338, gener_339, gener_340,
                gener_341, gener_342, gener_343, gener_344, gener_345, gener_346, gener_347, gener_348, gener_349, gener_350,
                gener_351, gener_352, gener_353, gener_354, gener_355, gener_356, gener_357, gener_358, gener_359, gener_360,
                gener_361, gener_362, gener_363, gener_364, gener_365, gener_366, gener_367, gener_368, gener_369, gener_370,
                gener_371, gener_372, gener_373, gener_374, gener_375, gener_376, gener_377, gener_378, gener_379, gener_380,
                gener_381, gener_382, gener_383, gener_384, gener_385, gener_386, gener_387, gener_388, gener_389, gener_390,
                gener_391, gener_392, gener_393, gener_394, gener_395, gener_396, gener_397, gener_398, gener_399, gener_400,
                gener_401, gener_402, gener_403, gener_404, gener_405, gener_406, gener_407, gener_408, gener_409, gener_410,
                gener_411, gener_412, gener_413, gener_414, gener_415, gener_416, gener_417, gener_418, gener_419, gener_420,
                gener_421, gener_422, gener_423, gener_424, gener_425, gener_426, gener_427, gener_428, gener_429, gener_430,
                gener_431, gener_432, gener_433, gener_434, gener_435, gener_436, gener_437, gener_438, gener_439, gener_440,
                gener_441, gener_442, gener_443, gener_444, gener_445, gener_446, gener_447, gener_448, gener_449, gener_450,
                gener_451, gener_452, gener_453, gener_454, gener_455, gener_456, gener_457, gener_458, gener_459, gener_460,
                gener_461, gener_462, gener_463, gener_464, gener_465, gener_466, gener_467, gener_468, gener_469, gener_470,
                gener_471, gener_472, gener_473, gener_474, gener_475, gener_476, gener_477, gener_478, gener_479, gener_480,
                gener_481, gener_482, gener_483, gener_484, gener_485, gener_486, gener_487, gener_488, gener_489, gener_490,
                gener_491, gener_492, gener_493, gener_494, gener_495, gener_496, gener_497, gener_498, gener_499, gener_500,
                ]
# Убираем дубликаты
new_general = []
for el, _ in groupby(GeneralGener):
    new_general.append(el)
# Выводим 100 НЕ ПОВТОРЯЕМЫХ(sample) рандомных индекса с отсортированного списка
random_index = random.sample(new_general, 100)
# Индексы переводим из списка в строки и записываем с новой строки каждый набор
mod = '\n'.join(random_index)
# Записываем результат в документ
file_1 = open('111_1.txt', 'w', encoding="utf8")
file_1.write(mod)
file_1.close()
