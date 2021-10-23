import tkinter as tk

root = tk.Tk()
root.title("G.C.D, L.C.M Calculator")
root.geometry("320x250")
root.configure(bg = "white")

itext = tk.Label(root, text = "Enter two numbers what you want to get the GCD and LCM.").grid(row = 0, column = 0, columnspan = 4)
n1text = tk.Label(root, text = "1st number").grid(row = 1, column = 0, columnspan = 2)
n2text = tk.Label(root, text = "2nd number").grid(row = 1, column = 2, columnspan = 2)
n1box = tk.Text(root, height = 13, width = 21)
n1box.grid(row = 2, column = 0, columnspan = 2)
n1box.insert(tk.END, 1)
n2box = tk.Text(root, height = 13, width = 21)
n2box.grid(row = 2, column = 2, columnspan = 2)
n2box.insert(tk.END, 1)
resultlabel = tk.Label(root, text = "GCD:- LCM:-")
def end(gcd, lcm):
    resultlabel['text'] = (f"GCD:{gcd} LCM:{lcm}")
def get():
    a = int(n1box.get("1.0", "end-1c"))
    b = int(n2box.get("1.0", "end-1c"))
    gcd = 0
    lcm = 0
    if a < b:
        temp = a
        a = b
        b = temp
    if a == b:
        gcd = a
        lcm = b
        end(gcd, lcm)
    if a == 0 or b == 0:
        if b < 0:
            gcd = abs(b)
        else:
            gcd = abs(a)
        lcm = 0
        end(gcd, lcm)
    w0 = [a]
    w1 = [b]
    w2 = [a % b]

    c = 0

    if a % b == 0:
        gcd = b
        lcm = a
        end(gcd, lcm)

    while True:
        if w0[c] % w1[c] == 0:
            gcd = w1[c]
            lcm = int(a * b / gcd)
            end(gcd, lcm)
            break
        w0.append(w1[c])
        w1.append(w2[c])
        w2.append(w0[c + 1] % w1[c + 1])
        c += 1
        # DEBUG : print(w0, w1, w2)
def exitprogram():
    exit(0)
resultlabel.grid(row = 3, column = 0, columnspan = 2)
cal = tk.Button(root, text = "Calculate!", command = get).grid(row = 3, column = 2)
quit = tk.Button(root, text = "QUIT", command = exitprogram).grid(row = 3, column = 3)
root.mainloop()