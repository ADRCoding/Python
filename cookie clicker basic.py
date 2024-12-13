from cmu_graphics import *

Image('C:\\Users\\chess\\Downloads\\wp7667538_400x400.jpg', 0, 0)
score = Label(0, 200, 25, size = 50, fill = "green")
cookie = Circle(200, 200, 150, fill = rgb(90, 50, 20))
Circle(135, 109, 20, fill = rgb(70, 50, 20))
Circle(202, 143, 20, fill = rgb(70, 50, 20))
Circle(196, 282, 20, fill = rgb(70, 50, 20))
Circle(300, 199, 20, fill = rgb(70, 50, 20))
Circle(291, 111, 20, fill = rgb(70, 50, 20))
Circle(125, 228, 20, fill = rgb(70, 50, 20))
Circle(135, 109, 20, fill = rgb(70, 50, 20))


def onMousePress(x, y):
    if cookie.hits(x, y):
        score.value+=1

cmu_graphics.run()
