def triangle(num):

    # 輸出三角形第一行
    print(' '*(num-1)+'*')
    # 輸出三角形中間部分
    for i in range(1,num-1):
        for j in range(num-i-1):
            print(' ', end='')
        print('*', end='')
        for k in range(i*2-1):
            print(' ', end='')
        print('*')

    # 輸出三角形的最後一行
    print('* '*(num-1)+'*')

num = int(input("請輸入一個正整數 num："))
triangle(num)
