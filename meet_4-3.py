x = 10
y = 5

# nested if
if x == 10 :
    if y == 10 :
        print('Hello')
    else :
        print('world')

# jadikan elif (cocok untuk pengecekan lebih dari satu ekspressure)
if x == 10 :
    print('x adalah 10 dan y adalah 10')
elif y == 10 :
    print('x adalah 10 dan y bukan 10')
else :
    print('x bukan 10')

# eif
if x == 10  and y == 10 :
    print('x adalah 10')
elif x == 10 and y != 10 :
    print ('x adalah 10')
else :
    print('x bukan 10')