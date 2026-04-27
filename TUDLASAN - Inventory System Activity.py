#Initialize Inventory using a Dictionary: {name: price}
inventory = {
    "Laptop": 999.99,
    "Monitor": 299.50,
    "Keyboard": 75.00,
    "Mouse": 25.99
}

def display_inventory(inv):
 """Displays all products and their prices"""
 print("\n--- INVENTORY ---")
 if not inv:
     print("Inventory is empty")
     return
 # Iterates through key-value pairs
 for product, price in inv.items():
     print(f"{product:<10}: ${price:.2f}")
     
def update_price(inv):
    """Updates the price of an existing product"""
    product = input("\nUpdate price for: ").strip()
    
    if product in inv:
        try:
            current_price = inv[product]
            new_price = float(input(f"Enter new price for {product} (Current: ${current_price:.2f}:"))
            inv[product] = new_price 
    # Update the value associated with the key
            print(f"Price for *{product}* succesfully updates to *${new_price:.2f}*.")
        except ValueError:
            print("Invalid price entered. Please enter a valid number.")
        else:
            print(f"Product '{product}' not found.")
    def search_product(inv):
        """Searches for a product by name"""
        product = input("\nSearch for product: ").strip()
        
        if product in inv:
            print(f"Product Found: *{product}* has a price of *${inv[product]:.2f}*.")
        else:
            print(f"Product '{product}' not found.")
    
    # Main System Loop
    while True:
        print("\n--- MENU ---")
        choice = input("1. Display | 2. Update Price | 3. Search | 4. Exit: ")
        
        if choice == '1':
            display_inventory(inventory)
        elif choice == '2':
            update_price(inventory)
        elif choice == '3':
            search_product(inventory)
        elif choice == '4':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")