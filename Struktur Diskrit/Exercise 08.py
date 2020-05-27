from tkinter import *
root = Tk()
root.geometry("500x300")
canvas = Canvas(root, width=550, height=820)
canvas.pack()
num = int(10)
for i in range(1,num*20,20):
    canvas.create_rectangle(300-i, 50+i, 320, 70+i, fill='white')

