from docplex.mp.model import Model

m = Model(name="Production Jewelry")

prodNecklaces = m.continuous_var(name="Necklaces Productions")
prodBracelets = m.continuous_var(name="Bracelets Productions")

priceNecklaces = 300
priceBracelets = 400

goldConstraint = m.add_constraint((prodNecklaces*3 + prodBracelets*2) <= 18)
platConstraint = m.add_constraint((prodNecklaces*2 + prodBracelets*4) <= 20)

necklacesConstraint = prodNecklaces <= 4

m.maximize(prodNecklaces*priceNecklaces + prodBracelets*priceBracelets)
solver = m.solve()

