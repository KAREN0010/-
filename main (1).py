while True:
    print ('Введите первое число ')
    a = float(input ())

    print ('Введите второе число ')
    b = float(input ())

    print ('Выбирите опирацию')
    print ('1 - (a + b)')
    print ('2 - (a ^ b)')
    print ('3 - (a * b)')
    print ('4 - (a : b)')
    d = float(input ())

    if d==1:
        print('а + b =',a+b)

    if d==2:
        print('a ^ b =',a**b)

    if d==3:
        print('a * b =',a*b)

    if d==4:
        print('a : b =',a/b)
        

    print('Выйти ? : 1 - да , 2 - нет ')
    i = float(input ()) 
    
    if  i==1:
        break
       



    

    
