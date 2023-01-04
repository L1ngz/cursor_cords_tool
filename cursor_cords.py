import pyautogui as py
from tkinter import *
from pynput import mouse

root = Tk()
root.geometry('300x300')
root.title("Cursor Cordinates Tool")

#update real time cords
def real_time_cord():
        x,y = py.position()
        x_value_lable.config(text=x)
        y_value_lable.config(text=y)
        root.after(1,real_time_cord)

#store x, y cords on click
def on_click(x, y, button, pressed):
   if pressed:
    x,y = py.position()
    x_saved_lable.config(text=x)
    y_saved_lable.config(text=y)
listener = mouse.Listener(
        on_click=on_click
        )
listener.start()
       
x_real_lable = Label(root, text='x', font=('Arial', 20),borderwidth=2, relief="groove",width=5)
y_real_lable = Label(root, text='y', font=('Arial', 20),borderwidth=2, relief="groove",width=5)

x_real_lable.grid(row=0, column=0, padx=5, pady=2)
y_real_lable.grid(row=1, column=0, padx=5, pady=2)

x_value_lable = Label(root, text="0", font=('Arial', 20),borderwidth=2, relief="groove",width=5)
y_value_lable = Label(root, text="0", font=('Arial', 20),borderwidth=2, relief="groove",width=5)

x_value_lable.grid(row=0, column=1, padx=5, pady=2)
y_value_lable.grid(row=1, column=1, padx=5, pady=2)

x_real_saved_lable = Label(root, text='-x-', font=('Arial', 20),borderwidth=2, relief="groove",width=5)
y_real_saved_lable = Label(root, text='-y-', font=('Arial', 20),borderwidth=2, relief="groove",width=5)

x_real_saved_lable.grid(row=2, column=0, padx=5, pady=2)
y_real_saved_lable.grid(row=3, column=0, padx=5, pady=2)


x_saved_lable = Label(root, text="", font=('Arial', 20),borderwidth=2, relief="groove",width=5)
y_saved_lable = Label(root, text="", font=('Arial', 20),borderwidth=2, relief="groove",width=5)

x_saved_lable.grid(row=2, column=1, padx=5, pady=2)
y_saved_lable.grid(row=3, column=1, padx=5, pady=2)


real_time_cord()

root.mainloop()

