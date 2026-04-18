# SkillCraft Technology - Task 01
# Temperature Converter

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return fahrenheit_to_celsius(f) + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def main():
    print("=" * 45)
    print("   SkillCraft Technology - Task 01")
    print("       Temperature Converter")
    print("=" * 45)

    while True:
        print("\nSelect input scale:")
        print("  1. Celsius    (C)")
        print("  2. Fahrenheit (F)")
        print("  3. Kelvin     (K)")
        print("  4. Exit")
        print("-" * 45)

        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == '4':
            print("\nThank you! SkillCraft Technology - Task 01 Complete!")
            break

        if choice not in ['1', '2', '3']:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")
            continue

        try:
            value = float(input("Enter temperature value: "))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue

        print("\n" + "-" * 45)
        print("         Conversion Results")
        print("-" * 45)

        if choice == '1':
            print(f"  Celsius      : {value:.2f} C")
            print(f"  Fahrenheit   : {celsius_to_fahrenheit(value):.2f} F")
            print(f"  Kelvin       : {celsius_to_kelvin(value):.2f} K")
        elif choice == '2':
            print(f"  Fahrenheit   : {value:.2f} F")
            print(f"  Celsius      : {fahrenheit_to_celsius(value):.2f} C")
            print(f"  Kelvin       : {fahrenheit_to_kelvin(value):.2f} K")
        elif choice == '3':
            if value < 0:
                print("  Error: Kelvin cannot be negative!")
                continue
            print(f"  Kelvin       : {value:.2f} K")
            print(f"  Celsius      : {kelvin_to_celsius(value):.2f} C")
            print(f"  Fahrenheit   : {kelvin_to_fahrenheit(value):.2f} F")

        print("-" * 45)

if __name__ == "__main__":
    main()