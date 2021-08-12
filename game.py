import random
import turtle as t

t.bgcolor('blue')

catterpillar=t.Turtle()
c=catterpillar
c.shape('square')
c.color('yellow')
c.speed(0)
c.penup()
c.hideturtle()

leaf=t.Turtle()
l=leaf
l_shape=((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
t.register_shape('leaf',l_shape)
l.shape('leaf')
l.color('green')
l.penup()
l.hideturtle()
l.speed(0)

game_started=False

text_on_screen=t.Turtle()
tx=text_on_screen
tx.write('PRESS SPACE TO START THE GAME',aligh='center',font=('Arial',20,'bold'))
tx.hideturtle()

score=t.Turtle()
s=score
s.hideturtle()
s.speed(0)

def outer():
 leftwall=-t.window_width()/2
 rightwall=t.window_width()/2
 topwall=t.window_width()/2
 bottomwall=-t.window_width()/2
 (x,y)=c.pos()
 out=\
  x<leftwall or \
  x>rightwall or \
  y<bottomwall or \
  y>topwall
 return out
 
def gameover():
 c.color('red')
 l.color('red')
 t.penup()
 t.hideturtle()
 t.write("GAME OVER :(",align='center',font=('Arial',20,'bold'))
 
def scoredisp(currentscore):
 s.clear()
 s.penup()
 x = (t.window_width() / 2) – 50
 y = (t.window_height() / 2) – 50
 s.setpos(x,y)
 s.write(str(currentscore),align='right',font=('Arial',20,'bold'))
 
def placeleaf():
 l.ht()
 l.setx(random.randint(-200,200))
 l.sety(random.randint(-200,200))
 l.st()
 
def startgame():
 global game_started
 if game_started:
  return
 game_started=True
 s=0
 tx.clear()
 
 c_speed=2
 c_length=5
 c.shapesize(1,c_length,1)
 c.showturtle()
 scoredisp(score)
 placeleaf()
 
 while True:
  c.forward(c_speed)
  if c.distance(l)<20:
   placeleaf()
   c_length=c_length+1
   c.shapesize(1,c_length,1)
   c_speed=c_speed+1
   s=s+10
   scoredisp(s)
  if outer():
   gameover()
   break
   
def moveup():
 if (c.heading()==0 or c.heading==180):
  c.setheading(90)
  
def movedown():
 if (c.heading==0 or c.heading==180):
  c.setheading(270)
  
def moveleft():
 if (c.heading==90 or c.heading=270):
  c.setheading(180)
  
def moveright():
 if (c.heading==90 or c.heading==270):
  c.setheading(0)
  
t.onkey(startgame,'space')
t.onkey(moveup,'Up')
t.onkey(movedown,'Down')
t.onkey(moveright,'Right')
t.onkey(moveleft,'Left')
t.listen()
t.mainloop()
