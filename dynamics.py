from space import *
from spaceship import *
from Laser import *

def mainGame():
    master = tkinter.Tk()
    map = space(30,35, master)
    main = spaceShip((15,6),2,'red')

    map.addSpaceship(main)

    map.updateCombinedCoord(master)

    map.updateMap()

    master.update()
    master.title("SPACE BATTLE")
    frame = Frame(master, width=100, height=100)



    def toTheLeft(event):
        main.update('left')
    def toTheRight(event):
        main.update('right')
    def toTheDown(event):
        main.update('down')
    def toTheUp(event):
        main.update('up')
    def shoot(event):
        bullet = main.shootLaser()
        map.addLaser(bullet)



    master.bind('<Left>',toTheLeft )
    master.bind('<Right>', toTheRight)
    master.bind('<Up>', toTheUp)
    master.bind('<Down>', toTheDown)
    master.bind('<space>', shoot)

    data = []

    i = 0
    while True:
        map.updateCombinedCoord(master)
        map.updateMap()

        
        if i % 25 == 0 and i < 400:
            map.addEnemyShip()
        if i % 20 == 0 and i <800 and i>400:
            map.addEnemyShip()
        if i%10 and i > 800:
            map.addEnemyShip()

        master.update()
        master.update_idletasks()

        i+=1
