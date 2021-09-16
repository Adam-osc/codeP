from turtle import Turtle

julie = Turtle()

# Tuto funkci implementuj.
def draw_tree(turtle: Turtle, length: int, min_length: int) -> None:
    """
    Parametry:
    julie: instancia triedy Turtle.
    length: dĺžka vetvy v každom individuálnom rekurzívnom volaní.
    min_length: udáva dĺžku najkratšej možnej vetvy
    """

    # Upravuj iba kód POD týmto komentárom
    if length >= min_length:
        turtle.forward(length)
        turtle.left(30)
        draw_tree(turtle, ((2 * length) / 3), min_length)
        turtle.right(60)
        draw_tree(turtle, ((2 * length) / 3), min_length)
        turtle.left(30)
        turtle.backward(length)
    else:
        return
    return


pass

# Upravuj iba kód NAD týmto komentárom
julie.penup()
julie.goto(0, -120)
julie.pendown()
julie.lt(90)

# Testy:

#  Strom z obrázku
draw_tree(julie, 120, 20)

# Strom, na ktorom sa testuje
draw_tree(julie, 120, 5)  # NEZABUDNI PRED ODOVZDANÍM ODKOMENTOVAŤ!
