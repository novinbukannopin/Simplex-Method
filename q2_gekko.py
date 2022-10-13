from gekko import GEKKO
import matplotlib.pyplot as plt
import numpy as np
m = GEKKO()

x1 = m.Var(lb=0, ub=10) #products necklaces
x2 = m.Var(lb=0, ub=10) #products bracelets
m.Maximize(300*x1+400*x2) #max profit
m.Equation(3*x1+2*x2<=18) #constraint of gold
m.Equation(2*x1+4*x2<=20) #constraint of platinum
m.Equation(x1<=4) # necklaces must be less than 4
m.solve(disp=False)
p1 = x1.VALUE[0];
p2 = x2.VALUE[0];
print(int(p1)) #item of necklace
print(int(p2)) #item of bracelets
print(int(300*p1 + 400*p2)) #profit fix


x = np.linspace(0,20,100)
plt.plot(x, p1)
plt.plot(x, p2)
plt.show()