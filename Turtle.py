import turtle
import math

def koch_inward(t, length, depth):
    """
    Draw a Koch-like segment with an inward indentation.
    If depth == 0: draw a straight line of given length.
    Otherwise: recurse on 4 segments with turns: R60, L120, R60.
    """
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_inward(t, length, depth - 1)
        t.right(60)          # go inward
        koch_inward(t, length, depth - 1)
        t.left(120)          # back out
        koch_inward(t, length, depth - 1)
        t.right(60)          # realign
        koch_inward(t, length, depth - 1)

def draw_fractal_polygon(n_sides, side_len, depth):
    """
    Draw a regular polygon where each edge is replaced by the inward Koch segment.
    Polygon is drawn clockwise so the 'V' points inward.
    """
    # Turtle setup
    screen = turtle.Screen()
    screen.title("Inward Koch Polygon")
    screen.setup(width=900, height=900)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(2)

    # Speed up drawing
    turtle.tracer(False)

    # Rough centering: start at bottom-left corner of the base polygon
    # Apothem helps place the polygon near the center.
    a = side_len / (2 * math.tan(math.pi / n_sides))
    t.penup()
    t.goto(-side_len / 2, -a)
    t.setheading(0)  # pointing to the right
    t.pendown()

    # Draw all sides with inward-INDENT Koch recursion
    exterior_turn = 360 / n_sides
    for _ in range(n_sides):
        koch_inward(t, side_len, depth)
        t.right(exterior_turn)  # clockwise -> interior is to the right

    turtle.update()
    screen.mainloop()

def main():
    # Inputs
    while True:
        try:
            n = int(input("Enter the number of sides: "))
            if n < 3:
                print("Please enter an integer >= 3.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    while True:
        try:
            side = float(input("Enter the side length (pixels): "))
            if side <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            depth = int(input("Enter the recursion depth (e.g., 0–5): "))
            if depth < 0:
                print("Please enter a non-negative integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    draw_fractal_polygon(n, side, depth)

if __name__ == "__main__":
    main()