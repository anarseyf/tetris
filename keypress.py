#!/usr/bin/env python3

from tkinter import Tk, Label, Frame
from threading import Timer
root = Tk()

obj = {
  'count': 0
}

def tick():
    print("tick:", obj['count'])
    Timer(1.0, tick).start()

def key_pressed(event, obj = obj):
  key = event.keysym
  print(event.keysym)
  if key == "Up":
    obj['count'] += 1
  if key == "Down":
    obj['count'] -= 1

tick()

root.bind("<Key>", key_pressed)
frame = Frame(root, width=0, height=0)
frame.pack()
frame.focus_set()
root.mainloop()
