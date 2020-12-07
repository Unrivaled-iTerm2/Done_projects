while True:
    print('"M" to see manual. "T" to convert mL to cc or cc to mL. "Q" to Quit the program.')
    a = input()
    if a == 'M':
        print('Input : [String] [Decimal]. Input "mL" or "cc" in [String], input number to convert the volume.')
        print('ex) mL 27, cc 78')
        print('"mL 20" means you want to convert 20cc to mL.')
        print('"cc 40" means you want to convert 40mL to cc.')
        print('And now, let\'s convert!')
    elif a == 'T':
        try:
            c, d = input().split()
            volume = c
            if volume == 'cc':
                b = float(d) * 1.000028
                print(b)
            elif volume == 'mL':
                b = float(d) / 1.000028
                print(b)
        except:
            print("Invalid input.")
    elif a == 'Q':
        break
    else:
        print('Invalid input.')
