hovaten = str(input("Vui lòng nhập họ và tên: ")).split(' ')

print(hovaten)

if len(hovaten) > 2:
    print('Họ nạn nhân là: ', hovaten[0])

    print('Tên đệm là: ', end='')

    for i in range(1, len(hovaten)-1):

        print(hovaten[i], end=' ')

    print('\n Tên là: ', hovaten[len(hovaten)-1])

else:
    print('Họ là: ', hovaten[0])

    print('\n Tên là: ', hovaten[len(hovaten)-1])
