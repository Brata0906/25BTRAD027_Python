# MINI PROJECT
# Name: DOKI BRATA RANJAN
# USN: 25BTRAD027
#
# This file contains two programs:
# 1. Unit Converter
# 2. Bill Generator


# ============================================================
# 1. UNIT CONVERTER
# ============================================================

def unit_converter():
    while True:
        print("\n===== UNIT CONVERTER =====")
        print("1. Kilometers to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. Kilograms to Pounds")
        print("0. Exit")

        try:
            choice = int(input("Enter your choice (0-3): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            try:
                km = float(input("Enter distance in kilometers: "))
                miles = km * 0.621371
                print("Distance in Miles =", round(miles, 2))
            except ValueError:
                print("Please enter a valid distance.")

        elif choice == 2:
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = (celsius * 9 / 5) + 32
                print("Temperature in Fahrenheit =", round(fahrenheit, 2))
            except ValueError:
                print("Please enter a valid temperature.")

        elif choice == 3:
            try:
                kg = float(input("Enter weight in kilograms: "))
                pounds = kg * 2.20462
                print("Weight in Pounds =", round(pounds, 2))
            except ValueError:
                print("Please enter a valid weight.")

        elif choice == 0:
            print("Exiting Unit Converter.")
            break

        else:
            print("Invalid Choice!")


# ============================================================
# 2. BILL GENERATOR
# ============================================================

def bill_generator():
    print("=" * 40)
    print("             BILL GENERATOR")
    print("=" * 40)

    items = []
    total = 0.0

    while True:
        item = input("\nEnter Item Name: ").strip()
        if not item:
            print("Item name cannot be empty.")
            continue

        try:
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price per Item: ₹"))

            if quantity <= 0 or price < 0:
                print("Quantity must be positive and price cannot be negative.")
                continue
        except ValueError:
            print("Please enter a valid quantity and price.")
            continue

        amount = quantity * price
        total += amount
        items.append([item, quantity, price, amount])

        choice = input(
            "\nDo you want to add another item? (yes/no): "
        ).strip().lower()

        if choice != "yes":
            break

    gst = total * 0.18
    grand_total = total + gst

    print("\n" + "=" * 55)
    print("{:<20} {:<10} {:<10} {:<10}".format(
        "Item", "Qty", "Price", "Amount"
    ))
    print("=" * 55)

    for entry in items:
        print("{:<20} {:<10} ₹{:<9.2f} ₹{:<9.2f}".format(
            entry[0], entry[1], entry[2], entry[3]
        ))

    print("=" * 55)
    print(f"Subtotal          : ₹{total:.2f}")
    print(f"GST (18%)         : ₹{gst:.2f}")
    print(f"Grand Total       : ₹{grand_total:.2f}")
    print("=" * 55)

    try:
        paid = float(input("Amount Paid: ₹"))
        if paid >= grand_total:
            balance = paid - grand_total
            print(f"Balance Returned: ₹{balance:.2f}")
        else:
            due = grand_total - paid
            print(f"Amount Due: ₹{due:.2f}")
    except ValueError:
        print("Invalid payment amount.")

    print("\nThank you for shopping!")


# ============================================================
# MAIN MENU
# ============================================================

def main():
    while True:
        print("\n========== MINI PROJECT MENU ==========")
        print("1. Unit Converter")
        print("2. Bill Generator")
        print("3. Exit")

        choice = input("Choose a project (1-3): ").strip()

        if choice == "1":
            unit_converter()
        elif choice == "2":
            bill_generator()
        elif choice == "3":
            print("Exiting Mini Project. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
