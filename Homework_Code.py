# TASK - ALLOW USER TO INPUT CHOICE IN ANY CASE
#      - (UPPER-CASE, LOWER-CASE, MIXED-CASE)
#      - PERFORM THE CHECK FUNCTIONALLY
#
#   HINT: Into function give the whole menu and the user choice
#       - If it matches in any case - return True
#       - Else return False
# change the menu to lower case in the function
# 2: go through code and deconstruct more

def pence_to_pound(pence):
    return f"£{pence / 100:.2f}"

def calculate_total(menu, order):
    total_pence = 0
    for row in order:
        total_pence = row["quantity"] * menu[row["item"]]
    return total_pence

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
    "Tea": 180,
}
def the_drink(menu, user_drink):
    menu_lowercase = {item.lower(): item for item in menu}
    user_drink_lowercase = user_drink.strip().lower()
    if user_drink_lowercase in menu_lowercase:
        return True, menu_lowercase[user_drink_lowercase]
    else:
        return False, None


# Step 2: Print the menu
print(" 🩷 Welcome to the Café!🩷 ")
print("----------------------------")
print("Drinks Menu:")

for item, price in menu.items():
    print(f"{item:15}: {pence_to_pound(price)}")

# Step 3: Ask the user for which item they want
# Step 4: Ask the user how many of that item they want

order = []

while True:
    another = "yes"
    choice = input("🩷 Which item would you like?🩷 ").strip()
    exists, drink_name = the_drink(menu, choice)    
    if exists:
        quantity = int(input(f"How many {drink_name}s would you like? ").strip())

        new_order_item = {"item": drink_name, "quantity": quantity}
        order.append(new_order_item)

        another = input("🩷 Would you like to order another item? (yes/no): ").strip().lower()
        if another != "yes":
            break
    else:
        print("🥺 Sorry, that item isn't on the menu.🥺")

print("Your order:")
for row in order:
    print(f"- {row['quantity']} x {row['item']}")

print(f"Total: {pence_to_pound(calculate_total(menu, order))}")

print("★｡.*☆ Thank you for choosing this cafe 💖☕✨ ☆*｡★");
