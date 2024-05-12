hovaten = input("Nhập họ và tên: ") # Nhập xâu kí tự họ và tên 

tachhovaten = hovaten.split(" ") # Tách các xâu kí tự trong hovaten qua kí tự dấu cách thành danh sách

ho = tachhovaten[0] # Lấy phần tử đầu của danh sách tachhovaten ( Họ )

tendem = [] # Tạo 1 danh sách để chứa tên đệm

ten = tachhovaten[len(tachhovaten)-1] # Lấy phần tử cuối của danh sách tachhovaten ( Tên )

if len(tachhovaten) > 2: # Xét nếu tachhovaten có nhiểu hơn 2 phần tử ( Có cả họ, tên và tên đệm )
    
    for i in range(1, len(tachhovaten)-1): # Lặp từ 1 đến số phần tử gần cuối của danh sách tachhovaten ( Giá trị xen kẽ giữa "họ" và "tên" )
        
        tendem.append(tachhovaten[i]) # Thêm tên đệm vào danh sách tên đệm

print('Họ là:', ho) # In ra họ
print('Tên đệm là:', " ".join(tendem)) # Sử dụng " ".join(tendem) để liên kết các phần tử trong danh sách tên đệm bằng dấu cách và in ra
print('Tên là:', ten) # In ra tên

# Cảm ơn Lý Hà Minh Đức đã cho tui ý tưởng :3
