# manufacturing_units.py
# Cost and defect calculations

def total_manu_cost(production):
    """Total manufacturing cost across all batches."""
    return sum(units * cost for _, _, units, _, cost in production)


def overall_defect_percent(production):
    """Overall defect percentage across all batches."""
    total_units = sum(units for _, _, units, _, _ in production)
    total_defective = sum(defective for _, _, _, defective, _ in production)
    if total_units == 0:
        return 0
    return (total_defective / total_units) * 100