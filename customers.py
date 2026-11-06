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
