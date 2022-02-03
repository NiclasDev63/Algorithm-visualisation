import turtle

from idna import valid_string_length
window = turtle.Screen()

window.bgcolor("black")
window.title("Tiefensuche")
window.setup(1600, 900)

start_x =  10
start_y = 33

end_x = 33
end_y = 32

class Wall(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Green(Wall):
    def __init__(self):
        Wall.__init__(self)
        self.color("green")

class Red(Wall):
    def __init__(self):
        Wall.__init__(self)
        self.color("red")

grid = [
"1111111111111111111111111111111111",
"1000000000000000000000000000000001",
"1010111111111111100111111111110101",
"1010100001000000100001000000010101",
"1011101111111110111001011111010101",
"1000001000000010001001000100010101",
"1011101111111011101001110111011101",
"1011101111111011101001110111011101",
"1010101000001010001001010001000101",
"1010111011111010111001011101110101",
"1010000010000010100000000101000101",
"1010111110101110111111111101011101",
"1010100000101000000000000001010001",
"1010101011101111111111011111010101",
"1010101010100000000001010001010101",
"1010101010111110111111010111011101",
"1010101010100010100000000100000101",
"1010101010101110111111110111110101",
"1000101010101000000000010000010101",
"1011101110101111111001110111110101",
"1010000000100000000001000100010101",
"1010111110111011111101110101110101",
"1010100010001010000100010101000101",
"1011101110111010100111011101110101",
"1010001000101010100001010000010101",
"1010111011101010111101110111010101",
"1010100010100010000100000101000101",
"1010101110111011100111011101111101",
"1000100000101000100101010000000001",
"1000100000101000100101010000000001",
"1011101110101111111101010111110101",
"1010001010000000000000010100010101",
"101111101111111111111101110111111e",
"0000000000s00000000000000000000100",
"0000000000000000000000000000000000"]

def paint_blob(x, y, blob):
    screen_x = -500 + (x*24)
    screen_y = 400 - (y*24)
    blob.goto(screen_x, screen_y)
    blob.stamp()

def paint_maze(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            char = grid[y][x]

            if char == "s":
                print(f"start x: {x}")
                print(f"start y: {y}")
            if char == "e":
                print(f"end x: {x}")
                print(f"end y: {y}")

            screen_x = -500 + (x*24)
            screen_y = 400 - (y*24)

            if char == "0":
                wall.goto(screen_x, screen_y)
                wall.stamp()
            if char == "e":
                green.goto(screen_x, screen_y)
                green.stamp()
            if char == "s":
                red.goto(screen_x, screen_y)
                red.stamp()

def _depthFirstSearch(visited, x, y):
    visited[y][x] = True

    if x == end_x and y == end_y:
        print("Fund")
        return

    paint_blob(x, y, red)

    if x + 1 < 35 and grid[y][x + 1] not in visited and grid[y][x + 1] != "0":
        _depthFirstSearch(visited, x + 1, y)
 
    if  x - 1 >= 0 and grid[y][x - 1] not in visited and grid[y][x - 1] != "0":
        _depthFirstSearch(visited, x - 1, y)

    if y + 1 < 35 and grid[y + 1][x] not in visited and grid[y + 1][x] != "0":
        _depthFirstSearch(visited, x, y + 1)

    if y - 1 >= 0 and grid[y - 1][x] not in visited and grid[y - 1][x] != "0":
        _depthFirstSearch(visited, x, y - 1)

def depthFirstSearch():
    visited = []
    for _ in range(len(grid)):
        l = []
        for _ in range(len(grid[0])):
            l.append(False)
        visited.append(l)
    visited[0][0] = True
    _depthFirstSearch(visited, start_x, start_y)


if __name__ == "__main__":
    wall = Wall()
    green = Green()
    red = Red()
    paint_maze(grid)
    depthFirstSearch()
    window.exitonclick()