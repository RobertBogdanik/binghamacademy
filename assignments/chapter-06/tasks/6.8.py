def celsiusToFahrenheit(celsius):
    return (9 / 5) * celsius + 32

def fahrenheitToCelsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

celsius = 40
fahrenheit = 120

for x in range(10):
    print(f"{celsius}\t\t{round(celsiusToFahrenheit(celsius), 1)}\t|\t{fahrenheit}\t\t{round(fahrenheitToCelsius(fahrenheit), 1)}")
    celsius -= 1
    fahrenheit -= 10