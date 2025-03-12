import compute_utils as cu

a = float(input("Enter the value for a: "))
b = float(input("Enter the value for b: "))

print(a, " + ", b, " = ", cu.add(a, b))
print(a, " - ", b, " = ", cu.substract(a, b))
print(a, " x ", b, " = ", cu.multiply(a, b))
print(a, " / ", b, " = ", cu.divide(a, b))