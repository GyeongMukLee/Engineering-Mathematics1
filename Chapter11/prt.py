import mathplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines["left"].set_position("center")
ax.spines["bottom"].set_position("zero")

ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")

xs = [x for x in range(-10, 11)]
ys = [x**2 for x in xs]

plt.plot(xs, ys)
plt.show()
