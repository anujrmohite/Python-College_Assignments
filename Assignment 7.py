from tkinter import *

ws = Tk()
ws.title("Assignment 6")
ws.geometry("200x200")

Label(ws, text="RED", borderwidth=3, relief="raised", padx=10, pady=20, bg="#EE2C2C").pack(padx=30, pady=40)
Label(ws, text="BLUE", borderwidth=3, relief="raised", padx=5, pady=10, bg="#1C86EE").pack(padx=10, pady=10)

ws.mainloop()

