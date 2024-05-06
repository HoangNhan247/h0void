string = str(input('Nhập 1 xâu ký tự: '))
kytucantim = str(input('Nhập ký tự cần tìm trong xâu: '))

def appearence(str, char):
    appear = 0

    for i in str:

        if i == char:

            appear += 1

    return appear

print('Trong xâu ký tự đã xuất hiện', appearence(string, kytucantim) , "lần")