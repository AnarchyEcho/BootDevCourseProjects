from tkinter import *
from tkinter import ttk

def main():
  root = Tk()
  frame = ttk.Frame(root, padding=10)
  frame.grid()
  ttk.Label(frame, text="Tic Tac Toe").grid(column=0, row=0)
  ttk.Button(frame, command=root.destroy, text="Quit").grid(column=0, row=1)
  root.mainloop()

if __name__ == '__main__':
  main()
