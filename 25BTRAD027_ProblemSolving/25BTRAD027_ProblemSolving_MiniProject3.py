from datetime import datetime

# ============================================================
# MINI PROJECT 1: ATTENDANCE TRACKER
# ============================================================

students = {}


def get_date():
    """Get a valid date in YYYY-MM-DD format."""
    while True:
        value = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            return datetime.strptime(value, "%Y-%m-%d").date().isoformat()
        except ValueError:
            print("Invalid date! Use YYYY-MM-DD format.")


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty!")
        return

    if name.lower() in [student.lower() for student in students]:
        print("Student already exists!")
        return

    students[name] = {}
    print(f"Student '{name}' added successfully!")


def remove_student():
    name = input("Enter student name to remove: ").strip()
    actual_name = next(
        (student for student in students if student.lower() == name.lower()),
        None
    )

    if actual_name:
        del students[actual_name]
        print("Student removed successfully!")
    else:
        print("Student not found!")


def mark_attendance():
    name = input("Enter student name: ").strip()
    actual_name = next(
        (student for student in students if student.lower() == name.lower()),
        None
    )

    if actual_name is None:
        print("Student not found! Add the student first.")
        return

    attendance_date = get_date()

    print("1. Present")
    print("2. Absent")
    choice = input("Enter attendance status: ").strip()

    if choice == "1":
        status = "Present"
    elif choice == "2":
        status = "Absent"
    else:
        print("Invalid attendance choice!")
        return

    if attendance_date in students[actual_name]:
        print("Existing attendance record will be updated.")

    students[actual_name][attendance_date] = status
    print("Attendance saved successfully!")


def individual_report():
    name = input("Enter student name: ").strip()
    actual_name = next(
        (student for student in students if student.lower() == name.lower()),
        None
    )

    if actual_name is None:
        print("Student not found!")
        return

    records = students[actual_name]
    print("\\n----- INDIVIDUAL ATTENDANCE REPORT -----")
    print("Student Name:", actual_name)

    if not records:
        print("No attendance records available.")
        return

    present = 0
    absent = 0

    for attendance_date, status in sorted(records.items()):
        print(attendance_date, ":", status)
        if status == "Present":
            present += 1
        else:
            absent += 1

    total = present + absent
    percentage = (present / total) * 100

    print()
    print("Total Classes:", total)
    print("Present:", present)
    print("Absent:", absent)
    print("Attendance Percentage:", round(percentage, 2), "%")


def class_report():
    print("\\n========== CLASS ATTENDANCE REPORT ==========")

    if not students:
        print("No student records available.")
        return

    print(f"{'Student':<20}{'Total':<10}{'Present':<10}"
          f"{'Absent':<10}{'Percentage':<12}")
    print("-" * 62)

    for name, records in students.items():
        total = len(records)
        present = list(records.values()).count("Present")
        absent = total - present
        percentage = (present / total * 100) if total else 0

        print(f"{name:<20}{total:<10}{present:<10}"
              f"{absent:<10}{percentage:.2f}%")

    print("=" * 62)


def calculate_percentage():
    print("\\n----- ATTENDANCE PERCENTAGES -----")

    if not students:
        print("No student records available.")
        return

    for name, records in students.items():
        total = len(records)
        present = list(records.values()).count("Present")
        percentage = (present / total * 100) if total else 0
        print(f"{name}: {percentage:.2f}%")


