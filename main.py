def celsius_to_fahrenheit(celsius):
    
    return (celsius * 9/5) + 32
    
def fahrenheit_to_celsius(fahrenheit):
    
    return (fahrenheit - 32) * 5/9
    
c_or_f = input("Enter temperature type ('Celsius' or 'Fahrenheit'): ")

if c_or_f == "Celsius":
    
    degrees = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(degrees)
    print(str(degrees) + " degrees celsius equals " + str(fahrenheit) + " degrees fahrenheit")
    
elif c_or_f == "Fahrenheit":
    
    degrees = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(degrees)
    print(str(degrees) + " degrees fahrenheit equals " + str(celsius) + " degrees celsius")
    
else:
    
    print("Wrong input. Please put either Celsius or Fahrenheit. ")