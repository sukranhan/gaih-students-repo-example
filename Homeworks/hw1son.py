matrix=[[],[],[]]
for x in range (9):
    num=int(input('please enter a prime number: '))
    a=True
    while a==True:
        if num==2 :
            break
        for i in range(2,num):
            if num%i==0:
                a=True
                break 
            else:
                a=False
        if a==True:
            num=int(input('this number is not a prime, please enter a prime number: '))
    if len(matrix[0])<3:
        matrix[0].append(num)
    elif len(matrix[1])<3:
        matrix[1].append(num)
    else:
        matrix[2].append(num)
for y in range(3):
    print(matrix[y])
