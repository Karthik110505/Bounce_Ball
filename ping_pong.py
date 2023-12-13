from tkinter import *

import time
import random

window=Tk()
window.geometry("600x600+400+10")
window.title("PING-PONG")

canvas = Canvas(window,width=600,height=450,bg="black")
canvas.pack()

scores=IntVar()

score_board=Frame(window,width=150,height=60,background="white")
score_board.pack()

score_label=Label(score_board,text="SCORE",font=("Arial",20),bg="green",width=10)
score_label.pack()

score=Label(score_board,textvariable=scores,bg="orange",width=4)
score.pack()
count =0


def update_game():
    ball1.move()
    check_border()
    check_collision()
    check_bar()
    window.after(10, update_game)

def newgame():
    global ball1, count ,bar1
    count = 0  
    scores.set(count)
    ball1 = ball(25, "red", 1, 2)  
    bar1=bar(250,400,"blue")
    start.config(state="disabled")
    update_game()

def check_border():
    coordinates=canvas.coords(ball1.canvas)
    if coordinates[2] >= 600 or coordinates[0]<0:
        ball1.xv = - ball1.xv
    if coordinates[1]<0:
        ball1.yv = - ball1.yv

def check_collision():
    coordinates=canvas.coords(ball1.canvas)
    if coordinates[3] >=450:
        ball1.destroy()
        bar1.destroy()
        start.config(state="active")
        new_window()


def new_window():
    score_window=Tk()
    score_window.title("Score Board")
    score_window.geometry("600x600+400+10")
    score_canvas=Canvas(score_window,bg="black",width=600,height=600)
    score_canvas.pack()
    board=Label(score_canvas,text="YOUR SCORE",font=("Arial",30),fg="blue",bg="yellow")
    board.pack()
    display=Label(score_canvas,text=scores.get(),width=30,height=2,font=("Arial",20),background="black",fg="green")
    display.pack()
    score_window.mainloop()
    
'''
def check_bar():
    global count
    ball1_coordinates=canvas.coords(ball1.canvas)
    bar1_coordinates=canvas.coords(bar1.canvas)
    if ball1_coordinates[3] >= bar1_coordinates[1] and bar1_coordinates[0] <= ball1_coordinates[2] <= bar1_coordinates[0]+100:
        ball1.yv=-ball1.yv
        count+=1
        scores.set(value=count)    
'''

def check_bar():
    global count
    ball1_coordinates = canvas.coords(ball1.canvas)
    bar1_coordinates = canvas.coords(bar1.canvas)
    if ball1_coordinates[2] >= bar1_coordinates[0] and ball1_coordinates[0] <= bar1_coordinates[2]:
        if ball1_coordinates[3] >= bar1_coordinates[1] and ball1_coordinates[3] <= bar1_coordinates[3]:
            ball1.yv = -ball1.yv
            count += 1
            scores.set(value=count)

start =Button(window,text="START",font=("Arial",10),fg="blue",bg="yellow",relief=RAISED,bd=3,state="disabled",command=newgame)
start.pack()

class ball:
    def __init__(self,diameter,color,xv,yv):
        self.diameter =diameter
        self.color=color
        self.xv=xv
        self.yv=yv
        x=random.randint(0,600-self.diameter)
        y=random.randint(0,100)
        self.canvas=canvas.create_oval(x,y,x+diameter,y+diameter,fill=self.color)

    def move(self):
        canvas.move(self.canvas,self.xv,self.yv)
    
    def destroy(self):
        canvas.delete(self.canvas)    

ball1=ball(25,"red",1,2)

class bar:
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color=color
        self.canvas=canvas.create_rectangle(self.x,self.y,self.x+100,self.y+10,fill=self.color)
    def move(self,new_direction):
        bar_cordinates=canvas.coords(bar1.canvas)
        self.new_direction=new_direction
        if self.new_direction == "left":
            if bar_cordinates[0] > 10 : 
                canvas.move(self.canvas,-10,0)
        if self.new_direction == "right":
            if bar_cordinates[2] <=590 : 
                canvas.move(self.canvas,10,0)    
    def destroy(self):
        canvas.delete(self.canvas)    

bar1=bar(250,400,"blue")

window.bind("<Left>", lambda event: bar1.move("left"))
window.bind("<Right>", lambda event: bar1.move("right"))

def game_loop():
    while True:
        ball1.move()
        check_border()
        check_collision()
        check_bar()
        time.sleep(0.01)
        window.update()       
game_loop()

window.mainloop()

