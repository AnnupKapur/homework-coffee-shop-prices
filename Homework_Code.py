# Step 1: Create a café menu with prices
menu = {
    "Espresso": 200,
    "Americano": 250,
    "Latte": 300,
    "Cappuccino": 320,
    "Mocha": 350,
    "Macchiato": 330,
    "Flat White": 300,
    "Hot Chocolate": 280,
    "Tea": 180
}

# Step 2: Print the menu
print(" 🩷 Welcome to the Café!🩷 ")
print("----------------------------")
print("Drinks Menu:")

for item, price in menu.items():
    print(f"{item:15} {price}p")

# Step 3: Ask the user for which item they want
# Step 4: Ask the user how many of that item they want


order = []
total = 0

while True:
    choice = input("🩷 Which item would you like?🩷 ").strip()
    if choice in menu:
        quantity = int(input(f"How many {choice}s would you like? ").strip())
        order.append(f"{quantity} x {choice}")
        total += menu[choice] * quantity
    else:
        print("🥺 Sorry, that item isn't on the menu.🥺")
    
    another = input("🩷 Would you like to order another item? (yes/no): ").strip().lower()
    if another != "yes":
        break

print("Your order:")
for item in order:
    print("-", item)

print(f"Total: £{total / 100:.2f}")


message = "Thank you for choosing this cafe 💖☕✨"

cutesy_message = f"""★｡.*☆ {message} ☆*｡★"""

print(cutesy_message)