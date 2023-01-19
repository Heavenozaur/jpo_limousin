from tkinter import *
import random

dim_x = 960
dim_y = 720


game = Tk()
game.title('Clément snake')

frame = Canvas(game,width = dim_x, height = dim_y, bg = 'white')
frame.grid(row=1,column=0,columnspan=3)

dino = PhotoImage(file='dino.png')
dino = dino.zoom(10)
dino = dino.subsample(70)

sol = PhotoImage(file='sol.png')

cactus = PhotoImage(file='cactus.png')
cactus = cactus.zoom(10)
cactus = cactus.subsample(20)

cactus2 = PhotoImage(file='cactus2.png')
cactus2 = cactus2.zoom(10)
cactus2 = cactus2.subsample(20)

Dino = frame.create_image(0,500, image = dino, anchor='nw')
Sol = frame.create_image(1370,700, image = sol)
Cactus = frame.create_image(1300,500, image = cactus)

bool = False


def next_image(event=None):
    frame.move(Sol, -10, 0)
    frame.after(10, next_image)
    x,y = frame.coords(Sol)
    if x<0 : 
        frame.move(Sol, 900, 0)

def apparition_cactus() :
    choix_image = random.randint(1,2)
    if choix_image == 1 : 
        frame.itemconfigure(Cactus,image=cactus)
    else :
        frame.itemconfigure(Cactus,image=cactus2)    
    frame.move(Cactus,1300,0)

def move_cactus() :
    frame.move(Cactus, -10, 0)
    x,y = frame.coords(Cactus)
    x1,y1= frame.coords(Dino)

    if x==-100 :
        apparition_cactus()
    elif x==x1+100 and y==y1 :
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



game.after_idle(move_cactus)
game.after_idle(next_image)


game.bind("<KeyPress-z>",dinoMonte)






game.mainloop()