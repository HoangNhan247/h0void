A = [1, 2, 3, 4, 5, 6]

def Tach_day(xlist):
    B = [] # Khai báo danh sách B, C
    C = []

    for i in xlist:

        if i % 2 == 0:

            B.append(i)

        elif i % 2 != 0:

            C.append(i)

    print(B)
    print(C)

Tach_day(A)