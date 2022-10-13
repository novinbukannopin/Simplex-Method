import matplotlib.pyplot as plt

# x + y <= 80
# ex y = 0
x1 = 80 - 0
# ex x = 0
y1 = 80 - 0 

# 2x + y <= 100
# ex y = 0
x2 = 100 / 2 - 0
# x + 0y <= 40
# ex x = 0
y2 = 100 - 0

# x + 0y <= 40
x3 = 40 - 0
y3 = 0

x = [0, x1]
y = [y1, 0]

q = [0, x2]
r = [y2, 0]

plt.plot(x,y)
plt.plot(q,r)
plt.show()