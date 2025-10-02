def fahrenheit_to_celsius(fahrenheit):
   
    return (5 / 9) * (fahrenheit - 32)

# Read temperature from user
f_temp = float(input("Enter temperature in Fahrenheit: "))

# Convert and display result
c_temp = fahrenheit_to_celsius(f_temp)
print(f"{f_temp}°F = {c_temp:.2f}°C")