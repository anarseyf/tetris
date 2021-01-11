#!/usr/bin/env python3

from tkinter import Tk, Label
root = Tk()

def key_pressed(event):
  print(event.char)
  print(dir(event))
  w = Label(root, text = "Key Pressed:" + event.char)
  w.place(x = 70, y = 90)

root.bind("<Key>", key_pressed)
root.bind("<Left>", key_pressed)
root.bind("<Right>", key_pressed)
root.bind("<Space>", key_pressed)
root.mainloop()