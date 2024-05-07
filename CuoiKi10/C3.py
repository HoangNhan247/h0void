string = input("Nhập 1 xâu kí tự: ") # Nhập xâu kí tự
 
num = 0 # Khai báo biến số và kí tự để đếm
char = 0

for i in string: # Vòng lặp duyệt từng phần tử ( i ) của string ( Xâu kí tự )

    if '0' <= i <= '9': # Xét nếu kí tự i là kí tự kiểu chữ số
        
        num = num + 1 # Nếu thỏa mãn thì biến đếm số tăng 1

    if 'A' <= i <= 'Z' or 'a' <= i <= 'z': # Xét nếu kí tự i là kí tự kiểu chữ cái
        
        char += 1 # Nếu thỏa mãn thì biến đếm chữ tăng 1

print('Trong xâu có tổng ký tự số là: ', num) # In ra màn hình kết quả
print('Trong xâu có tổng ký tự chữ là: ', char)
