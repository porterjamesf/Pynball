from Tkinter import *
from wall import Wall
from table import Table

width = 384
height = 512

ball_radius = 16

root = Tk()

table = Table(width, height)
wall1 = Wall(0,height/5,width*0.6,height*0.8)
wall1.setBlockingPixels(ball_radius, table)

w = Canvas(root, width=width, height = height)

w.create_line(wall1.x1, wall1.y1, wall1.x2, wall1.y2, fill="#1010FF")

w.pack()

root.mainloop()
