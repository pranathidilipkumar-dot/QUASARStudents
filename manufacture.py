# manufacturing.py
# tuple = (batch_id, product_name, units_produced, defective_units, cost_per_unit)

from manufacturing_utlis import total_manu_cost, overall_defect_percent

production = [
    ("501", "Circuit Board", 100, 5, 250),
    ("502", "Power Supply", 80, 12, 400),
    ("503", "Sensor", 150, 8, 180),
    ("504", "Controller", 60, 3, 650),
    ("505", "Connector", 200, 15, 50)
]

batch_cost = lambda b: b[2] * b[4]


def add_batch():
    """Add a batch with full validation using try/except/else/finally."""
    try:
        # --- may raise ValueError if input is non-numeric ---
        batch_id = input("Batch ID: ")
        product = input("Product name: ")
        units = int(input("Units produced: "))
        defective = int(input("Defective units: "))
        cost = float(input("Cost per unit: "))
    except ValueError:
        print("Error: units, defective units and cost must be numeric.")
        return
    else:
        # --- runs only if try block succeeded ---
        if units <= 0:
            print("Error: units produced must be positive.")
            return
        if defective < 0:
            print("Error: defective units cannot be negative.")
            return
        if cost < 0:
            print("Error: cost per unit cannot be negative.")
            return
        if defective > units:
            print("Error: defective units cannot exceed units produced.")
            return

        production.append((batch_id, product, units, defective, cost))
        print("Batch added.")
    finally:
        # --- always runs, regardless of success/failure ---
        print("Input processing finished.")


def view_batches():
    print("\nID\tProduct\tProduced\tDefective\tCost/Unit")
    for b in production:
        print(f"{b[0]}\t{b[1]}\t{b[2]}\t\t{b[3]}\t\t{b[4]}")


def high_defect_batches():
    high = list(filter(lambda b: b[3] > 10, production))
    if not high:
        print("No batches with more than 10 defective units.")
    else:
        print("\nBatches with defective units > 10:")
        for b in high:
            print(b)


def accepted_quantities():
    accepted = list(map(lambda b: b[2] - b[3], production))
    print("Accepted production quantities:", accepted)


def manu_cost_per_batch():
    costs = list(map(batch_cost, production))
    print("Manufacturing cost per batch:", costs)


while True:
    print("\n1 Add batch  2 View batches  3 Total manu cost  4 Defect %"
          "  5 High defect batches  6 Accepted quantities  7 Cost per batch  0 Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_batch()
    elif choice == "2":
        view_batches()
    elif choice == "3":
        print("Total manufacturing cost:", total_manu_cost(production))
    elif choice == "4":
        print("Overall defect %:", round(overall_defect_percent(production), 2))
    elif choice == "5":
        high_defect_batches()
    elif choice == "6":
        accepted_quantities()
    elif choice == "7":
        manu_cost_per_batch()
    elif choice == "0":
        break
    else:
        print("Invalid choice")