xaukitu = input("Nhập 1 xâu kí tự: ") # Khai báo xâu kí tự và kí tự cần tìm
kitucantim = input("Nhập 1 kí tự cần tìm: ")

def timkitu(xau, kitu): # Khai báo hàm trong đó | xau là tham số chỉ xâu | kitu là tham số chỉ kí tự
    
    xuathien = 0 # Khai báo biến đếm số lần kí tự xuất hiện

    for i in xau: # Duyệt từng kí tự trong tham số "xau"

        if i == kitu: # Xét nếu kí tự trùng với tham số "kitu" ( kí tự cần tìm )

            xuathien = xuathien + 1 # Nếu thỏa mãn tăng giá trị đếm lên 1

    return xuathien # Trả lại giá trị xuất hiện

print('Trong xâu ký tự đã xuất hiện', timkitu(xaukitu, kitucantim) ) # Gọi hàm trong print

# Nếu đề bài ra kí tự cần tìm có hơn 1 kí tự thì hết cứu :))
