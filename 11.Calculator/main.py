import tkinter

tk = tkinter.Tk()
tk.title("Calculator")

result = tkinter.Label(tk, text="Result =")
result.grid(row=0, column=0)

def one():
    return 0; 

btn1 = tkinter.Button(tk, text="1", command = one())
btn1.grid(row=1, column=0)

btn2 = tkinter.Button(tk, text="2", command = one())
btn2.grid(row=1, column=1)

btn3 = tkinter.Button(tk, text="3", command = one())
btn3.grid(row=1, column=2)

btnDiv = tkinter.Button(tk, text="/", command = one())
btnDiv.grid(row=1, column=3)

tk.mainloop()
