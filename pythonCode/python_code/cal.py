from tkinter import Tk, Entry, Button, StringVar
class Calculator:
  def __init__(self, root):
    root.title('Calculator')
    root.geometry('357x420')
    root.resizable(False, False)
    root.config(bg='gray')

    self.equation = StringVar()
    self.entry_value = ''

    # UI
    Entry(width=44, bg='#fff', fg='#000', font=('Arial Bold', 28), textvariable= self.equation).place(x=0, y=0, height=50)
    
    Button(width=11, height=4, text='(', relief='flat', bg='white', command=lambda:self.show('(')).place(x=0,y=50)
  def show(self, value):
      self.entry_value += str(value)
      print(self.entry_value)
      self.equation.set(self.entry_value)
  def clear(self):
      pass
  def calculate(self):
      pass
root = Tk()
my_cal = Calculator(root)
root.mainloop()
