# E-commerce Product Management System
# This program allows users to add, view, update, and delete products.

import json

PRODUCTS_FILE = "File_Handling/Day10/Day10_tasks/products.json"

def load_products():
    try:
        with open(PRODUCTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error loading products: {e}")
        return []

def save_products(products):
    try:
        with open(PRODUCTS_FILE, 'w') as file:
            json.dump(products, file, indent=4)
    except Exception as e:
        print(f"Error saving products: {e}")

def add_product():
    try:
        products = load_products()
        
        print("\nAdd New Product")
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        
        # Check if product ID already exists
        for product in products:
            if product['id'] == product_id:
                print("Product ID already exists!")
                return
        
        new_product = {
            'id': product_id,
            'name': name,
            'price': price,
            'quantity': quantity
        }
        
        products.append(new_product)
        save_products(products)
        print("Product added successfully!")
        
    except ValueError:
        print("Error: Please enter valid numbers for price and quantity!")
    except Exception as e:
        print(f"Error adding product: {e}")

def view_products():
    try:
        products = load_products()
        
        print("\nAll Products")
        if not products:
            print("No products found!")
            return
        
        for product in products:
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Quantity: {product['quantity']}")
            print("-" * 20)
            
    except Exception as e:
        print(f"Error viewing products: {e}")

def update_product():
    try:
        products = load_products()
        
        if not products:
            print("No products to update!")
            return
        
        print("\nUpdate Product")
        product_id = input("Enter product ID to update: ")
        
        for product in products:
            if product['id'] == product_id:
                print("Leave blank to keep current value:")
                
                name = input(f"Enter new name ({product['name']}): ") or product['name']
                
                price_input = input(f"Enter new price ({product['price']}): ")
                price = float(price_input) if price_input else product['price']
                
                quantity_input = input(f"Enter new quantity ({product['quantity']}): ")
                quantity = int(quantity_input) if quantity_input else product['quantity']
                
                product['name'] = name
                product['price'] = price
                product['quantity'] = quantity
                
                save_products(products)
                print("Product updated successfully!")
                return
        
        print("Product not found!")
        
    except ValueError:
        print("Error: Please enter valid numbers for price and quantity!")
    except Exception as e:
        print(f"Error updating product: {e}")

def delete_product():
    try:
        products = load_products()
        
        if not products:
            print("No products to delete!")
            return
        
        print("\nDelete Product")
        product_id = input("Enter product ID to delete: ")
        
        for i, product in enumerate(products):
            if product['id'] == product_id:
                products.pop(i)
                save_products(products)
                print("Product deleted successfully!")
                return
        
        print("Product not found!")
        
    except Exception as e:
        print(f"Error deleting product: {e}")

def main():
    while True:
        print("\nE-Commerce Product Management")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")
        
        try:
            choice = input("Enter your choice (1-5): ")
            
            if choice == '1':
                add_product()
            elif choice == '2':
                view_products()
            elif choice == '3':
                update_product()
            elif choice == '4':
                delete_product()
            elif choice == '5':
                print("Thank you for using the system!")
                break
            else:
                print("Invalid choice! Please enter 1-5.")
                
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()