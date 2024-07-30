from datetime import datetime

item_list = [
    ("Apple", 30),
    ("Banana", 10),
    ("Orange", 20),
    ("Milk", 40),
    ("Bread", 25)
]

def generate_bill(items, filename):
    
    name = input("Enter your name: ")
    phn_no = input("Enter your phone number: ")  
    
    total_amount = sum(price * quantity for item, price, quantity in items)
    
    bill_content = []
    
    bill_content.append("----------- BILL -----------")
    bill_content.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    bill_content.append("----------------------------")
    
    for item, price, quantity in items:
        bill_content.append(f"{item} ({quantity} x ₹{price:.2f}): ₹{price * quantity:.2f}")
    
    bill_content.append("----------------------------")
    bill_content.append(f"Total Amount: ₹{total_amount:.2f}")
    bill_content.append(f"----------- THANK YOU  {name}  -----------")
    

    
    for line in bill_content:
        print(line)

    
    with open(filename, "a", encoding="utf-8") as file:
        for line in bill_content:
            file.write(line + "\n")

def main():
    items = []

    print("Available items:")
    for i, (item, price) in enumerate(item_list, start=1):
        print(f"{i}. {item} - ₹{price}")
    
    print("\nSelect items by number (type 'done' when finished):")
    
    while True:
        choice = input("Enter item number: ")
 
        if choice.lower() == 'done':
            break
        
        if choice.isdigit():
            choice_i = int(choice) - 1
            
            if 0 <= choice_i < len(item_list):
                item, price = item_list[choice_i]
                
                quantity_str = input(f"Enter quantity for {item}: ")
                if quantity_str.isdigit():
                    quantity = int(quantity_str)
                    if quantity > 0:
                        items.append((item, price, quantity))
                        print(f"Added {quantity} x {item} - ₹{price * quantity:.2f}")
                    else:
                        print("Quantity must be a positive integer. Please try again.")
                else:
                    print("Invalid quantity. Please enter a number.")
            else:
                print("Invalid item number. Please try again.")
        else:
            print("Invalid input. Please enter a number.")
    
    if items:
        filename = "bill.txt" 
        generate_bill(items, filename)
        print(f"Bill has been written to {filename}.")
    else:
        print("No items selected.")

if __name__ == "_main_":
    main()