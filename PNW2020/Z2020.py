#COMPLETE: took way too long. Also split up work
num = 100
input = "1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768697071727374757677787980818384858687888990919293949596979899100"

for i in range(1, num + 1):
    string = str(i)
    
    
    if i < 10:
        test = str(input[i - 1])
    elif i < 100 : #input : 9th, 11th i = 9, 11 2n - 
        test = str(input[2 * (i - 1) - 9: 2 * (i - 1) - 7])
    else:
        test = "100"

    #print(test)

    if string != test:
        print(i)
        break
        
