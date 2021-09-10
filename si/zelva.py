from turtle import Turtle, done
julie = Turtle()
p_uhlov = 3
max_uhlov = 9

for j in range(p_uhlov, max_uhlov + 1):
    print(j)
    print(360 / j)
    for i in range(j):
        julie.forward(100)
        julie.left(360 / j)
    j += 1
done()
