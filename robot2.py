from tkinter import *
import random
import time

tk = Tk()
tk.title("Dancing Robot")


can = Canvas(tk, width=500, height = 400, bd = 0, highlightthickness = 0)
rob1 = PhotoImage(file="Python\\rob1.gif")
rob2 = PhotoImage(file="Python\\rob2.gif")
rob3 = PhotoImage(file="Python\\rob3.gif")
rob4 = PhotoImage(file="Python\\rob4.gif")
rob5 = PhotoImage(file="Python\\rob5.gif")
rob6 = PhotoImage(file = "Python\\rob6.gif")
rob7 = PhotoImage(file = "Python\\rob7.gif")
rob8 = PhotoImage(file = "Python\\rob8.gif")
rob9 = PhotoImage(file = "Python\\rob9.gif")
rob10 = PhotoImage(file = "Python\\rob10.gif")
rob11 = PhotoImage(file = "Python\\rob11.gif")
rob12 = PhotoImage(file = "Python\\rob12.gif")
can.pack()
tk.update()


def animateTri(em):

    if em.keysym == 'Up':

        circle2 = can.create_image(50, 50, anchor=NW, image=rob2)
        can.pack()
        can.move(circle2, 0, -3)
        tk.update()

    elif em.keysym == 'Down':
        can.move(circle, 0, 3)
        tk.update()

        #time.sleep(0.005)
    elif em.keysym == "Left":
        can.move(circle, -3, 0)
        tk.update()


        #time.sleep(0.005)

    elif em.keysym == "Return":
        x = random.randrange(10)
        y = 1
        for i in range(x, y):
            can.move(circle, x, y)


            tk.update()
            time.sleep(0.005)
    else:
        can.move(circle, 3, 0)


        tk.update()


can.bind_all('<KeyPress-Right>', animateTri)
can.bind_all('<KeyPress-Left>', animateTri)
can.bind_all('<KeyPress-Up>', animateTri)
can.bind_all('<KeyPress-Down>', animateTri)
can.bind_all('<KeyPress-Return>', animateTri)

while True:
    can.pack_forget()
    can = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
    can.pack()
    starts = [rob1, rob2, rob3, rob4, rob5, rob6, rob7, rob8, rob9, rob10, rob11, rob12]
    random.shuffle(starts)

    circle = can.create_image(50, 50, anchor=NW, image=starts[0])
    can.move(circle, -3, 0)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.2)




