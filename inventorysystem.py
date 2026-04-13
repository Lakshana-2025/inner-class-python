import sys

# Supplier Class
class Supplier:
    def __init__(self, sup_id, name):
        self.sup_id = sup_id
        self.name = name

    def display_supplier(self):
        print(f"Supplier ID: {self.sup_id}, Name: {self.name}")


# Product Class
class Product:
    def __init__(self, prod_id, name, supplier, spec):
        self.prod_id = prod_id
        self.name = name
        self.supplier = supplier   # reference to Supplier object
        self.spec = spec           # reference to Specification object

    # Inner Class
    class Specification:
        def __init__(self, color, weight):
            self.color = color
            self.weight = weight

        def display_spec(self):
            print(f"Color: {self.color}, Weight: {self.weight}")

    # Display Product Details
    def display_product(self):
        print(f"\nProduct ID: {self.prod_id}, Name: {self.name}")
        self.spec.display_spec()
        self.supplier.display_supplier()

        # Reference counts
        print("Reference count of Product:", sys.getrefcount(self))
        print("Reference count of Supplier:", sys.getrefcount(self.supplier))


# Inventory Manager
class Inventory:
    def __init__(self):
        self.products = []

    # Add Product
    def add_product(self):
        prod_id = int(input("Enter Product ID: "))
        name = input("Enter Product Name: ")

        sup_id = int(input("Enter Supplier ID: "))
        sup_name = input("Enter Supplier Name: ")
        supplier = Supplier(sup_id, sup_name)

        color = input("Enter Color: ")
        weight = input("Enter Weight: ")
        spec = Product.Specification(color, weight)

        product = Product(prod_id, name, supplier, spec)
        self.products.append(product)

        print(f"Product {name} added.")
        print("Reference count of Product:", sys.getrefcount(product))
        print("Reference count of Supplier:", sys.getrefcount(supplier))

    # Display All Products
    def display_all(self):
        if not self.products:
            print("No products available.")
        else:
            for product in self.products:
                product.display_product()


# Main Program
inv = Inventory()

while True:
    print("\n1. Add Product")
    print("2. Display Products")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        inv.add_product()
    elif choice == '2':
        inv.display_all()
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice")
