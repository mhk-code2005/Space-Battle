from Laser import laser

class spaceShip:
    #Init Cord ---> Main weight of the spaceship
    def __init__(self, initCord, modelNumber, color):
        self.coordList = [initCord]
        x,y = initCord
        self.model = modelNumber
        self.weight = initCord
        if modelNumber == 1:
            self.coordList.append((x,y+1)) 
            self.coordList.append((x,y+2))
            self.coordList.append((x,y-1))
            self.coordList.append((x+1,y))
            self.coordList.append((x-1,y))
            self.rightmost = x,y+2

        if modelNumber == 2:
            self.coordList.append((x,y+1))
            self.coordList.append((x,y+2))
            self.coordList.append((x+1,y))
            self.coordList.append((x-1,y))
            self.coordList.append((x-2,y))
            self.coordList.append((x-2,y+1))
            self.coordList.append((x+2,y))
            self.coordList.append((x+2,y+1))
            self.coordList.append((x,y-1))
            self.rightmost = x,y+2


        if modelNumber == 3:
            self.coordList.append((x,y+1))
            self.coordList.append((x,y-1))
            self.coordList.append((x,y-2))

            self.coordList.append((x+1,y))
            self.coordList.append((x-1,y))

            self.coordList.append((x+1,y-1))
            self.coordList.append((x-1,y-1))

            self.coordList.append((x+2,y-1))
            self.coordList.append((x-2,y-1))
            self.rightmost = x,y+1

        if modelNumber == "enemy":
            self.coordList.append((x,y-1))
            self.coordList.append((x+1,y))
            self.coordList.append((x-1,y))
            self.coordList.append((x,y+1))
        self.color = color

    def update(self,direction):
        directions = {"up":[0,-1],
                      "down":[0,+1],
                      "right":[1,+1],
                      "left":[1,-1],
                        }
        index = directions[direction][0]
       
        if self.model != 'enemy':
            x,y = self.rightmost
            if index == 0:
                self.rightmost = (x+directions[direction][1], y)
            if index == 1:
                self.rightmost = (x, y+directions[direction][1])


        for i in range(len(self.coordList)):
            x,y = self.coordList[i]
            if index == 0:
                self.coordList[i] = (x+directions[direction][1], y)
            if index == 1:
                self.coordList[i] = (x, y+directions[direction][1])

    def __str__(self):
        return 'ship: '+ str(self.model) 

    def shootLaser(self):
        x,y = self.rightmost

        bullet = laser((x,y+1),1,2,'lime')
        return bullet


        
