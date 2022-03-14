from tkinter import *
from tkinter import Canvas, Frame, BOTH
import sys
import os

root = Tk()
root.title("крестики-нолики")
root.geometry("360x450")
canvas = Canvas(root, height = 450, width = 360)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

huita = PhotoImage(width = 1, height = 1)
new_game = Button(root, image = huita, text = "новая игра", background = "#FFFF00", foreground = "#000000", width = 360, height = 90, compound = "c", font = "Arial 24", command = restart_program)
new_game.place(x = 0, y = 0)


button1 = Button(root, image = huita, width = 120, height = 120, compound = "c", bg = "#FFA500", activebackground = "#FFA500")
button1.place(x = 0, y = 90)
button2 = Button(root, image = huita, width = 120, height = 120, compound = "c", bg = "#FFA500", activebackground = "#FFA500")
button2.place(x = 120, y = 90)
button3 = Button(root, image = huita, width = 120, height = 120, compound = "c", bg = "#FFA500", activebackground = "#FFA500")
button3.place(x = 240, y = 90)
button4 = Button(root, image = huita, width = 120, height = 120, compound = "c", bg = "#FFA500", activebackground = "#FFA500")
button4.place(x = 0, y = 210)
button5 = Button(root, image = huita, width = 120, height = 120, compound = "c", bg = "#FFA500", activebackground = "#FFA500")
button5.place(x = 120, y = 210)
button6 = Button(root, image = huita, width = 120, height = 120, compound = "c", bg = "#FFA500", activebackground = "#FFA500")
button6.place(x = 240, y = 210)
button7 = Button(root, image = huita, width = 120, height = 120, compound = "c", bg = "#FFA500", activebackground = "#FFA500")
button7.place(x = 0, y = 330)
button8 = Button(root, image = huita, width = 120, height = 120, compound = "c", bg = "#FFA500", activebackground = "#FFA500")
button8.place(x = 120, y = 330)
button9 = Button(root, image = huita, width = 120, height = 120, compound = "c", bg = "#FFA500", activebackground = "#FFA500")
button9.place(x = 240, y = 330)

text1a = Label(text = "x", foreground = "#000000", background = "#FFA500", font = "Arial 60")
text1b = Label(text = "o", foreground = "#000000", background = "#FFA500", font = "Arial 60")
text2a = Label(text = "x", foreground = "#000000", background = "#FFA500", font = "Arial 60")
text2b = Label(text = "o", foreground = "#000000", background = "#FFA500", font = "Arial 60")
text3a = Label(text = "x", foreground = "#000000", background = "#FFA500", font = "Arial 60")
text3b = Label(text = "o", foreground = "#000000", background = "#FFA500", font = "Arial 60")
text4a = Label(text = "x", foreground = "#000000", background = "#FFA500", font = "Arial 60")
text4b = Label(text = "o", foreground = "#000000", background = "#FFA500", font = "Arial 60")
text5a = Label(text = "x", foreground = "#000000", background = "#FFA500", font = "Arial 60")
text5b = Label(text = "o", foreground = "#000000", background = "#FFA500", font = "Arial 60")
text6a = Label(text = "x", foreground = "#000000", background = "#FFA500", font = "Arial 60")
text6b = Label(text = "o", foreground = "#000000", background = "#FFA500", font = "Arial 60")
text7a = Label(text = "x", foreground = "#000000", background = "#FFA500", font = "Arial 60")
text7b = Label(text = "o", foreground = "#000000", background = "#FFA500", font = "Arial 60")
text8a = Label(text = "x", foreground = "#000000", background = "#FFA500", font = "Arial 60")
text8b = Label(text = "o", foreground = "#000000", background = "#FFA500", font = "Arial 60")
text9a = Label(text = "x", foreground = "#000000", background = "#FFA500", font = "Arial 60")
text9b = Label(text = "o", foreground = "#000000", background = "#FFA500", font = "Arial 60")

flag = True
flag1 = 0
flag2 = 0
flag3 = 0
flag4 = 0
flag5 = 0
flag6 = 0
flag7 = 0
flag8 = 0
flag9 = 0

cnt = 1

