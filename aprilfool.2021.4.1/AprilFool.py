import time
from random import randint
import tkinter as tk
import tkinter.font as tkf
from tkinter import messagebox as msg

root = tk.Tk()
root.withdraw()

font = tkf.nametofont('TkDefaultFont').copy()

ans = msg.askyesno('Warning', 'Your computer is attack by this virus!\n' \
        '为了保证此病毒会带给您更好的体验，\n' \
        '我们将会争取您的意见，是否继续')

if not ans: # no
    title, message, bit = 'Bad Answer', 'You made a bad choice!\n3秒后您的电脑将会被慢慢侵蚀！', 'warning'
else:
    title, message, bit = 'Nice Answer', '3秒后您的电脑将会被温柔的入侵！', 'warning'

winsize = root.winfo_screenwidth() // 2 - 125, root.winfo_screenheight() // 2 - 25
msgtop = tk.Toplevel()
msgtop.title(title)
msgtop.geometry('250x50+%d+%d' % winsize)
bit = tk.BitmapImage(bit)
tk.Label(msgtop, bitmap=bit).pack(side='left', fill='y', anchor='center', padx=10)
tk.Label(msgtop, {tk.Pack: dict(anchor='center', expand='yes'), 'text': message})
msgtop.update()
msgtop.resizable(0,0)
time.sleep(3)
msgtop.destroy()

root.update()
top = tk.Toplevel()

top.overrideredirect(True)

winsize = root.winfo_screenheight() + 50, root.winfo_screenwidth() + 50
rh, rw = tuple(map(lambda x: x // 2, winsize))
ah, aw = cells = tuple(map(lambda x: x // 5, winsize))

height, width = cells
top.geometry(f"%dx%d+{rw - width // 2}+{rh - width//2}" % (width, height))
top.update()

frame = tk.Frame(top, bg='black')
frame.pack(fill='both', expand='yes', padx=1, pady=1)

font['size'] = height // 2
label = tk.Label(frame, text='5', font=font, bg='black', fg='white', justify='left')
label.pack(expand='yes', anchor='center')

top.update()

w, h = root.winfo_screenwidth(), root.winfo_screenheight()

for i in range(4):
    width += aw + 1
    height += ah + 1
    time.sleep(1)
    top.geometry(f"%dx%d+{rw - width // 2 - 1}+{rh - height//2 - 1}" % (width, height))
    top.update()
    label['text'] = str(4 - i)
    label.update()

time.sleep(1)

label['text'] = 'Black screen!'
label['fg'] = 'red'
top.update()
time.sleep(1)

label['text'] = '病毒成功入侵！'
top.update()
time.sleep(1.5)

for i in range(randint(2, 5)):
    for j in range(randint(2, 5)):
        label['text'] = '电脑崩溃中' + '.' * j
        top.update()
        time.sleep(randint(5, 10) / 10)

label['bg'] = 'blue'
frame['bg'] = 'blue'
label['fg'] = 'white'
font['size'] = h // 15

label['text'] = '检测到您电脑异常，\n未能找到异常原因\u3000'
top.update()
time.sleep(5.5)

label['justify'] = 'right'
label['text'] = '愚人节，祝您开心！ '\
        '\nJeefy@github.com'
top.update()

time.sleep(5)
top.destroy()
