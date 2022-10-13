\* Supplay-Demand-Problem *\
Minimize
OBJ: X_11 + 3 X_12 + 0.5 X_13 + 4 X_14 + 2.5 X_21 + 5 X_22 + 1.5 X_23
 + 2.5 X_24
Subject To
Demands_Constraints_0: X_11 + X_21 >= 35000
Demands_Constraints_1: X_12 + X_22 >= 22000
Demands_Constraints_2: X_13 + X_23 >= 18000
Demands_Constraints_3: X_14 + X_24 >= 30000
Supply_Constraints0: X_11 + X_12 + X_13 + X_14 <= 60000
Supply_Constraints1: X_21 + X_22 + X_23 + X_24 <= 80000
Bounds
 0 <= X_11
 0 <= X_12
 0 <= X_13
 0 <= X_14
 0 <= X_21
 0 <= X_22
 0 <= X_23
 0 <= X_24
Generals
X_11
X_12
X_13
X_14
X_21
X_22
X_23
X_24
End
