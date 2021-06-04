from tkinter import *

FONT = ("Arial", 14, "bold")

def calculate():
  miles = float(miles_entry.get())
  result = miles * 1.609
  result_label.config(text=f"{result}")

# Create the window
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=250, height=100)
window.config(padx=5, pady=5)

# Labels
miles_label = Label(text="Miles:", font=FONT)
miles_label.grid(column=0, row=0)

km_label = Label(text="Km:", font=FONT)
km_label.grid(column=0, row=1)

result_label = Label(text="0", font=FONT)
result_label.grid(column=1, row=1)

# Entries
miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)

# Button
button = Button(text="calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()