def click_1(event):
    global cnt, flag1, flag
    if cnt % 2 == 1:
        if flag == True and flag1 == 0:
            text1a.place(x = 35, y = 100)
            flag1 = 1
            cnt += 1
    else:
        if flag == True and flag1 == 0:
            text1b.place(x = 35, y = 100)
            flag1 = 2
            cnt += 1
    if(flag1 == flag4 == flag7 != 0):
        button1.config(bg = "#FF0000", activebackground = "#FF0000")
        text1a.config(bg = "#FF0000")
        text1b.config(bg = "#FF0000")
        button4.config(bg = "#FF0000", activebackground = "#FF0000")
        text4a.config(bg = "#FF0000")
        text4b.config(bg = "#FF0000")
        button7.config(bg = "#FF0000", activebackground = "#FF0000")
        text7a.config(bg = "#FF0000")
        text7b.config(bg = "#FF0000")
        flag = False
    if(flag1 == flag2 == flag3 != 0):
        button1.config(bg = "#FF0000", activebackground = "#FF0000")
        text1a.config(bg = "#FF0000")
        text1b.config(bg = "#FF0000")
        button2.config(bg = "#FF0000", activebackground = "#FF0000")
        text2a.config(bg = "#FF0000")
        text2b.config(bg = "#FF0000")
        button3.config(bg = "#FF0000", activebackground = "#FF0000")
        text3a.config(bg = "#FF0000")
        text3b.config(bg = "#FF0000")
        flag = False
    if(flag1 == flag5 == flag9 != 0):
        button1.config(bg = "#FF0000", activebackground = "#FF0000")
        text1a.config(bg = "#FF0000")
        text1b.config(bg = "#FF0000")
        button5.config(bg = "#FF0000", activebackground = "#FF0000")
        text5a.config(bg = "#FF0000")
        text5b.config(bg = "#FF0000")
        button9.config(bg = "#FF0000", activebackground = "#FF0000")
        text9a.config(bg = "#FF0000")
        text9b.config(bg = "#FF0000")
        flag = False
button1.bind("<Button-1>", click_1)

def click_2(event):
    global cnt, flag2, flag
    if cnt % 2 == 1:
        if flag == True and flag2 == 0:
            text2a.place(x = 155, y = 100)
            flag2 = 1
            cnt += 1
    else:
        if flag == True and flag2 == 0:
            text2b.place(x = 155, y = 100)
            flag2 = 2
            cnt += 1
    if(flag1 == flag2 == flag3 != 0):
        button1.config(bg = "#FF0000", activebackground = "#FF0000")
        text1a.config(bg = "#FF0000")
        text1b.config(bg = "#FF0000")
        button2.config(bg = "#FF0000", activebackground = "#FF0000")
        text2a.config(bg = "#FF0000")
        text2b.config(bg = "#FF0000")
        button3.config(bg = "#FF0000", activebackground = "#FF0000")
        text3a.config(bg = "#FF0000")
        text3b.config(bg = "#FF0000")
        flag = False
    if(flag2 == flag5 == flag8 != 0):
        button2.config(bg = "#FF0000", activebackground = "#FF0000")
        text2a.config(bg = "#FF0000")
        text2b.config(bg = "#FF0000")
        button5.config(bg = "#FF0000", activebackground = "#FF0000")
        text5a.config(bg = "#FF0000")
        text5b.config(bg = "#FF0000")
        button8.config(bg = "#FF0000", activebackground = "#FF0000")
        text8a.config(bg = "#FF0000")
        text8b.config(bg = "#FF0000")
        flag = False
button2.bind("<Button-1>", click_2)

