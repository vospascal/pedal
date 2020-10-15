from tkinter import Scale, Tk, Frame, Label, Button
from tkinter.ttk import Notebook, Entry


def getValue(value):
    print(value)


window = Tk()
window.title("Scale,Tabs,Table Example")
window.geometry("600x400")

frameTabs = Frame(window)
frameTabs.pack(fill="both")

tablayout = Notebook(frameTabs)

# tab1
tab1 = Frame(tablayout)
tab1.pack(fill="both")
label1 = Label(tab1, text="Item 1 in Horizontal")
label1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
label1 = Label(tab1, text="Item 2 in Horizontal")
label1.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
label1 = Label(tab1, text="Item 3 in Horizontal")
label1.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
tab1.grid_columnconfigure(0, weight=1)
tab1.grid_columnconfigure(1, weight=1)
tab1.grid_columnconfigure(2, weight=1)
tab1.grid_columnconfigure(3, weight=1)
tablayout.add(tab1, text="TAB 1")

# tab2
tab2 = Frame(tablayout)
tab2.pack(fill="both")
tab2labela = Label(tab2, text="tab2a")
tab2labela.grid(row=0, column=0)
tab2labelb = Label(tab2, text="tab2b")
tab2labelb.grid(row=0, column=1)
tablayout.add(tab2, text="TAB 2")



tablayout.pack(fill="both")

window.mainloop()
