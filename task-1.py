from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value

model = LpProblem(name="production-optimization", sense=LpMaximize)

lemonade = LpVariable(name="lemonade", lowBound=0, cat='Continuous')
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat='Continuous')

model += lpSum([lemonade, fruit_juice])

model += (2 * lemonade + 1 * fruit_juice <= 100, "Water")
model += (1 * lemonade <= 50, "Sugar")
model += (1 * lemonade <= 30, "Lemon juice")
model += (2 * fruit_juice <= 40, "Fruit puree")

model.solve()

print(f"Лимонад: {value(lemonade)}")
print(f"Фруктовий сік: {value(fruit_juice)}")
print(f"Всьго продукції: {value(model.objective)}")
