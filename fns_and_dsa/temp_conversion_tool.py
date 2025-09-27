FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    
    results = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 
    print(f'{fahrenheit}°F is {results}°C')
def convert_to_fahrenheit(celsius):
    
    results = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32 
    print(f'{celsius}°C is {results}°F')

user_input = float(input("Enter the temperature to convert: "))
choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower() 

if choice == "f":
    convert_to_celsius(user_input)
elif choice == "c":
    convert_to_fahrenheit(user_input)
else:
    print("Invalid unit")
    