def click_3(event):
    global cnt, flag3, flag
    if cnt % 2 == 1:
        if flag == True and flag3 == 0:
            text3a.place(x = 275, y = 100)
            flag3 = 1
            cnt += 1
    else:
        if flag == True and flag3 == 0:
            text3b.place(x = 275, y = 100)
            flag3 = 2
            cnt += 1
    if(flag1 == flag2 == flag3 != 0):
        button1.config(bg = "#FF0000", activebackground = "#FF0000")
        text1a.config(bg = "#FF0000")
        text1b.config(bg = "#FF0000")
        button2.config(bg = "#FF0000", activebackground = "#FF0000")
        text2a.config(bg = "#FF0000")
        text2b.config(bg = "#FF0000")
        button3.config(bg = "#FF0000", activebackground = "#FF0000")
        text3a.config(bg = "#FF0000")
        text3b.config(bg = "#FF0000")
        flag = False
    if(flag3 == flag6 == flag9 != 0):
        button3.config(bg = "#FF0000", activebackground = "#FF0000")
        text3a.config(bg = "#FF0000")
        text3b.config(bg = "#FF0000")
        button6.config(bg = "#FF0000", activebackground = "#FF0000")
        text6a.config(bg = "#FF0000")
        text6b.config(bg = "#FF0000")
        button9.config(bg = "#FF0000", activebackground = "#FF0000")
        text9a.config(bg = "#FF0000")
        text9b.config(bg = "#FF0000")
        flag = False
    if(flag3 == flag5 == flag7 != 0):
        button3.config(bg = "#FF0000", activebackground = "#FF0000")
        text3a.config(bg = "#FF0000")
        text3b.config(bg = "#FF0000")
        button5.config(bg = "#FF0000", activebackground = "#FF0000")
        text5a.config(bg = "#FF0000")
        text5b.config(bg = "#FF0000")
        button7.config(bg = "#FF0000", activebackground = "#FF0000")
        text7a.config(bg = "#FF0000")
        text7b.config(bg = "#FF0000")
        flag = False
button3.bind("<Button-1>", click_3)

def click_4(event):
    global cnt, flag4, flag
    if cnt % 2 == 1:
        if flag == True and flag4 == 0:
            text4a.place(x = 35, y = 220)
            flag4 = 1
            cnt += 1
    else:
        if flag == True and flag4 == 0:
            text4b.place(x = 35, y = 220)
            flag4 = 2
            cnt += 1
    if(flag1 == flag4 == flag7 != 0):
        button1.config(bg = "#FF0000", activebackground = "#FF0000")
        text1a.config(bg = "#FF0000")
        text1b.config(bg = "#FF0000")
        button4.config(bg = "#FF0000", activebackground = "#FF0000")
        text4a.config(bg = "#FF0000")
        text4b.config(bg = "#FF0000")
        button7.config(bg = "#FF0000", activebackground = "#FF0000")
        text7a.config(bg = "#FF0000")
        text7b.config(bg = "#FF0000")
        flag = False
    if(flag4 == flag5 == flag6 != 0):
        button4.config(bg = "#FF0000", activebackground = "#FF0000")
        text4a.config(bg = "#FF0000")
        text4b.config(bg = "#FF0000")
        button5.config(bg = "#FF0000", activebackground = "#FF0000")
        text5a.config(bg = "#FF0000")
        text5b.config(bg = "#FF0000")
        button6.config(bg = "#FF0000", activebackground = "#FF0000")
        text6a.config(bg = "#FF0000")
        text6b.config(bg = "#FF0000")
        flag = False
button4.bind("<Button-1>", click_4)

def click_5(event):
    global cnt, flag5, flag
    if cnt % 2 == 1:
        if flag == True and flag5 == 0:
            text5a.place(x = 155, y = 220)
            flag5 = 1
            cnt += 1
    else:
        if flag == True and flag5 == 0:
            text5b.place(x = 155, y = 220)
            flag5 = 2
            cnt += 1
    if(flag1 == flag5 == flag9 != 0):
        button1.config(bg = "#FF0000", activebackground = "#FF0000")
        text1a.config(bg = "#FF0000")
        text1b.config(bg = "#FF0000")
        button5.config(bg = "#FF0000", activebackground = "#FF0000")
        text5a.config(bg = "#FF0000")
        text5b.config(bg = "#FF0000")
        button9.config(bg = "#FF0000", activebackground = "#FF0000")
        text9a.config(bg = "#FF0000")
        text9b.config(bg = "#FF0000")
        flag = False
    if(flag2 == flag5 == flag8 != 0):
        button2.config(bg = "#FF0000", activebackground = "#FF0000")
        text2a.config(bg = "#FF0000")
        text2b.config(bg = "#FF0000")
        button5.config(bg = "#FF0000", activebackground = "#FF0000")
        text5a.config(bg = "#FF0000")
        text5b.config(bg = "#FF0000")
        button8.config(bg = "#FF0000", activebackground = "#FF0000")
        text8a.config(bg = "#FF0000")
        text8b.config(bg = "#FF0000")
        flag = False
    if(flag3 == flag5 == flag7 != 0):
        button3.config(bg = "#FF0000", activebackground = "#FF0000")
        text3a.config(bg = "#FF0000")
        text3b.config(bg = "#FF0000")
        button5.config(bg = "#FF0000", activebackground = "#FF0000")
        text5a.config(bg = "#FF0000")
        text5b.config(bg = "#FF0000")
        button7.config(bg = "#FF0000", activebackground = "#FF0000")
        text7a.config(bg = "#FF0000")
        text7b.config(bg = "#FF0000")
        flag = False
    if(flag4 == flag5 == flag6 != 0):
        button4.config(bg = "#FF0000", activebackground = "#FF0000")
        text4a.config(bg = "#FF0000")
        text4b.config(bg = "#FF0000")
        button5.config(bg = "#FF0000", activebackground = "#FF0000")
        text5a.config(bg = "#FF0000")
        text5b.config(bg = "#FF0000")
        button6.config(bg = "#FF0000", activebackground = "#FF0000")
        text6a.config(bg = "#FF0000")
        text6b.config(bg = "#FF0000")
        flag = False
