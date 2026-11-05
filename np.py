import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 200)


y1 = x**3 - 2 * x + 10
y2 = -(x**3) + 2 * x + 10


plt.plot(x, y1, label="f1(x) = x^3 - 2x + 10", color="blue")
plt.plot(x, y2, label="f2(x) = -x^3 + 2x + 10", color="orange")

plt.title("Wykres funkcji f1(x) oraz f2(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
plt.grid(True)
plt.legend()

plt.show()