#!/usr/bin/env python3

from tkinter import Tk, Label, Frame
root = Tk()

def key_pressed(event):
  print(event.keysym)

frame = Frame(root, width=300, height=300)
root.bind("<Key>", key_pressed)
root.bind("<Left>", key_pressed)
root.bind("<Right>", key_pressed)
# frame.bind("<Space>", key_pressed)
frame.pack()
frame.focus_set()
root.mainloop()