button5.bind("<Button-1>", click_5)

def click_6(event):
    global cnt, flag6, flag
    if cnt % 2 == 1:
        if flag == True and flag6 == 0:
            text6a.place(x = 275, y = 220)
            flag6 = 1
            cnt += 1
    else:
        if flag == True and flag6 == 0:
            text6b.place(x = 275, y = 220)
            flag6 = 2
            cnt += 1
    if(flag3 == flag6 == flag9 != 0):
        button3.config(bg = "#FF0000", activebackground = "#FF0000")
        text3a.config(bg = "#FF0000")
        text3b.config(bg = "#FF0000")
        button6.config(bg = "#FF0000", activebackground = "#FF0000")
        text6a.config(bg = "#FF0000")
        text6b.config(bg = "#FF0000")
        button9.config(bg = "#FF0000", activebackground = "#FF0000")
        text9a.config(bg = "#FF0000")
        text9b.config(bg = "#FF0000")
        flag = False
    if(flag4 == flag5 == flag6 != 0):
        button4.config(bg = "#FF0000", activebackground = "#FF0000")
        text4a.config(bg = "#FF0000")
        text4b.config(bg = "#FF0000")
        button5.config(bg = "#FF0000", activebackground = "#FF0000")
        text5a.config(bg = "#FF0000")
        text5b.config(bg = "#FF0000")
        button6.config(bg = "#FF0000", activebackground = "#FF0000")
        text6a.config(bg = "#FF0000")
        text6b.config(bg = "#FF0000")
        flag = False
button6.bind("<Button-1>", click_6)

def click_7(event):
    global cnt, flag7, flag
    if cnt % 2 == 1:
        if flag == True and flag7 == 0:
            text7a.place(x = 35, y = 340)
            flag7 = 1
            cnt += 1
    else:
        if flag == True and flag7 == 0:
            text7b.place(x = 35, y = 340)
            flag7 = 2
            cnt += 1
    if(flag1 == flag4 == flag7 != 0):
        button1.config(bg = "#FF0000", activebackground = "#FF0000")
        text1a.config(bg = "#FF0000")
        text1b.config(bg = "#FF0000")
        button4.config(bg = "#FF0000", activebackground = "#FF0000")
        text4a.config(bg = "#FF0000")
        text4b.config(bg = "#FF0000")
        button7.config(bg = "#FF0000", activebackground = "#FF0000")
        text7a.config(bg = "#FF0000")
        text7b.config(bg = "#FF0000")
        flag = False
    if(flag3 == flag5 == flag7 != 0):
        button3.config(bg = "#FF0000", activebackground = "#FF0000")
        text3a.config(bg = "#FF0000")
        text3b.config(bg = "#FF0000")
        button5.config(bg = "#FF0000", activebackground = "#FF0000")
        text5a.config(bg = "#FF0000")
        text5b.config(bg = "#FF0000")
        button7.config(bg = "#FF0000", activebackground = "#FF0000")
        text7a.config(bg = "#FF0000")
        text7b.config(bg = "#FF0000")
        flag = False
    if(flag7 == flag8 == flag9 != 0):
        button7.config(bg = "#FF0000", activebackground = "#FF0000")
        text7a.config(bg = "#FF0000")
        text7b.config(bg = "#FF0000")
        button8.config(bg = "#FF0000", activebackground = "#FF0000")
        text8a.config(bg = "#FF0000")
        text8b.config(bg = "#FF0000")
        button9.config(bg = "#FF0000", activebackground = "#FF0000")
        text9a.config(bg = "#FF0000")
        text9b.config(bg = "#FF0000")
        flag = False
