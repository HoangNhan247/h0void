string = input("Nhập 1 xâu kí tự: ") # Khai báo xâu kí tự và kí tự cần tìm
kitucantim = input("Nhập 1 kí tự cần tìm: ")

def timkitu(str, char): # Khai báo hàm trong đó | str là tham số chỉ xâu | char là tham số chỉ kí tự
    
    xuathien = 0 # Khai báo biến đếm số lần kí tự xuất hiện

    for i in str: # Duyệt từng kí tự trong xâu

        if i == char: # Xét nếu kí tự trùng với kí tự cần tìm

            xuathien = xuathien + 1 # Nếu thỏa mãn tăng giá trị đếm lên 1

    return xuathien # Trả lại giá trị xuất hiện

print('Trong xâu ký tự đã xuất hiện', timkitu(string, kitucantim) ) # Gọi hàm trong print
