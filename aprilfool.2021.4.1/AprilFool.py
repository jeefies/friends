import time
from random import randint
import tkinter as tk
import tkinter.font as tkf
from tkinter import messagebox as msg
from multiprocessing import Process
from collections import deque
#from threading import Thread

root = tk.Tk()
root.withdraw()

ans = msg.askyesno('Warning', 'Your computer is attack by this virus!\n' \
        '为了保证此病毒会带个您更好的体验，\n' \
        '我们将会争取您的意见，是否继续')

if not ans: # no
    msg.showwarning('Bad Answer', 'You made a bad choice!\n您的电脑将会被慢慢侵蚀！')
else:
    msg.showinfo('Nice Answer', '您的电脑将会被温柔的入侵！')

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
frame.pack(fill='both', expand='yes')

font = tkf.nametofont('TkDefaultFont').copy()
font['size'] = height // 2
label = tk.Label(frame, text='5', font=font, bg='black', fg='white')
label.pack(expand='yes', anchor='center')

top.update()

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
def makemany():
    start = time.time()
    tops = deque()
    while time.time() - start < 5:
        top = tk.Toplevel()
        top.overrideredirect(True)
        tops.append(top)
        top.geometry('100x50+%d+%d' % (randint(0, w - 100), randint(0, h - 50)))
        top.update()
        time.sleep(0.2)
    for top in tops:
        top.destroy()

#Process(target=makemany).start()
for i in range(4):
    width += aw + 1
    height += ah + 1
    time.sleep(1)
    top.geometry(f"%dx%d+{rw - width // 2}+{rh - height//2}" % (width, height))
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
time.sleep(1)

for i in range(2):
    for j in range(4):
        label['text'] = '电脑崩溃中' + '.' * j
        top.update()
        time.sleep(0.5)

label['bg'] = 'blue'
frame['bg'] = 'blue'
label['fg'] = 'white'
font['size'] = 14

label['text'] = '检测到您电脑异常，未能找到异常原因     '
top.update()
time.sleep(5)

label['text'] = '愚人节，祝您开心！\nJeefy@github.com'
top.update()

time.sleep(4)
top.destroy()
