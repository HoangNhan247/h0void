A = [1, 2, 3, 4, 5, 6] # Danh sách

def Tach_day(xlist): # Khai báo hàm | xlist là tham số
    B = [] # Khai báo danh sách B và C
    C = []

    for i in xlist: # Duyệt từng giá trị (Phần tử) của tham số

        if i % 2 == 0: # Xét giá trị tham số của danh sách

            B.append(i) # Thêm giá trị i vào danh sách B nếu đạt điều kiện

        elif i % 2 != 0: 

            C.append(i)

    print(B) # In ra danh sách B và C
    print(C)

Tach_day(A) # Gọi hàm