button7.bind("<Button-1>", click_7)

def click_8(event):
    global cnt, flag8, flag
    if cnt % 2 == 1:
        if flag == True and flag8 == 0:
            text8a.place(x = 155, y = 340)
            flag8 = 1
            cnt += 1
    else:
        if flag == True and flag8 == 0:
            text8b.place(x = 155, y = 340)
            flag8 = 2
            cnt += 1
    if(flag2 == flag5 == flag8 != 0):
        button2.config(bg = "#FF0000", activebackground = "#FF0000")
        text2a.config(bg = "#FF0000")
        text2b.config(bg = "#FF0000")
        button5.config(bg = "#FF0000", activebackground = "#FF0000")
        text5a.config(bg = "#FF0000")
        text5b.config(bg = "#FF0000")
        button8.config(bg = "#FF0000", activebackground = "#FF0000")
        text8a.config(bg = "#FF0000")
        text8b.config(bg = "#FF0000")
        flag = False
    if(flag7 == flag8 == flag9 != 0):
        button7.config(bg = "#FF0000", activebackground = "#FF0000")
        text7a.config(bg = "#FF0000")
        text7b.config(bg = "#FF0000")
        button8.config(bg = "#FF0000", activebackground = "#FF0000")
        text8a.config(bg = "#FF0000")
        text8b.config(bg = "#FF0000")
        button9.config(bg = "#FF0000", activebackground = "#FF0000")
        text9a.config(bg = "#FF0000")
        text9b.config(bg = "#FF0000")
        flag = False
button8.bind("<Button-1>", click_8)

def click_9(event):
    global cnt, flag9, flag
    if cnt % 2 == 1:
        if flag == True and flag9 == 0:
            text9a.place(x = 275, y = 340)
            flag9 = 1
            cnt += 1
    else:
        if flag == True and flag9 == 0:
            text9b.place(x = 275, y = 340)
            flag9 = 2
            cnt += 1
    if(flag1 == flag5 == flag9 != 0):
        button1.config(bg = "#FF0000", activebackground = "#FF0000")
        text1a.config(bg = "#FF0000")
        text1b.config(bg = "#FF0000")
        button5.config(bg = "#FF0000", activebackground = "#FF0000")
        text5a.config(bg = "#FF0000")
        text5b.config(bg = "#FF0000")
        button9.config(bg = "#FF0000", activebackground = "#FF0000")
        text9a.config(bg = "#FF0000")
        text9b.config(bg = "#FF0000")
        flag = False
    if(flag3 == flag6 == flag9 != 0):
        button3.config(bg = "#FF0000", activebackground = "#FF0000")
        text3a.config(bg = "#FF0000")
        text3b.config(bg = "#FF0000")
        button6.config(bg = "#FF0000", activebackground = "#FF0000")
        text6a.config(bg = "#FF0000")
        text6b.config(bg = "#FF0000")
        button9.config(bg = "#FF0000", activebackground = "#FF0000")
        text9a.config(bg = "#FF0000")
        text9b.config(bg = "#FF0000")
        flag = False
    if(flag7 == flag8 == flag9 != 0):
        button7.config(bg = "#FF0000", activebackground = "#FF0000")
        text7a.config(bg = "#FF0000")
        text7b.config(bg = "#FF0000")
        button8.config(bg = "#FF0000", activebackground = "#FF0000")
        text8a.config(bg = "#FF0000")
        text8b.config(bg = "#FF0000")
        button9.config(bg = "#FF0000", activebackground = "#FF0000")
        text9a.config(bg = "#FF0000")
        text9b.config(bg = "#FF0000")
        flag = False
button9.bind("<Button-1>", click_9)



window_height = 450
window_width = 360

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
canvas.pack()
root.mainloop()
