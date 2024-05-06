string = str(input("Nhập 1 xâu kí tự: "))

num = 0
char = 0

for i in string:

    if '0' <= i <= '9':
        num += 1

    if 'A' <= i <= 'Z' or 'a' <= i <= 'z':
        char += 1

print('Trong xâu có tổng ký tự số là: ', num)
print('Trong xâu có tổng ký tự chữ là: ', char)