#import des differents composants dont on aura besoin 
#///


#dimensions de la fenetre de jeu
dim_x = 960
dim_y = 720

#creation de la fenetre 
#///
game.title('Dino JPO')

#creation de l'élément principal de la fenetre qui accueillera les autres composants 

frame.grid(row=1,column=0,columnspan=3)

#importation des différentes images

#différents dinos
dino1 = PhotoImage(file='dino1.png')
dino1 = dino1.zoom(25)
dino1 = dino1.subsample(10)

dino2 = PhotoImage(file='dino2.png')
dino2 = dino2.zoom(25)
dino2 = dino2.subsample(10)

#image du sol qui tourne en boucle
sol = PhotoImage(file='sol.png')
sol = sol.zoom(5)

#images des différents cactus (trois types)
#///

cactus2 = PhotoImage(file='cactus2.png')
cactus2 = cactus2.zoom(7)
cactus2 = cactus2.subsample(5)

cactus3 = PhotoImage(file='cactus3.png')
cactus3 = cactus3.zoom(7)
cactus3 = cactus3.subsample(5)

cactus4 = PhotoImage(file='cactus4.png')
cactus4 = cactus4.zoom(7)
cactus4 = cactus4.subsample(5)

#creation de l'élément relatif à leurs images importées dans la fenêtre
Dino = frame.create_image(0,500, image = dino1, anchor='nw')
Sol = frame.create_image(500,670, image = sol)
Cactus = frame.create_image(1300,530, image = cactus)

#creation du score
#///

#initialisation des composants au début
photoDino = dino1
score_joueur = 0
vitesse = -10
bool = False

#fonction définissant la périodicité avec laquelle le sol revient (image en boucle)
def next_image(event=None):
    vitesse_changement()
    frame.move(Sol, -10, 0)
    frame.after(vitesse, next_image)
    x,y = frame.coords(Sol)
    if x<0 : 
        frame.move(Sol, 1000, 0)

#fonction définissant quel cactus apparait aléatoirement
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

#fonction définissant le mouvement du cactus ainsi que son apparition par rapport à sa position
def move_cactus() :
    vitesse_changement()
    frame.move(Cactus, -10, 0)
    x,y = frame.coords(Cactus)
    x1,y1= frame.coords(Dino)
    collision = frame.find_overlapping(x1=frame.bbox(Cactus)[0],y1=frame.bbox(Cactus)[1],x2=frame.bbox(Cactus)[2],y2=frame.bbox(Cactus)[3])
    if x==-100 :
        apparition_cactus()
    elif len(collision) == 3:
        game.quit()
    frame.after(vitesse, move_cactus)

#fonction de l'animation du saut du dinosaure
def dinoMonte(event=None) : 
   
    if frame.coords(Dino)[1] >= 300 :
        frame.move(Dino, 0, -10)
        frame.after(10, dinoMonte)
    else :
        dinoDescend()

#fonction de l'animation de la redesceente du dinosaure après un saut
def dinoDescend() :
    if frame.coords(Dino)[1] != 500 :
        frame.move(Dino, 0, 10)
        frame.after(10, dinoDescend)

#fonction codant le changement d'image du dinosaure pour l'animation de course
def dinoCourt() :
    global photoDino
    if photoDino == dino1 : 
        photoDino = dino2
    else :
        photoDino = dino1         
    frame.itemconfigure(Dino,image=photoDino)  
    frame.after(100, dinoCourt)

#fonction incrémentant le score d'un joueur toutes les 100 millisecondes
def incremente_score_joueur() : 
    global score_joueur
    #///
    frame.itemconfigure(Score,text="Score : "+str(score_joueur)) 
    #recursivite
    #///

#fonction augmentant la vitesse du cactus et du sol au fur et à mesure du score
def vitesse_changement() :
    global vitesse
    print(vitesse)
    if score_joueur < 99 :
        vitesse =  10
    elif score_joueur > 99 :
        vitesse = 10 - int(score_joueur/100)
    elif score_joueur > 999 :
        vitesse = 0 - int(score_joueur/1000)    

#fontions se lancent au démarrage du jeu
game.after_idle(move_cactus)
game.after_idle(next_image)
game.after_idle(dinoCourt)
game.after_idle(incremente_score_joueur)

#dinosaure saute à l'appui de la touche espace
#///

#lance la fenetre
game.mainloop()
