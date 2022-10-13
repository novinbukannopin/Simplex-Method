import matplotlib.pyplot as plt

# 3x + 2y <= 18 -> persamaan 1
# 2x + 4y <= 20 -> persamaan 2

# persamaan 1
#  x?, y?
# mencari x 
nil = 0
x1 = 18 / 3 - (2 * nil)
print(x1)

# mencari y 
y1 = 18 / 2 - (3 * nil)
print(y1)

# ------------------------
# persamaan 2
# x?, y?
# mencari x
x2 = 20 / 2 - (4 * nil)
print(x2)

# mencari y
y2 = 20 / 4 - (2 * nil)
print(y2)

# print plot
eq1x = [nil, x1]
eq2x = [y1, nil]

eq1y = [nil, x2]
eq2y = [y2, nil]

plt.plot(eq1x, eq2x)
plt.plot(eq1y, eq2y)
plt.show()