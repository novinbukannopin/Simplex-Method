from scipy.optimize import linprog

obj = [-2, -1]
lhs = [[2,1], [-5,4], [-1,4]]
rhs = [22,15,12]
lhs_eq = [[-1,4]]
rhs_eq = [16]

bnd = [(0, float('inf')), (0,float('inf'))]

optimization = linprog(c = obj, A_ub=lhs, b_ub=rhs, A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd, method='simplex')
print(optimization)