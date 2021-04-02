
from tkinter import *



# Driver code
if __name__ == "__main__" :
	root = Tk()
	root.configure(background = 'light gray')
	root.geometry("400x250")
	root.title("Calculate Compound Interest")
	Label(root, text = "Principle Amount(Rs) : ", fg = 'black', bg = 'red').grid(row = 1, column = 0, padx = 10, pady = 10)
	Label(root, text = "Interest Rate(%) : ", fg = 'black', bg = 'red').grid(row = 2, column = 0, padx = 10, pady = 10)
	Label(root, text = "Time(Years) : ",fg = 'black', bg = 'red').grid(row = 3, column = 0, padx = 10, pady = 10)
	Label(root, text = "Compound Interest : ",fg = 'black', bg = 'red').grid(row = 4, column = 0, padx = 10, pady = 10)
	button1 = Button(root, text = "Submit", bg = "red", fg = "black").grid(row = 4, column = 1, pady = 10)
	button2 = Button(root, text = "Clear", bg = "red", fg = "black").grid(row = 6, column = 1, pady = 10)
	root.mainloop()
	
