xaukitu = input("Nhập 1 xâu kí tự: ") # Nhập xâu kí tự
 
tongso = 0 # Khai báo biến để đếm số
tongkitu = 0 # Khai báo biến đếm kí tự

for i in xaukitu: # Vòng lặp duyệt từng phần tử ( i ) của string ( Xâu kí tự )

    if '0' <= i <= '9': # Xét nếu kí tự i là kí tự kiểu chữ số
        
        tongso = tongso + 1 # Nếu thỏa mãn thì biến đếm số tăng 1

    if 'A' <= i <= 'Z' or 'a' <= i <= 'z': # Xét nếu kí tự i là kí tự kiểu chữ cái
        
        tongkitu = tongkitu + 1 # Nếu thỏa mãn thì biến đếm chữ tăng 1

print('Trong xâu có tổng ký tự số là: ', tongso) # In ra màn hình kết quả
print('Trong xâu có tổng ký tự chữ là: ', tongkitu)
