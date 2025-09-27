FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    results = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 
    print(f'{fahrenheit}°F is {results:.2f}°C')
    
def convert_to_fahrenheit(celsius):
    results = 32 + celsius * CELSIUS_TO_FAHRENHEIT_FACTOR
    print(f'{celsius}°C is {results:.2f}°F')

try:
    user_input = float(input("Enter the temperature to convert: "))
    choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower() 

    if choice == "f":
        convert_to_celsius(user_input)
    elif choice == "c":
        convert_to_fahrenheit(user_input)
    else:
        print("Invalid unit. Please enter C or F.")
        
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")