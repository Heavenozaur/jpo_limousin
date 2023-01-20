from tkinter import *
import random

dim_x = 960
dim_y = 720

score_joueur = 0

game = Tk()
game.title('Clément snake')

frame = Canvas(game,width = dim_x, height = dim_y, bg = 'white')
frame.grid(row=1,column=0,columnspan=3)

text = Text(frame, height=10, width=50)
text.insert(INSERT, "Hello.....")

dino1 = PhotoImage(file='dino1.png')
dino1 = dino1.zoom(25)
dino1 = dino1.subsample(10)

dino2 = PhotoImage(file='dino2.png')
dino2 = dino2.zoom(25)
dino2 = dino2.subsample(10)

sol = PhotoImage(file='sol.png')
sol = sol.zoom(5)


cactus = PhotoImage(file='cactus.png')
cactus = cactus.zoom(7)
cactus = cactus.subsample(5)

cactus2 = PhotoImage(file='cactus2.png')
cactus2 = cactus2.zoom(7)
cactus2 = cactus2.subsample(5)

cactus3 = PhotoImage(file='cactus3.png')
cactus3 = cactus3.zoom(7)
cactus3 = cactus3.subsample(5)

cactus4 = PhotoImage(file='cactus4.png')
cactus4 = cactus4.zoom(7)
cactus4 = cactus4.subsample(5)



Dino = frame.create_image(0,500, image = dino1, anchor='nw')
Sol = frame.create_image(500,670, image = sol)
Cactus = frame.create_image(1300,530, image = cactus)


photoDino = dino1

bool = False


def next_image(event=None):
    frame.move(Sol, -10, 0)
    frame.after(10, next_image)
    x,y = frame.coords(Sol)
    if x<0 : 
        frame.move(Sol, 1000, 0)

def apparition_cactus() :
    choix_image = random.randint(1,4)
    if choix_image == 1 : 
        frame.itemconfigure(Cactus,image=cactus)
    elif choix_image == 2 :
        frame.itemconfigure(Cactus,image=cactus2)
    elif choix_image == 3 :
        frame.itemconfigure(Cactus,image=cactus3) 
    elif choix_image == 4 :
        frame.itemconfigure(Cactus,image=cactus4) 
    frame.move(Cactus,1300,0)


def move_cactus() :
    frame.move(Cactus, -10, 0)
    x,y = frame.coords(Cactus)
    x1,y1= frame.coords(Dino)
    collision = frame.find_overlapping(x1=frame.bbox(Cactus)[0],y1=frame.bbox(Cactus)[1],x2=frame.bbox(Cactus)[2],y2=frame.bbox(Cactus)[3])
    print(collision)
    if x==-100 :
        apparition_cactus()
    elif len(collision) == 3:
        game.quit()

    frame.after(10, move_cactus)

def dinoMonte(event=None) : 
    if frame.coords(Dino)[1] >= 300 :
        frame.move(Dino, 0, -10)
        frame.after(5, dinoMonte)
    else :
        dinoDescend()

def dinoDescend() :
    if frame.coords(Dino)[1] != 500 :
        frame.move(Dino, 0, 10)
        frame.after(5, dinoDescend)

def dinoCourt() :
    global photoDino
    if photoDino == dino1 : 
        photoDino = dino2
    else :
        photoDino = dino1
    frame.itemconfigure(Dino,image=photoDino)  
    frame.after(100, dinoCourt)
    
def score_joueur() : 
    score+=1
    frame.after(100, score_joueur)


game.after_idle(move_cactus)
game.after_idle(next_image)
game.after_idle(dinoCourt)

game.bind("<KeyPress-z>",dinoMonte)

text.pack()
game.mainloop()