# Step 1: Create a café menu with prices
menu = {
    "Espresso": 2.00,
    "Americano": 2.50,
    "Latte": 3.00,
    "Cappuccino": 3.20,
    "Mocha": 3.50,
    "Macchiato": 3.30,
    "Flat White": 3.00,
    "Hot Chocolate": 2.80,
    "Tea": 1.80
}

# Step 2: Print the menu
print(" 🩷 Welcome to the Café!🩷 ")
print("----------------------------")
print("Drinks Menu:")

for item, price in menu.items():
    print(f"{item:15} £{price:.2f}")