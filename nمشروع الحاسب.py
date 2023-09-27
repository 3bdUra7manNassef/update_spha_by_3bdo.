from tkinter import *

root = Tk()
root.title('Tasbeeh Counter')
root.geometry('200x100')

count = 0
dark_mode_or_light_mode = 'dark mode'

def button_plus():
    global count
    count += 1
    btn.config(text=str(count))

def btn_re():
    global count
    count = 0
    btn.config(text=str(count))

def btn_dark_mode_or_light_mode():
    global dark_mode_or_light_mode
    if dark_mode_or_light_mode == 'light mode':
        dark_mode_or_light_mode = 'dark mode'
        root.config(background='white')
        btn_dark_mode_light_mode.config(text=dark_mode_or_light_mode)
    else:
        dark_mode_or_light_mode = 'light mode'
        root.config(background='black')
        btn_dark_mode_light_mode.config(text=dark_mode_or_light_mode)

btn_dark_mode_light_mode = Button(root, text=dark_mode_or_light_mode, command=btn_dark_mode_or_light_mode)
btn_dark_mode_light_mode.place(x=80, y=60)

btn = Button(root, text=str(count), command=button_plus)
btn.place(x=50, y=30)

btn_re = Button(root, text="Reset", command=btn_re)
btn_re.place(x=120, y=30)

root.mainloop()
