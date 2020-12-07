while True:
    print('"M" to see manual. "T" to convert Farenheit to Celcius or Celcius to Farenheit. "Q" to Quit the program.')
    a = input()
    if a == 'M':
        print('Input : [String] [Decimal]. Input "F" or "C" in [String], input number to convert the temperature.')
        print('ex) F 27, C 78')
        print('"F 27" means you want to convert 27 degrees Celcius to Farenheit.')
        print('"C 78" means you want to convert 78 degrees Farenheit to Celcius.')
        print('And now, let\'s convert!')
    elif a == 'T':
        c, d = input().split()
        temp = c
        if temp == 'F':
            b = int(d) * 1.8 + 32
            print(b)
        elif temp == 'C':
            b = (int(d) - 32) * 1.8
            print(b)
    elif a == 'Q':
        break
    else:
        print('Invalid input.')
