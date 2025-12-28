from pulp import LpMaximize, LpProblem, LpVariable, value

def optimize_production():
    # Створюємо модель
    model = LpProblem("Drink_Production_Optimization", LpMaximize)

    # Змінні (кількість продуктів)
    lemonade = LpVariable("Lemonade", lowBound=0, cat="Integer")
    juice = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

    # Цільова функція
    model += lemonade + juice, "Maximize_total_products"

    # Обмеження ресурсів
    model += 2 * lemonade + 1 * juice <= 100, "Water_constraint"
    model += 1 * lemonade <= 50, "Sugar_constraint"
    model += 1 * lemonade <= 30, "Lemon_juice_constraint"
    model += 2 * juice <= 40, "Fruit_puree_constraint"

    # Розв’язання
    model.solve()

    return {
        "Lemonade": int(value(lemonade)),
        "Fruit Juice": int(value(juice)),
        "Total": int(value(lemonade + juice))
    }



import random
import math
from scipy.integrate import quad

def monte_carlo_integral(func, a, b, n=1_000_000):
    total = 0
    for _ in range(n):
        x = random.uniform(a, b)
        total += func(x)
    return (b - a) * total / n


def analytical_integral(func, a, b):
    result, _ = quad(func, a, b)
    return result


def f(x):
    return math.sin(x)


if __name__ == "__main__":
    # --- Завдання 1 ---
    production_result = optimize_production()
    print("=== Завдання 1 ===")
    print(production_result)

    # --- Завдання 2 ---
    a, b = 0, math.pi
    mc_result = monte_carlo_integral(f, a, b)
    exact_result = analytical_integral(f, a, b)

    print("\n=== Завдання 2 ===")
    print(f"Monte Carlo result: {mc_result}")
    print(f"Analytical (quad) result: {exact_result}")
    print(f"Absolute error: {abs(mc_result - exact_result)}")
