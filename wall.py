class Wall:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def setBlockingPixels(self, ball_radius, table):
        #ray-cast upper and lower lines
        cellx = int(self.x1)
        celly = int(self.y1)
        xdir = 1 if self.x2 > self.x1 else -1
        ydir = 1 if self.y2 > self.y1 else -1
        xtstep = 1/abs(self.x2 - self.x1)
        ytstep = 1/abs(self.y2 - self.y1)
        nextxt = abs((cellx + xdir/2 + .5 - self.x1) / (self.x2 - self.x1))
        nextyt = abs((celly + xdir/2 + .5 - self.y1) / (self.y2 - self.y1))
        #print "Cell: (%d,%d) Dir: (%d,%d) Tstep: (%f,%f) NextT: (%f,%f)" \
           # % (cellx, celly, xdir, ydir, xtstep, ytstep, nextxt, nextyt)
        while nextxt < 1 and nextyt < 1:
            if nextxt > nextyt:
                celly += ydir
                nextyt += ytstep
            else:
                cellx += xdir
                nextxt += xtstep
            table.pixels[cellx][celly] = [1.0, 1.0]
           # print "Next cell: (%d, %d)" % (cellx, celly)
        
        
        

