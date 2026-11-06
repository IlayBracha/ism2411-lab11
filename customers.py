# Exercise 1 
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1200
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# Exercise 2 
customer["phone"] = "123-456-7890"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

# Exercise 3 
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email not found")

# Exercise 4
for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only goes through the keys.
for key in customer:
    print(key)

# Exercise 5 - Lookup Table
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount_rate = tier_discounts.get(tier, 0)

purchase_amount = 200
final_price = purchase_amount * (1 - discount_rate)

print("Tier:", tier)
print("Discount:", discount_rate * 100, "%")
print("Final price: $", round(final_price, 2))

# Exercise 6 - List of Dictionaries
customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Charlie", "tier": "silver"}
]

for person in customers:
    name = person["name"]
    tier = person["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount_rate

    print(f"{name}: {tier}, discount: ${discount_amount:.2f}")
