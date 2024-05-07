hovaten = input("Nhập họ và tên: ") # Nhập xâu kí tự họ và tên 

tachhovaten = hovaten.split(" ") # Tách các xâu kí tự trong hovaten qua kí tự dấu cách

if len(hovaten) > 2: # Xét nếu tổng phần tử trong hovaten lớn hơn 2
    
    print('Họ là: ', tachhovaten[0]) # In ra giá trị đầu của tachhovanten ( Họ )

    print('Tên đệm là: ', end='') 
    
    for i in range(1, len(tachhovaten)-1): # In ra các phần tử xen kẽ giữa phần tử đầu và cuối của tachhovaten ( Tên đệm )
        print(hovaten[i], end=' ')

    print('\n Tên là: ', hovaten[len(hovaten)-1]) # In ra phần tử cuối của tachhovaten ( Tên )

else:  # Xét nếu tổng phần tử trong hovaten ít hơn 2
    
    print('Họ là: ', hovaten[0]) # In ra giá trị đầu của tachhovanten ( Họ )

    print('\n Tên là: ', hovaten[len(hovaten)-1]) # In ra phần tử cuối của tachhovaten ( Tên )
