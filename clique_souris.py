from tkinter import *

def pointeur(event):
    chaine.configure(text = "Clic détecté en X =" + str(event.x) +\
                               ", Y =" + str(event.y))

    x = event.x
    y = event.y
    cadre.create_oval(x-5, y-5, x+5, y+5, outline="red", fill="red")

fen = Tk()
cadre = Canvas(fen, width =200, height =150, bg="blue")
cadre.bind("<Button-1>", pointeur)
cadre.pack()
chaine = Label(fen)
chaine.pack()

fen.mainloop()