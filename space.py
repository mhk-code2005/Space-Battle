from math import factorial
from random import randint
import tkinter
from tkinter import *

from numpy import diff
from spaceship import spaceShip



class space:
    def __init__(self,x,y, master, laserColor = 'green'):
        self.map = {}
        self.lasers = []
        self.labels = []
        self.x = x
        self.y = y
        self.score = 0
        self.laserCord = {}

        for i in range(x):
            liste = []
            for j in range(y):
                self.map.update({(i,j):["black"]})
                q=Label(master, fg='white', bg='black',  width=2, height=1,borderwidth=1)#, relief="groove")
                q.grid(row = i, column = j)
                liste.append(q)
            self.labels.append(liste)

        self.spaceShips = []
        self.combinedCoord = {}

        for i in self.spaceShips:
            for j in i.coordList:
                self.combinedCoord.update({j:i.color})

    def addLaser(self, bullet):
        self.lasers.append(bullet)
        for i in bullet.coordList:
            self.combinedCoord.update({i:bullet.color})
            self.laserCord.update({i:bullet})

    def initiateTheMap(self, master):
        for i in self.map:
            q=Label(master, fg='white', bg=self.map[i][-1],  width=2, height=1,borderwidth=1)#, relief="groove")
            q.grid(row = i[0], column = i[1])
            self.labels.append(q)

    def addSpaceship(self, spaceship, i=1):
        self.spaceShips.append(spaceship)
        for i in spaceship.coordList:
            try:
                self.map[i][0] = spaceship.color
            except:
                pass

    def withinBounds(self,i):
        flag = False
        if -1<i[0]<self.x and -1<i[1]<self.y:
                flag = True 
        return flag

    def shipWithinBounds(self, laserOrSpacehip):
        flag = False
        for i in laserOrSpacehip.coordList:
            if self.withinBounds(i):
                flag = True
                break
        return flag
    
    def destroyLaser(self, bullet):
        self.lasers.remove(bullet)
        toBeDestroyed = []
        for i in self.laserCord:
            if self.laserCord[i] == bullet:
                toBeDestroyed.append(i)
        for i in toBeDestroyed:
            self.combinedCoord.pop(i)
            self.laserCord.pop(i)

    def quit(self, master):
        master.destroy()
        from IntroSpaceBattle import intro
        intro(self.score)
                         

    def updateCombinedCoord(self,master):

        self.laserCord = {}
        self.combinedCoord = {}
        for i in self.lasers:
            if self.shipWithinBounds(i):
                for j in i.coordList:
                    if self.withinBounds(j):
                        self.combinedCoord.update({j:i.color})
                        self.laserCord.update({j:i})
            
                i.updateLaser()
        toBeDestroyed = []
        for i in self.spaceShips:
            for j in i.coordList:      
                if self.shipWithinBounds(i):
                    if j[1] <= -1:
                        self.quit(master)
                    if self.withinBounds(j):
                        if j not in self.laserCord:
                            self.combinedCoord.update({j:i.color})
                        else:
                            toBeDestroyed.append(i)
                            self.score+=1
                            self.destroyLaser(self.laserCord[j])
                            break
                    
            if i.model == 'enemy':
                i.update('left')
        
        
        for i in toBeDestroyed:
            self.spaceShips.remove(i)
        

        coord = {}
        for i in self.combinedCoord:
            if self.withinBounds(i):
                coord.update({i:self.combinedCoord[i]})
        self.combinedCoord = coord

        main = self.spaceShips[0]
        for i in main.coordList:
            if self.combinedCoord[i] != main.color:
                print('quit accessed')
                self.quit(master)

        
    def updateMap(self):
        
        for i in self.map:
            if i in self.combinedCoord:
                color = self.combinedCoord[i]
            else:
                color = 'black'

            self.map[i][-1] = color
            x,y = i
            self.labels[x][y].configure(bg = color)

    def addEnemyShip(self):
        from random import randint, choice
        initPosY = randint(2,self.x-2)
        initPos = initPosY, self.y+1
        enemySpaceShip = spaceShip(initPos,'enemy', choice(['yellow', 'blue', 'white']))
        self.addSpaceship(enemySpaceShip)






