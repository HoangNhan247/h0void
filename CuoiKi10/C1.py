A = [1, 2, 3, 4, 5, 6] # Danh sách

def Tach_day(xlist): # Khai báo hàm | xlist là tham số
    B = [] # Khai báo danh sách B và C
    C = []

    for i in range(xlist): # Đếm các chỉ số i từ 0 đến tổng số phần tử của danh sách xlist

        if i % 2 == 0: # Xét nếu chỉ số chẵn

            B.append(i) # Thêm giá trị i vào danh sách B nếu đạt điều kiện

        elif i % 2 != 0: # Xét nếu chỉ số lẻ

            C.append(i) # Thêm giá trị i vào danh sách C nếu đạt điều kiện

    print(B) # In ra danh sách B và C
    print(C)

Tach_day(A) # Gọi hàm
