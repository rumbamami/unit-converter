def show_menu():
    print("\nUnit Converter Menu:")
    print("1. Convert Kilometers to Miles")
    print("2. Convert Miles to Kilometers")
    print("3. Convert Celsius to Fahrenheit")
    print("4. Convert Fahrenheit to Celsius")
    print("5. Convert Kilograms to Pounds")
    print("6. Convert Pounds to Kilograms")
    print("7. Exit")

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

while True:
    show_menu()
    choice = input("\nChoose an option (1-7): ")
    
    if choice == "1":
        km = float(input("Enter kilometers: "))
        print(f"{km} km is equal to {km_to_miles(km):.2f} miles.")
    elif choice == "2":
        miles = float(input("Enter miles: "))
        print(f"{miles} miles is equal to {miles_to_km(miles):.2f} kilometers.")
    elif choice == "3":
        celsius = float(input("Enter Celsius: "))
        print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius):.2f}°F.")
    elif choice == "4":
        fahrenheit = float(input("Enter Fahrenheit: "))
        print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit):.2f}°C.")
    elif choice == "5":
        kg = float(input("Enter kilograms: "))
        print(f"{kg} kg is equal to {kg_to_pounds(kg):.2f} pounds.")
    elif choice == "6":
        pounds = float(input("Enter pounds: "))
        print(f"{pounds} pounds is equal to {pounds_to_kg(pounds):.2f} kilograms.")
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
