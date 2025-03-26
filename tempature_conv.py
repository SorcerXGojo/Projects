def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

if __name__ == "__main__":
    choice = input("Enter 1 to convert from Celsius to Fahrenheit, 2 to convert from Fahrenheit to Celsius, 3 to convert from Celsius to Kelvin, 4 to convert from Kelvin to Celsius, 5 to convert from Fahrenheit to Kelvin, or 6 to convert from Kelvin to Fahrenheit: ")
    if choice == '1':
        c = float(input("Enter the temperature in Celsius: "))
        result = celsius_to_fahrenheit(c)
        print("The temperature in Fahrenheit is", result)
    elif choice == '2':
        f = float(input("Enter the temperature in Fahrenheit: "))
        result = fahrenheit_to_celsius(f)
        print("The temperature in Celsius is", result)
    elif choice == '3':
        c = float(input("Enter the temperature in Celsius: "))
        result = celsius_to_kelvin(c)
        print("The temperature in Kelvin is", result)
    elif choice == '4':
        k = float(input("Enter the temperature in Kelvin: "))
        result = kelvin_to_celsius(k)
        print("The temperature in Celsius is", result)
    elif choice == '5':
        f = float(input("Enter the temperature in Fahrenheit: "))
        result = fahrenheit_to_kelvin(f)
        print("The temperature in Kelvin is", result)
    elif choice == '6':
        k = float(input("Enter the temperature in Kelvin: "))
        result = kelvin_to_fahrenheit(k)
        print("The temperature in Fahrenheit is", result)
    else:
        print("Invalid choice")