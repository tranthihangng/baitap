# baitap
# bai 1
n = int(input('nhap gia tri n: '))
if(n%2==1):
    print('weird')
if(n%2==0 and n<=20):
    print('weird')
if(n%2==0 and n>20):
    print('not weird')
# bai 2
lhs = []
lhsb  = []
diemtb = []

n = int(input('nhap so hs: '))
while(n<1):
    n = int(input('nhap so hs: '))
for i in range(n):
    name = str(input('ten: '))
    math = float(input("diem toan: "))
    lite = float(input("diem van: "))
    engl = float(input("diem anh: "))
    d = [name, math, lite, engl]
    dtb = (d[1]+d[2]+d[3])/3
    diemtb.append(dtb)
    d2 = [name, math, lite, engl, dtb]
    lhs.append(d2)


# a
dtbcopy = diemtb.copy()
dtbcopy.sort()
print('diem tb cao t2 la: ', dtbcopy[1])
lis2 = []
for i in lhs:
    if (i[4] == dtbcopy[1]):
        lis2.append(i[0])

print('ten la: ',sorted(lis2))
# b
for i in lhs:
    if (i[4]>= 8.5):
        sovo = 4
    elif (7<= i[4]< 8.5):
        sovo = 3
    elif (5<= i[4]<7):
        sovo = 2
    else:
        sovo = 0
    i.append(sovo)
    i[4]= 'TB = '+str(dtb)

print(lhs)
