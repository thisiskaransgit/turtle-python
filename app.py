
# WINDOWS LOGO

#Importing turtle 
from turtle import * 

#setting turtle speed 
speed(1)
width(4)

#setting color to blue 
bgcolor('black')
color('blue')

begin_fill()
penup()


# moving turtle to starting point 
goto(-50,60)
pendown()
#going to right top
goto(100, 100)
#going to right bottom 
goto(100,-100)
#going to left bottom 
goto(-50,-60)

#going to starting point 
goto(-50,60)

end_fill()

penup()

#setting turtle color to black
color('black')

#changing width of the turtle 
width(10)

# cutting the shape into two equal haves horizontally 


# starting from left middle 
goto(-50,0)
pendown()

#ending at the right middle 
goto(100,0)
penup()

# cutting the shape into two halves vertically 

#starting from upper middle 
goto(25,80)
pendown()

#ending ar bottom middle 
goto(25,-80)

done()