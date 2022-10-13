from operator import mod
from pulp import *
import pandas as pd
import numpy as np

n_warehouses = 2
n_customers = 4

# cost matrix
cost_matrix = np.array([[1,3,0.5,4],[2.5,5,1.5,2.5]])

cust_demands = np.array([35000, 22000, 18000, 30000])

warehouse_supply = np.array([60000, 80000])

model = LpProblem("Supplay-Demand-Problem", LpMinimize)

var_names = [str(i)+str(j) for j in range(1, n_customers+1) for i in range(1, n_warehouses+1)]
var_names.sort()
print("Variables Indices :", var_names)


DV_var = LpVariable.matrix("X", var_names, cat="Integer", lowBound=0)
allocation = np.array(DV_var).reshape(2,4)
print("Decision Variable / Allocation Matrix :")
print(allocation)

obj_func = lpSum(allocation*cost_matrix)
print(obj_func)
model += obj_func
print(model)

# supply constraints
for i in range(n_warehouses):
    print(lpSum(allocation[i][j] for j in range(n_customers)) <= warehouse_supply[i])
    model += lpSum(allocation[i][j] for j in range(n_customers)) <= warehouse_supply[i], "Supply Constraints" + str(i)

# demands constraints
for j in range(n_customers):
    print(lpSum(allocation[i][j] for i in range(n_warehouses)) >= cust_demands[j])
    model += lpSum(allocation[i][j] for i in range(n_warehouses)) >= cust_demands[j], "Demands Constraints " + str(j)

model.writeLP("Supply_demand_prob.lp")
model.solve(PULP_CBC_CMD())
status = LpStatus[model.status]
print(status)

print("Total Cost:", model.objective.value())

# decision variables
for v in model.variables():
    try:
        print(v.name,"=", v.value())
    except:
        print("err couldnt find val")

# req capacity
for i in range(n_warehouses):
    print("Warehouse ", str(i+1))
    print(lpSum(allocation[i][j].value() for j in range(n_customers)))