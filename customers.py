# Reflection 1:
# I would use .get() when some information might be missing.
# I would use brackets when I know the information exists.
# I think .get() is better when I am not sure.

# Reflection 2:
# This reminds me of using Excel to organize and calculate data.
# I think Python is better for large amounts of data because
# it can do the calculations automatically and save time.

# Exercise 1: 
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

# Exercise 2:
customer["phone"] = "123-456-7890"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

# Exercise 3: 
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email not found")

# Exercise 4:
for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only goes through the keys.
for key in customer:
    print(key)

# Exercise 5: 
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

# Exercise 6: 
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

# Exercise 7:
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product}")

# Exercise 8: 
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_by_region = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]}")