def check_shortage():
    if not students:
        print("No student records available.")
        return

    while True:
        try:
            threshold = float(
                input("Enter minimum attendance percentage (0-100): ")
            )
            if 0 <= threshold <= 100:
                break
            print("Enter a value between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

    print(f"\\nStudents below {threshold}% attendance:")
    found = False

    for name, records in students.items():
        total = len(records)
        present = list(records.values()).count("Present")
        percentage = (present / total * 100) if total else 0

        if percentage < threshold:
            print(f"{name}: {percentage:.2f}%")
            found = True

    if not found:
        print("No students are below the threshold.")


def class_statistics():
    total_students = len(students)
    total_classes = sum(len(records) for records in students.values())
    total_present = sum(
        list(records.values()).count("Present")
        for records in students.values()
    )
    total_absent = total_classes - total_present

    print("\\n----- CLASS STATISTICS -----")
    print("Total Students:", total_students)
    print("Total Attendance Entries:", total_classes)
    print("Total Present Entries:", total_present)
    print("Total Absent Entries:", total_absent)

    percentage = (
        total_present / total_classes * 100 if total_classes else 0
    )
    print("Overall Attendance:", round(percentage, 2), "%")


def attendance_tracker():
    while True:
        print("\\n===================================")
        print("         ATTENDANCE TRACKER")
        print("===================================")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Mark / Update Attendance")
        print("4. Individual Attendance Report")
        print("5. Complete Class Report")
        print("6. Calculate Attendance Percentage")
        print("7. Check Attendance Shortage")
        print("8. Class Statistics")
        print("9. Exit")
        print("===================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            mark_attendance()
        elif choice == "4":
            individual_report()
        elif choice == "5":
            class_report()
        elif choice == "6":
            calculate_percentage()
        elif choice == "7":
            check_shortage()
        elif choice == "8":
            class_statistics()
        elif choice == "9":
            print("Thank you for using Attendance Tracker!")
            break
        else:
            print("Invalid choice! Please try again.")


# ============================================================
# MINI PROJECT 2: SALES DATA ANALYZER
# ============================================================

sales_data = {
    "Laptop": {"quantity": 10, "price": 45000},
    "Mobile": {"quantity": 20, "price": 15000},
    "Headphones": {"quantity": 30, "price": 2000},
    "Keyboard": {"quantity": 15, "price": 1000}
}


def add_or_update_product():
    name = input("Enter product name: ").strip().title()
    if not name:
        print("Product name cannot be empty!")
        return

    try:
        quantity = int(input("Enter quantity sold: "))
        price = float(input("Enter product price: "))
        if quantity < 0 or price < 0:
            print("Quantity and price cannot be negative.")
            return
    except ValueError:
        print("Please enter valid numeric values.")
        return

    if name in sales_data:
        sales_data[name]["quantity"] += quantity
        sales_data[name]["price"] = price
        print("Product record updated successfully!")
    else:
        sales_data[name] = {"quantity": quantity, "price": price}
        print("New product added successfully!")


def calculate_total_sales():
    total = 0
    for details in sales_data.values():
        total += details["quantity"] * details["price"]
    print("\\nTotal Sales Revenue: Rs.", total)


def display_sales():
    print("\\n---------- PRODUCT SALES REPORT ----------")
    print("{:<15} {:<12} {:<12} {:<12}".format(
        "Product", "Quantity", "Price", "Revenue"
    ))

    for product, details in sales_data.items():
        revenue = details["quantity"] * details["price"]
        print("{:<15} {:<12} {:<12} {:<12}".format(
            product,
            details["quantity"],
            details["price"],
            revenue
        ))


def highest_selling_product():
    if not sales_data:
        print("No product records available.")
        return

    highest = max(
        sales_data,
        key=lambda product: sales_data[product]["quantity"]
    )
    print("\\nHighest Selling Product:", highest)
    print("Quantity Sold:", sales_data[highest]["quantity"])


def compare_performance():
    print("\\n---------- SALES PERFORMANCE ----------")
    sorted_products = sorted(
        sales_data.items(),
        key=lambda item: item[1]["quantity"],
        reverse=True
    )

    for product, details in sorted_products:
        revenue = details["quantity"] * details["price"]
        print(product, "- Quantity:", details["quantity"],
              "| Revenue: Rs.", revenue)


def sales_data_analyzer():
    while True:
        print("\\n====== SALES DATA ANALYZER ======")
        print("1. Add or Update Product")
        print("2. Calculate Total Sales")
        print("3. Display Product-wise Sales")
        print("4. Find Highest-selling Product")
        print("5. Compare Product Performance")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_or_update_product()
        elif choice == "2":
            calculate_total_sales()
        elif choice == "3":
            display_sales()
        elif choice == "4":
            highest_selling_product()
        elif choice == "5":
            compare_performance()
        elif choice == "6":
            print("Thank you for using Sales Data Analyzer!")
            break
        else:
            print("Invalid choice! Please try again.")


# ============================================================
# PROGRAM SELECTION MENU
# ============================================================

def main():
    while True:
        print("\\n========== MINI PROJECTS ==========")
        print("1. Attendance Tracker")
        print("2. Sales Data Analyzer")
        print("3. Exit")

        choice = input("Choose a project: ").strip()

        if choice == "1":
            attendance_tracker()
        elif choice == "2":
            sales_data_analyzer()
        elif choice == "3":
            print("Exiting mini projects. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
