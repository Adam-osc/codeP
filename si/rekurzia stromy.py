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
    turtle.forward(length)

    while length >= min_length:
        return None



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
# draw_tree(julie, 120, 5) # NEZABUDNI PRED ODOVZDANÍM ODKOMENTOVAŤ!