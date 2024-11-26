food_prices = {
    "pizza": 12.99,
    "tacos": 8.99,
    "sushi": 15.99,
    "burger": 10.99,
}

for i in food_prices:
    print(f"{i} - ${food_prices[i]:.2f}")

selected_foods = input("Enter one or more food items separated by commas: ").split(",")
total_cost = 0
for food in selected_foods:
    if food in food_prices:
        total_cost += food_prices[food]
print(f"Total cost of selected foods: ${total_cost:.2f}")
