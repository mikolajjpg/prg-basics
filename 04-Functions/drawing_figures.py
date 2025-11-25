import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

side_lenght = 100
side_lenght2= 200

figures.draw_square(side_lenght)
figures.draw_trangle(side_lenght,150,0)
figures.draw_rectangle(side_lenght, side_lenght2, -150, 0)


window.mainloop()
