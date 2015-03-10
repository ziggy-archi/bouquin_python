from tkinter import *

def cercle(x, y, r, coul ='black'):
     "tracé d'un cercle de centre (x,y) et de rayon r"
     can.create_oval(x-r, y-r, x+r, y+r, outline=coul)

def figure_1():
    "dessiner une cible"
    can.delete(ALL)
    can.create_line(100, 0, 100, 200, fill ='blue')
    can.create_line(0, 100, 200, 100, fill ='blue')
    rayon = 15
    while rayon < 100:
        cercle(100, 100, rayon)
        rayon += 15

def figure_2():
    "dessiner un visage simplifié"
    can.delete(ALL)
    cc =[[100, 100, 80, 'red'],
         [70, 70, 15, 'blue'],
         [130, 70, 15, 'blue'],
         [70, 70, 5, 'black'],
         [130, 70, 5, 'black'],
         [44, 115, 20, 'red'],
         [156, 115, 20, 'red'],
         [100, 95, 15, 'purple'],
         [100, 145, 30, 'purple']]
    i = 0
    while i < len(cc):
        el = cc[i]
        cercle(el[0], el[1], el[2], el[3])
        i += 1
fen = Tk()
can = Canvas(fen, width =200, height =200, bg ='ivory')
can.pack(side =TOP, padx =5, pady =5)
b1 = Button(fen, text ='dessin 1', command =figure_1)
b1.pack(side =LEFT, padx =3, pady =3)
b2 = Button(fen, text ='dessin 2', command =figure_2)
b2.pack(side =RIGHT, padx =3, pady =3)
fen.mainloop()