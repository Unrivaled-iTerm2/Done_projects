while True:
    try:
        a, b, c = input().split()
        if b == "+":
            print(int(a) + int(c))
        elif b == "-":
            print(int(a) - int(c))
        elif b == "*":
            print(int(a) * int(c))
        elif b == "/":
            try:
                print(int(a) / int(c))
            except ZeroDivisionError:
                print("Cannot divided by zero.")
        elif b == "//":
            try:
                print(int(a) // int(c))
            except ZeroDivisionError:
                print("Cannot divided by zero.")
        elif b == "%":
            try:
                print(int(a) % int(c))
            except ZeroDivisionError:
                print("Cannot divided by zero.")
        elif b == "^":
            a = int(a)
            c = int(c)
            i = 1
            while i < c:
                a *= a
                i += 1
            if c == 0:
                print(1)
            else:
                print(a)
        else:
            print("Invalid input.")
    except:
        print("Invalid input.")
