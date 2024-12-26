import tkinter as tk
from tkinter import ttk

playerTurn = 0

def main():
  root = tk.Tk()
  root.geometry("250x150")
  root.title("Tic Tac Tkinter")
  frame = ttk.Frame(root, padding=10)
  frame.grid()

  def chkbx(btn):
    global playerTurn

    print(btn)
    btn.config(text="O" if playerTurn == 0 else "X")

    if playerTurn == 0:
      playerTurn = 1
    else:
      playerTurn = 0

  for i in range(3):
    btn = ttk.Button(frame, text="")
    btn.grid(column=0, row=i)
    btn.configure(command=lambda id=btn: chkbx(id))
    for y in range(2):
      inbtn = ttk.Button(frame, text="")
      inbtn.grid(column=y+1, row=i)
      inbtn.configure(command=lambda inid=inbtn: chkbx(inid))

  ttk.Button(frame, command=root.destroy, text="Quit").grid(column=1, row=9, pady=10)
  root.mainloop()

if __name__ == '__main__':
  main()
