class laser:
    def __init__(self, initCord, velocity, length, color):
        self.initCord = initCord
        x,y = initCord
        self.velocity = velocity
        self.length = length
        self.coordList = []
        self.color = color
        for i in range(self.length):
            self.coordList.append((x,y+i))

    def updateLaser(self):
        for i in range(len(self.coordList)):
            x,y = self.coordList[i]
            self.coordList[i] = (x,y+self.velocity)