from turtle import Turtle


# Tuto funkci implementuj.
def spiral(turtle: Turtle, side_length: float,
           angle: float, increment: float, max_length: float) -> None:
    """
    Parametry:
    julie: instancia triedy Turtle.
    side_length: dĺžka hrany v každom individuálnom rekurzívnom volaní.
    angle: uhol otočenia.
    increment: hodnota, o ktorú je každá ďalšia hrana väščia ako jej predošlá.
    max_length: udáva dĺžku najdlhšej možnej hrany.
    """

    # Upravuj iba kód pod týmto komentárom
    while side_length <= max_length:
        print("Side vs max: " + str(max_length - side_length))
        turtle.forward(side_length)
        turtle.right(angle)

        spiral(turtle, side_length + increment, angle, increment, max_length)
        return None
    pass


# Testy:
julie = Turtle()

spiral(julie, 10, 90, 1, 9) # Prázdne
spiral(julie, .01, 89.5, 2, 239)  # Vykreslí zadanú špirálu