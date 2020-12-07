while True:
    print('"M" to see manual. "T" to convert Kilometer to Mile or Mile to Kilometer. "Q" to Quit the program.')
    a = input()
    if a == 'M':
        print('Input : [String] [Decimal]. Input "km" or "Mile" in [String], input number to convert the distance.')
        print('ex) F 27, C 78')
        print('"Mile 27" means you want to convert 27 mile to km.')
        print('"km 78" means you want to convert 78 km to Mile.')
        print('And now, let\'s convert!')
    elif a == 'T':
        c, d = input().split()
        temp = c
        if temp == 'km':
            b = int(d) / 0.621371
            print(b)
        elif temp == 'Mile':
            b = int(d) * 0.621371
            print(b)
    elif a == 'Q':
        break
    else:
        print('Invalid input.')
