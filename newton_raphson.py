import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Function defination
def get_user_defined_function():
    try:
        user_input = input("Enter the function definition : ")
        if user_input:

            def f1(x):
                return eval(user_input)

            return f1

    except:
        print("Function defination is not valid\n use example function")

        def f2(x):
            return 2 * (x**2) + (16 / x)

        return f2


# First order derivative
def df(x, deltax):
    return (f(x + deltax) - f(x - deltax)) / (2 * deltax)


# Second order derivative
def df2(x, deltax):
    return (f(x + deltax) + f(x - deltax) - 2 * f(x)) / (deltax**2)


# Newton raphson
def newton_raphson(start, epsilon, ans=None, itr=1):
    if ans is None:
        ans = []

    if itr > 15:
        print("Not Converging\nTherefore Quiting\nTry another Starting point ")

    print(itr, start)
    ans.append([itr, start])
    deltax = start * epsilon
    next = start - (df(start, deltax) / df2(start, deltax))
    # Check Terminating Condition
    if abs(next - start) > epsilon:
        return newton_raphson(next, epsilon, ans, itr=itr + 1)
    else:
        print(itr, next)
        return ans


# Animation
def animate(frame, points, scat, x_values, y_values):
    point = points[frame]
    scat.set_offsets([[point[1], f(point[1])]])
    scat.set_label(f"Iter {point[0]}: ({point[1]:.2f}, {f(point[1]):.2f})")
    plt.legend()
    return scat


# Visualization
def visualize(ans):
    x_values = np.linspace(0.1, 10, 1000)  # Adjust the range as needed
    y_values = [f(x) for x in x_values]

    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, label="f(x)")
    scat = ax.scatter([], [], color="red")

    anim = FuncAnimation(
        fig,
        animate,
        frames=len(ans),
        fargs=(ans, scat, x_values, y_values),
        interval=1000,
        repeat=False,
    )

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Newton-Raphson Method")
    plt.grid(True)
    plt.show()


# Get Function
f = get_user_defined_function()
ans = newton_raphson(float(input("Initial Guess:    ")), float(input("Epsilon:      ")))
visualize(ans)
