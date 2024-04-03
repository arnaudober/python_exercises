from tkinter import *

CONVERSION = 1.609344

root = Tk()
root.title("Mile to Km Converter")
frame = Frame(root, padx=10, pady=10)
frame.grid()

miles = StringVar()

Entry(frame, width=5, textvariable=miles).grid(column=1, row=0)
Label(frame, text="Miles").grid(column=2, row=0)
Label(frame, text="is equal to").grid(column=0, row=1)

km = Label(frame, text=0)
km.grid(column=1, row=1)

Label(frame, text="Km").grid(column=2, row=1)

def calculate():
    converted = float(miles.get()) * CONVERSION
    km['text'] = float("{:.2f}".format(converted))


Button(frame, text="Calculate", command=calculate).grid(column=1, row=2)

root.mainloop()
